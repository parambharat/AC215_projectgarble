import api.model as model
import api.transcription as transcription
import logging
import os
from fastapi import FastAPI, File
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from tempfile import TemporaryDirectory

# Setup FastAPI app


app = FastAPI(title="API Server", description="API Server", version="v1")

# Enable CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    print("Starting up API Service")
    model.download_model_dir()


# Routes
@app.get("/")
async def get_index():
    return {"message": "Welcome to the API Service"}


@app.post("/transcribe")
async def transcribe(file: bytes = File(...)):
    print("Audio file:", len(file), type(file))

    # Save the image
    with TemporaryDirectory() as audio_dir:
        audio_path = os.path.join(audio_dir, "test.mp3")
        with open(audio_path, "wb") as output:
            output.write(file)

        # transcribe audio file
        transcription_results = transcription.transcribe_audio_file(audio_path)
        print("Transcription:", transcription_results)
    return transcription_results


class SummarizationRequest(BaseModel):
    transcript: str


@app.post("/summarize")
async def summarize(request: SummarizationRequest):
    pipeline = model.SummarizationPipeline()
    logging.debug("request:", request)
    data = request.dict()
    transcript = data["transcript"]
    summary = pipeline.make_prediction(transcript)
    logging.debug("Summary:", summary)
    return summary
