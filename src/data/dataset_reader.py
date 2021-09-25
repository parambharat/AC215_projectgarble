import pathlib
from collections import defaultdict
from multiprocessing import cpu_count
from pprint import pprint
from typing import Any, Dict

from datasets import DatasetDict, load_dataset

from src.data.utils import drop_columns


def load_json_paths(base_path: str) -> Dict[str, Any]:
    base_path = pathlib.Path(base_path)
    datasets_path = defaultdict(dict)
    for path in base_path.rglob("**/*.json.gz"):
        name_path = path.parent
        datasets_path[name_path.stem][path.stem] = str(path)
        datasets_path[name_path.stem]["task_type"] = str(name_path.parent.stem)
    datasets_path = dict(datasets_path)
    output_paths = {}
    for name, splits in datasets_path.items():
        output_paths[name] = {"task_type": splits.pop("task_type"), "splits": splits}
    return output_paths


def load_json_dataset(name: str, data_files: Dict, cache_dir: str) -> DatasetDict:
    dataset = load_dataset(
        "json", name=name, data_files=data_files, cache_dir=cache_dir
    )
    return dataset


def clean_examples_by_length(
    examples: Dict, document_length: int = 1, sentence_length: int = 1
) -> Dict:
    documents = []

    for document in examples["document"]:
        if len(document) > document_length:
            for sentence in document:
                if len(sentence) > sentence_length:
                    documents.append(document)
    return {"document": documents}


def convert_summarization_examples(examples: Dict) -> Dict:
    return {"document": examples["document"] + examples["summary"]}


def convert_segmentation_examples(examples: Dict) -> Dict:
    documents = [
        [sentence for segment in document for sentence in segment]
        for document in examples["document"]
    ]

    return {"document": documents}


def convert_summarization_dataset(
    dataset: DatasetDict, batch_size: int = 1000
) -> DatasetDict:
    dataset = dataset.map(
        convert_summarization_examples,
        batched=True,
        num_proc=cpu_count(),
        batch_size=batch_size,
        remove_columns=drop_columns(dataset, keep_columns=["document"]),
    )
    dataset = dataset.map(
        clean_examples_by_length,
        batched=True,
        num_proc=cpu_count(),
        batch_size=batch_size,
        remove_columns=drop_columns(dataset, keep_columns=["document"]),
    )
    return dataset


def convert_segmentation_dataset(
    dataset: DatasetDict, batch_size: int = 1000
) -> DatasetDict:
    dataset = dataset.map(
        convert_segmentation_examples,
        batched=True,
        num_proc=cpu_count(),
        batch_size=batch_size,
        remove_columns=drop_columns(dataset, keep_columns=["document"]),
    )
    dataset = dataset.map(
        clean_examples_by_length,
        batched=True,
        num_proc=cpu_count(),
        batch_size=batch_size,
        remove_columns=drop_columns(dataset, keep_columns=["document"]),
    )
    return dataset


def convert_unsupervised_dataset(
    dataset: DatasetDict, batch_size: int = 1000
) -> DatasetDict:
    dataset = dataset.map(
        clean_examples_by_length,
        batched=True,
        num_proc=cpu_count(),
        batch_size=batch_size,
        remove_columns=drop_columns(dataset, keep_columns=["document"]),
    )
    return dataset


def load_dataset_documents(dataset_paths, cache_dir):
    named_datasets = {}
    for name, task_info in dataset_paths.items():
        print(f"Loading {name} dataset")
        task_type = task_info["task_type"]
        dataset = load_json_dataset(name, task_info["splits"], cache_dir)
        if task_type == "summarization":
            dataset = convert_summarization_dataset(dataset)
        elif task_type == "segmentation":
            dataset = convert_segmentation_dataset(
                dataset,
            )
        elif task_type == "unsupervised":
            dataset = convert_unsupervised_dataset(dataset)
        named_datasets[name] = dataset
    return named_datasets


def main():
    cache_dir = "datasets/external/hf_datasets"
    # base_path = pathlib.Path("datasets/raw/supervised/summarization")
    # preprocess_dataset_from_hf(
    #     base_path=pathlib.Path("datasets/raw/supervised/summarization"),
    #     cache_dir=cache_dir,
    # )
    base_path = "datasets/raw/"
    json_paths = load_json_paths(base_path)
    pprint(json_paths)
    raw_datasets = load_dataset_documents(json_paths, cache_dir)
    # print(raw_datasets)


if __name__ == "__main__":
    main()
