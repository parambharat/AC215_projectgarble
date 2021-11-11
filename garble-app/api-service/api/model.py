from typing import Dict

from transformers import pipeline

summarization_pipeline = pipeline(
    "summarization",
    model="paulowoicho/t5-podcast-summarisation",
    tokenizer="paulowoicho/t5-podcast-summarisation",
)


def make_prediction(text: str) -> Dict[str, str]:
    """
    Makes a prediction using the model
    """
    print(summarization_pipeline(text)[0])
    summary = summarization_pipeline(text)[0]['summary_text']
    summary = summary.split('---')[0]
    
    return {"summary": summary}
