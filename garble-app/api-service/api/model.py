import logging
import os
from google.cloud import storage
from typing import Dict, Optional, Union

from transformers import LEDTokenizer, pipeline
from transformers.file_utils import PaddingStrategy
from transformers.tokenization_utils_base import BatchEncoding, EncodedInput

gcp_project = os.environ["GCP_PROJECT"]
bucket_name = "ac215-project-garble-bucket"
source_dir = "models/led-16k/checkpoint-2500"
local_models_path = "/persistent/models/led-16k/"


def download_model_dir(
    bucket_name=bucket_name, source_dir=source_dir, destination_dir=local_models_path
):
    """Downloads a blob from the bucket."""

    storage_client = storage.Client(project=gcp_project)

    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=source_dir)  # Get list of files

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for blob in blobs:
        blob_name = blob.name
        if blob.name.endswith("/"):
            continue
        dst_file_name = os.path.join(destination_dir, blob_name.split("/")[-1])
        logging.info("destination file: {}".format(dst_file_name))
        if not os.path.isfile(dst_file_name):
            blob.download_to_filename(dst_file_name)


class LEDTokenizerFixed(LEDTokenizer):
    def _pad(
        self,
        encoded_inputs: Union[Dict[str, EncodedInput], BatchEncoding],
        max_length: Optional[int] = None,
        padding_strategy: PaddingStrategy = PaddingStrategy.DO_NOT_PAD,
        pad_to_multiple_of: Optional[int] = None,
        return_attention_mask: Optional[bool] = None,
    ) -> dict:
        """
        Pad encoded inputs (on left/right and up to predefined length or max length in the batch)

        Args:
            encoded_inputs: Dictionary of tokenized inputs (`List[int]`) or batch of tokenized inputs (`List[List[int]]`).
            max_length: maximum length of the returned list and optionally padding length (see below).
                Will truncate by taking into account the special tokens.
            padding_strategy: PaddingStrategy to use for padding.

                - PaddingStrategy.LONGEST Pad to the longest sequence in the batch
                - PaddingStrategy.MAX_LENGTH: Pad to the max length (default)
                - PaddingStrategy.DO_NOT_PAD: Do not pad
                The tokenizer padding sides are defined in self.padding_side:

                    - 'left': pads on the left of the sequences
                    - 'right': pads on the right of the sequences
            pad_to_multiple_of: (optional) Integer if set will pad the sequence to a multiple of the provided value.
                This is especially useful to enable the use of Tensor Core on NVIDIA hardware with compute capability
                >= 7.5 (Volta).
            return_attention_mask: (optional) Set to False to avoid returning attention mask (default: set to model specifics)
        """
        # Load from model defaults
        if return_attention_mask is None:
            return_attention_mask = "attention_mask" in self.model_input_names

        required_input = encoded_inputs[self.model_input_names[0]]

        if padding_strategy == PaddingStrategy.LONGEST:
            max_length = len(required_input)

        if (
            max_length is not None
            and pad_to_multiple_of is not None
            and (max_length % pad_to_multiple_of != 0)
        ):
            max_length = ((max_length // pad_to_multiple_of) + 1) * pad_to_multiple_of

        needs_to_be_padded = (
            padding_strategy != PaddingStrategy.DO_NOT_PAD
            and len(required_input) != max_length
        )

        # Initialize attention mask if not present.
        if return_attention_mask and "attention_mask" not in encoded_inputs:
            encoded_inputs["attention_mask"] = [1] * len(required_input)

        if needs_to_be_padded:
            difference = max_length - len(required_input)

            if self.padding_side == "right":
                if return_attention_mask:
                    encoded_inputs["attention_mask"] = (
                        encoded_inputs["attention_mask"] + [0] * difference
                    )
                    encoded_inputs["global_attention_mask"] = (
                        encoded_inputs["global_attention_mask"] + [0] * difference
                    )
                if "token_type_ids" in encoded_inputs:
                    encoded_inputs["token_type_ids"] = (
                        encoded_inputs["token_type_ids"]
                        + [self.pad_token_type_id] * difference
                    )
                if "special_tokens_mask" in encoded_inputs:
                    encoded_inputs["special_tokens_mask"] = (
                        encoded_inputs["special_tokens_mask"] + [1] * difference
                    )
                encoded_inputs[self.model_input_names[0]] = (
                    required_input + [self.pad_token_id] * difference
                )
            elif self.padding_side == "left":
                if return_attention_mask:
                    encoded_inputs["attention_mask"] = [
                        0
                    ] * difference + encoded_inputs["attention_mask"]
                if "token_type_ids" in encoded_inputs:
                    encoded_inputs["token_type_ids"] = [
                        self.pad_token_type_id
                    ] * difference + encoded_inputs["token_type_ids"]
                if "special_tokens_mask" in encoded_inputs:
                    encoded_inputs["special_tokens_mask"] = [
                        1
                    ] * difference + encoded_inputs["special_tokens_mask"]
                encoded_inputs[self.model_input_names[0]] = [
                    self.pad_token_id
                ] * difference + required_input
            else:
                raise ValueError("Invalid padding strategy:" + str(self.padding_side))

        return encoded_inputs


class SummarizationPipeline:
    summarization_pipeline = pipeline(
        "summarization",
        model=local_models_path,
        tokenizer=LEDTokenizerFixed.from_pretrained(local_models_path),
    )

    def make_prediction(self, text: str) -> Dict[str, str]:
        """
        Makes a prediction using the model
        """
        print(self.summarization_pipeline(text)[0])
        summary = self.summarization_pipeline(text)[0]["summary_text"]
        summary = summary.split("---")[0]

        return {"summary": summary}
