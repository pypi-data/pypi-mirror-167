################################################################################
# File: /best_package/d02_modelling/model/my_network.py                        #
# Project: best_project                                                        #
# File Created: Wednesday, 14th September 2022 7:45:33 am                      #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 14th September 2022 7:45:33 am                     #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################

from ...d_utils.runtime_context import RuntimeContext
from .hyper_parameters import HyperParameters
import tensorflow as tf
import functools
from .my_model import MyModel
from flax.metrics import tensorboard
from tqdm.auto import tqdm
import jax
import jax.numpy as jnp
import optax
from flax.training import train_state, checkpoints
from flax import jax_utils
from flax.training.common_utils import get_metrics


@functools.partial(
    jax.pmap, axis_name="batch", static_broadcasted_argnums=(4, 5)  # , backend="gpu"
)
def train_step(
    replicated_state,
    replicated_metrics,
    replicated_rng,
    batch,
    num_classes,
    train=True,
):
    def loss_fn(params, rng_key, images, labels):
        labels_onehot = jax.nn.one_hot(labels, num_classes=num_classes)
        rng, dropout_apply_rng = jax.random.split(rng_key)
        logits = replicated_state.apply_fn(
            {"params": params},
            images,
            train=train,
            rngs={"dropout": dropout_apply_rng},
        )
        loss = optax.softmax_cross_entropy(logits, labels_onehot).mean()
        acc = (logits.argmax(axis=-1) == labels).mean()
        return loss, acc

    imgs = batch["image"]
    labels = batch["label"]
    grad_fn = jax.value_and_grad(loss_fn, has_aux=True)

    # Get loss, gradients for loss, and other outputs of loss function
    (loss, acc), grads = grad_fn(replicated_state.params, replicated_rng, imgs, labels)

    gathered_loss = jax.lax.pmean(loss, axis_name="batch")
    gathered_acc = jax.lax.pmean(acc, axis_name="batch")
    # accuracy = jnp.mean(jnp.argmax(probs, -1) == labels)
    grads = jax.lax.pmean(grads, axis_name="batch")
    # Update parameters and batch statistics
    replicated_state = replicated_state.apply_gradients(grads=grads)
    replicated_metrics["loss"] = gathered_loss
    replicated_metrics["acc"] = gathered_acc
    return replicated_state, replicated_metrics


train_step = jax_utils.pad_shard_unpad(
    train_step, static_argnums=(0, 1, 2, 4, 5), static_return=True
)


def train_epoch(
    replicated_state,
    replicated_metrics,
    train_dataset,
    replicated_rng,
    num_classes,
    per_device_batch_size,
    train=True,
):
    nb_samples = (
        train_dataset.cardinality().numpy()
        * per_device_batch_size
        * jax.local_device_count()
    )

    samples_progressbar = tqdm(
        total=nb_samples,
        desc="Training... %i samples" % nb_samples,
        position=1,
        leave=False,
    )
    batches_metrics = []
    # Train model for one epoch, and log avg loss and accuracy
    for batch in train_dataset.as_numpy_iterator():
        replicated_state, updated_replicated_metrics = train_step(
            replicated_state,
            replicated_metrics,
            replicated_rng,
            batch,
            num_classes,
            train,
            min_device_batch=per_device_batch_size,
        )
        batches_metrics.append(updated_replicated_metrics)
        samples_progressbar.update(per_device_batch_size * jax.local_device_count())
    batches_metrics = get_metrics(batches_metrics)
    batches_metrics = jax.tree_map(jnp.mean, batches_metrics)
    samples_progressbar.close()
    train_loss = round(batches_metrics["loss"].item(), 4)
    train_accuracy = round(batches_metrics["acc"].item(), 4)
    return replicated_state, train_loss, train_accuracy


@functools.partial(
    jax.pmap, axis_name="batch", static_broadcasted_argnums=(4, 5)  # , backend="gpu"
)
def eval_step(
    replicated_state,
    replicated_metrics,
    replicated_rng,
    batch,
    num_classes,
    train=False,
):
    def loss_fn(params, rng_key, images, labels):
        labels_onehot = jax.nn.one_hot(labels, num_classes=num_classes)
        rng, dropout_apply_rng = jax.random.split(rng_key)
        logits = replicated_state.apply_fn(
            {"params": params},
            images,
            train=train,
            rngs={"dropout": dropout_apply_rng},
        )
        loss = optax.softmax_cross_entropy(logits, labels_onehot).mean()

        acc = (logits.argmax(axis=-1) == labels).mean()
        return loss, acc

    imgs = batch["image"]
    labels = batch["label"]
    loss, acc = loss_fn(replicated_state.params, replicated_rng, imgs, labels)

    gathered_loss = jax.lax.pmean(loss, axis_name="batch")
    gathered_acc = jax.lax.pmean(acc, axis_name="batch")

    replicated_metrics["loss"] = gathered_loss
    replicated_metrics["acc"] = gathered_acc
    return replicated_metrics


eval_step = jax_utils.pad_shard_unpad(
    eval_step, static_argnums=(0, 1, 2, 4, 5), static_return=True
)


def eval_model(
    replicated_state,
    replicated_metrics,
    test_dataset,
    replicated_rng,
    num_classes,
    per_device_batch_size,
    train=False,
):
    nb_samples = (
        test_dataset.cardinality().numpy()
        * per_device_batch_size
        * jax.local_device_count()
    )

    samples_progressbar = tqdm(
        total=nb_samples,
        desc="Testing... %i samples" % nb_samples,
        position=1,
        leave=False,
    )
    batches_metrics = []
    # Train model for one epoch, and log avg loss and accuracy
    for batch in test_dataset.as_numpy_iterator():
        updated_replicated_metrics = eval_step(
            replicated_state,
            replicated_metrics,
            replicated_rng,
            batch,
            num_classes,
            train,
            min_device_batch=per_device_batch_size,
        )
        batches_metrics.append(updated_replicated_metrics)
        samples_progressbar.update(per_device_batch_size * jax.local_device_count())

    batches_metrics = get_metrics(batches_metrics)
    batches_metrics = jax.tree_map(jnp.mean, batches_metrics)
    samples_progressbar.close()
    test_loss = round(batches_metrics["loss"].item(), 4)
    test_accuracy = round(batches_metrics["acc"].item(), 4)

    return test_loss, test_accuracy


def create_train_state(hyper_parameters: HyperParameters, input_shape, rng_key):

    init_rng, dropout_init_rng = jax.random.split(rng_key, 2)

    mymodel = MyModel(
        embed_dim=hyper_parameters.embed_dim,
        patch_size=hyper_parameters.patch_size,
        dropout_prob=hyper_parameters.dropout_prob,
    )
    params = mymodel.init(
        {"params": init_rng, "dropout": dropout_init_rng},
        jnp.ones(list(input_shape)),
        train=True,
    )["params"]

    optimizer = optax.chain(
        optax.clip_by_global_norm(1.0),  # Clip gradients at norm 1
        optax.adamw(
            learning_rate=hyper_parameters.learning_rate,
            weight_decay=hyper_parameters.weight_decay,
        ),
    )
    # Initialize training state
    state = train_state.TrainState.create(
        apply_fn=mymodel.apply,
        params=params,
        tx=optimizer,
    )
    return state


def train_and_evaluate(
    hyper_parameters: HyperParameters,
    runtime_context: RuntimeContext,
    train_dataset: tf.data.Dataset,
    val_dataset: tf.data.Dataset,
    seed=42,
):
    log_dir = runtime_context.modelling_context.get_modelling_folder_path()
    if jax.process_index() == 0:
        summary_writer = tensorboard.SummaryWriter(log_dir)

    rng_key = jax.random.PRNGKey(seed)

    input_shape = next(iter(train_dataset))["image"].shape

    state = create_train_state(
        hyper_parameters=hyper_parameters, input_shape=input_shape, rng_key=rng_key
    )

    replicated_state = jax_utils.replicate(state)

    replicated_metrics = jax_utils.replicate(
        dict(loss=jnp.array(0, jnp.int32), acc=jnp.array(0, jnp.int32))
    )

    val_replicated_metrics = jax_utils.replicate(
        dict(loss=jnp.array(0, jnp.int32), acc=jnp.array(0, jnp.int32))
    )
    replicated_rng = jax.random.split(rng_key, jax.local_device_count())

    epochs = tqdm(
        range(1, hyper_parameters.number_epochs), desc=f"Epoch ...", position=0
    )

    for epoch in epochs:

        replicated_state, train_loss, train_accuracy = train_epoch(
            replicated_state,
            replicated_metrics,
            train_dataset,
            replicated_rng,
            hyper_parameters.num_classes,
            runtime_context.modelling_context.per_device_batch_size,
            True,
        )

        epochs.write(
            "Epoch... (%i/%i | Train Loss: %f, Train Accuracy:%f"
            % (
                epoch,
                hyper_parameters.number_epochs,
                train_loss,
                train_accuracy,
            )
        )
        if epoch % 2 == 0:
            val_loss, val_accuracy = eval_model(
                replicated_state,
                val_replicated_metrics,
                val_dataset,
                replicated_rng,
                hyper_parameters.num_classes,
                runtime_context.modelling_context.per_device_batch_size,
                False,
            )
            epochs.write(
                "Epoch... (%i/%i | Test Loss: %f, Test Accuracy:%f"
                % (
                    epoch,
                    hyper_parameters.number_epochs,
                    val_loss,
                    val_accuracy,
                )
            )

        if jax.process_index() == 0:
            summary_writer.scalar("train/loss", train_loss, epoch)
            summary_writer.scalar("train/accuracy", train_accuracy, epoch)
            if epoch % 2 == 0:
                summary_writer.scalar("val/loss", val_loss, epoch)
                summary_writer.scalar("val/accuracy", val_accuracy, epoch)

    summary_writer.flush()
    return state
