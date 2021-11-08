import json
import pathlib
from multiprocessing import cpu_count
from typing import Dict

from datasets import DatasetDict, load_dataset
from nltk import sent_tokenize

from src.data.utils import drop_columns


def to_sentences(examples: Dict) -> Dict:
    document_sentences = []
    summary_sentences = []
    for document, summary in zip(examples["document"], examples["summary"]):
        document_sentence = [
            tok for sent in document.split("\n") for tok in sent_tokenize(sent)
        ]
        summary_sentence = [
            tok for sent in summary.split("\n") for tok in sent_tokenize(sent)
        ]
        document_sentences.append(document_sentence)
        summary_sentences.append(summary_sentence)
    return {
        "document": document_sentences,
        "summary": summary_sentences,
    }


def convert_cnn_dailymail_examples(examples: Dict) -> Dict:
    return {"document": examples["article"], "summary": examples["highlights"]}


def convert_cnn_dailymail_dataset(
    dataset: DatasetDict, batch_size: int = 1000
) -> DatasetDict:
    dataset = dataset.map(
        convert_cnn_dailymail_examples,
        batched=True,
        num_proc=cpu_count(),
        batch_size=batch_size,
        remove_columns=drop_columns(dataset, keep_columns=["document", "summary"]),
    )
    dataset = dataset.map(
        to_sentences,
        batched=True,
        num_proc=cpu_count(),
        batch_size=batch_size,
        remove_columns=drop_columns(dataset, keep_columns=["document", "summary"]),
    )

    return dataset


def convert_xsumm_dataset(dataset: DatasetDict, batch_size: int = 1000) -> DatasetDict:
    dataset = dataset.map(
        to_sentences,
        batched=True,
        num_proc=cpu_count(),
        batch_size=batch_size,
        remove_columns=drop_columns(dataset, keep_columns=["document", "summary"]),
    )
    return dataset


def convert_cc_news_examples(examples: Dict) -> Dict:
    output = {}
    output["document"] = examples["text"]
    output["summary"] = [
        "\n".join([title, description])
        for title, description in zip(examples["title"], examples["description"])
    ]
    return output


def convert_cc_news_dataset(
    dataset: DatasetDict, batch_size: int = 1000
) -> DatasetDict:
    dataset = dataset.map(
        convert_cc_news_examples,
        batched=True,
        num_proc=cpu_count(),
        batch_size=batch_size,
        remove_columns=drop_columns(dataset, keep_columns=["document", "summary"]),
    )
    dataset = dataset.map(
        to_sentences,
        batched=True,
        num_proc=cpu_count(),
        batch_size=batch_size,
        remove_columns=drop_columns(dataset, keep_columns=["document", "summary"]),
    )
    return dataset


def load_hf_dataset(dataset_name, cache_dir):
    dataset = None
    if dataset_name == "cnn_dailymail":
        dataset = load_dataset(dataset_name, "3.0.0", cache_dir=cache_dir)
        dataset = convert_cnn_dailymail_dataset(dataset)
    elif dataset_name == "xsum":
        dataset = load_dataset(dataset_name, cache_dir=cache_dir)
        dataset = convert_xsumm_dataset(dataset)
    elif dataset_name == "cc_news":
        dataset = load_dataset(dataset_name, cache_dir=cache_dir)
        train_test_dataset = dataset["train"].train_test_split(test_size=0.2)
        test_valid = train_test_dataset["test"].train_test_split(test_size=0.5)
        dataset = DatasetDict(
            {
                "train": train_test_dataset["train"],
                "test": test_valid["test"],
                "validation": test_valid["train"],
            }
        )
        dataset = convert_cc_news_dataset(dataset)
    return dataset


def preprocess_dataset_from_hf(base_path, cache_dir):
    cache_dir = "datasets/external/hf_datasets"
    base_path = pathlib.Path("datasets/raw/supervised/summarization")
    hf_datasets = ["cnn_dailymail", "xsum", "cc_news"]
    for dataset_name in hf_datasets:
        hf_dataset = load_hf_dataset(dataset_name, cache_dir)
        for split, dataset in hf_dataset.items():
            outfile_name = base_path.joinpath(dataset_name).joinpath(f"{split}.json")
            print(outfile_name)
            with outfile_name.open("w+") as outfile:
                for item in dataset:
                    outfile.write(json.dumps(item) + "\n")


def main():
    cache_dir = "datasets/external/hf_datasets"
    base_path = pathlib.Path("datasets/raw/supervised/summarization")
    preprocess_dataset_from_hf(base_path=base_path, cache_dir=cache_dir)


if __name__ == "__main__":
    main()
