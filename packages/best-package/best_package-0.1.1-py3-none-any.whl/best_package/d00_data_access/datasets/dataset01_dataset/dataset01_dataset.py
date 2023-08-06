"""ukbiobank_dataset dataset."""

import tensorflow_datasets as tfds
import csv
from zipfile import ZipFile
import io
from ....d_utils.runtime_context import RuntimeContext
import numpy as np
from PIL import Image
import tensorflow as tf

# TODO(ukbiobank_dataset): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
Description is **formatted** as markdown.

It should also contain any processing which has been applied (if any),
(e.g. corrupted example skipped, images cropped,...):
"""

# TODO(ukbiobank_dataset): BibTeX citation
_CITATION = """
"""


class Dataset01Dataset(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for ukbiobank_dataset dataset."""

    MANUAL_DOWNLOAD_INSTRUCTIONS = """ UKBIOBANK Manual Dataset
    """
    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {
        "1.0.0": "Initial release.",
    }
    rc: RuntimeContext = None

    def __init__(self, rc: RuntimeContext) -> None:
        self.rc = rc
        super().__init__()

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""
        # TODO(ukbiobank_dataset): Specifies the tfds.core.DatasetInfo object
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    # These are the features of your dataset like images, labels ...
                    "image": tfds.features.Image(
                        shape=(
                            512,
                            512,
                            1,
                        ),
                        dtype=tf.float32,
                    ),
                    "label": tfds.features.ClassLabel(num_classes=10),
                }
            ),
            # If there's a common (input, target) tuple from the
            # features, specify them here. They'll be used if
            # `as_supervised=True` in `builder.as_dataset`.
            supervised_keys=("image", "label"),  # Set to `None` to disable
            homepage="https://dataset-homepage/",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):

        """Returns SplitGenerators."""
        # TODO(ukbiobank_dataset): Downloads the data and defines the splits
        # path = dl_manager.download_and_extract("https://todo-data-url")
        path = dl_manager.manual_dir

        # TODO(ukbiobank_dataset): Returns the Dict[split names, Iterator[Key, Example]]
        return {
            "dataset01": self._generate_examples(path / "dataset01.csv"),
        }

    def _generate_examples(self, path):
        """Yields examples."""
        with path.open() as f:
            idx = 0
            for row in csv.DictReader(f):
                idx = idx + 1
                zip_file = ZipFile(row["eyeleft_t0"])

                image_slice_data = zip_file.read(zip_file.namelist()[65])

                p_id = row["eid"]
                image_data = Image.open(io.BytesIO(image_slice_data))
                image = np.array(image_data, dtype=np.float32)
                image = image.reshape(image.shape[0], image.shape[1], 1)
                label = row["target"]
                # TODO(ukbiobank_dataset): Yields (key, example) tuples from the dataset
                yield p_id, {
                    "image": image,
                    "label": label,
                }
