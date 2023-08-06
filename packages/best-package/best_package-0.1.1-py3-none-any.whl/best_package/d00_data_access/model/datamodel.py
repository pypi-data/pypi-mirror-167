from pathlib import Path


from dataclasses import dataclass
from ...d_utils.enums import Step


@dataclass
class DataSet:
    name: str
    is_in_separate_folder: bool

    def where_is_it(self, step: Step = None):
        return
