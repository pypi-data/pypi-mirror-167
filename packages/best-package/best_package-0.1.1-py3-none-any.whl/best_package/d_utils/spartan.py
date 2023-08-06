################################################################################
# File: /deepeye/d_utils/spartan.py                                            #
# Project: deep_eye_no_dementia                                                #
# File Created: Wednesday, 11th May 2022 2:49:00 am                            #
# Author: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                           #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 11th May 2022 2:49:01 am                           #
# Modified By: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                      #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from datetime import datetime
from pathlib import Path

from . import tools as tl
from .runtime_context import RuntimeContext

import subprocess
import os


def constrcut_job_slurm_file(rc: RuntimeContext):
    datnow = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    sparatn_dir = rc.execution_path
    # sparatn_dir = os.path.dirname(execution_path)
    Path(sparatn_dir + "/spartan_jobs").mkdir(parents=True, exist_ok=True)
    Path(sparatn_dir + "/spartan_outputs").mkdir(parents=True, exist_ok=True)
    filepath = sparatn_dir + "/spartan_jobs/job_%s.%s" % (datnow, "slurm")
    with open(filepath, "w") as f:
        f.write("#!/bin/bash\n")
        f.write(
            "# summary: %s, %s, \n"
            % (rc.config.get_data_set().name, rc.config.get_main_method().name)
        )
        f.write(
            "# epochs: %s, data sets included in training:[%s] ,\n"
            % (
                rc.config.get_number_epochs(),
                ", ".join(map(str, rc.config.get_data_set().name)),
            )
        )
        f.write(
            "# Created by the MDAP unimelb deepeye job script generator for SLURM\n"
        )
        f.write("# %s\n" % datnow)
        f.write("\n\n")
        f.write("# Partition for the job:\n")
        f.write("#SBATCH --partition=" + rc.config.get_spartan_partition() + "\n")
        f.write("\n\n")
        f.write("# Multithreaded (SMP) job: must run on one node\n")
        f.write("#SBATCH --nodes=1\n")
        f.write("#SBATCH -q " + rc.config.get_spartan_qos_setting() + "\n")
        f.write("\n\n")
        f.write("# The name of the job:\n")
        f.write('#SBATCH --job-name="deepeye_%s"\n' % datnow)
        f.write(
            "#SBATCH -o "
            + sparatn_dir
            + "/spartan_outputs/slurm_job_%s.%s" % (datnow, "out")
        )
        f.write("\n\n")
        f.write("# The project ID which this job should run under:\n")
        f.write('#SBATCH --account="' + rc.config.get_spartan_account() + '"\n')
        f.write("\n\n")
        f.write("# Maximum number of tasks/CPU cores used by the job:\n")
        f.write("#SBATCH --ntasks=1\n")
        f.write(
            "#SBATCH --cpus-per-task="
            + str(rc.config.get_spartan_cpus_per_task())
            + "\n"
        )
        f.write("\n\n")
        f.write("# Number of GPUs requested per node:\n")
        f.write(
            "#SBATCH --gres=gpu:" + str(rc.config.get_spartan_gpus_per_node()) + "\n"
        )
        f.write("\n\n")
        f.write("# The amount of memory in megabytes per process in the job:\n")
        f.write("#SBATCH --mem=" + str(rc.config.get_spartan_memory()) + "\n")
        f.write("\n\n")
        f.write("# The maximum running time of the job in days-hours:mins:sec\n")
        f.write(
            "#SBATCH --time="
            + str(rc.config.get_spartan_time_days())
            + "-"
            + str(rc.config.get_spartan_time_hours())
            + ":"
            + str(rc.config.get_spartan_time_minutes())
            + ":00\n"
        )
        f.write("\n\n")
        f.write("# check that the script is launched with sbatch\n")
        f.write('if [ "x$SLURM_JOB_ID" == "x" ]; then\n')
        f.write(
            'echo "You need to submit your job to the queuing system with sbatch"\n'
        )
        f.write("exit 1\n")
        f.write("fi\n")
        f.write("\n\n")
        f.write("# Run the job from the directory where it was launched (default)\n")
        f.write("\n\n")
        f.write("# The modules to load\n")

        f.write("module load cuda/11.7.0\n")
        f.write("module load cudnn/8.2.1.32-cuda-11.3.1\n")
        f.write("\n\n")
        f.write("# The job command(s):\n")
        f.write("#source activate " + rc.config.get_spartan_conda_env() + "\n")
        f.write("conda info --envs\n")

        # which python
        # python --version
        f.write("time python " + sparatn_dir + "/main.py spartan")
    return filepath


def run_job(job_file_name):
    completed = subprocess.run("sbatch " + job_file_name, shell=True)
    print("returncode:", completed.returncode)
    return


def generate_and_submit_spartan_job(rc: RuntimeContext):
    job_slurm_file_name = constrcut_job_slurm_file(rc)
    run_job(job_slurm_file_name)


if __name__ == "__main__":
    job_slurm_file_name = constrcut_job_slurm_file()
    run_job(job_slurm_file_name)
