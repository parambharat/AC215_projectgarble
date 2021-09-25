from typing import List

from datasets import DatasetDict


def drop_columns(dataset: DatasetDict, keep_columns: List[str]) -> List[str]:
    if isinstance(dataset, DatasetDict):
        columns = list(
            set(
                [
                    item
                    for sublist in dataset.column_names.values()
                    for item in sublist
                    if item not in keep_columns
                ]
            )
        )
        return columns
