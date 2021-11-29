import os
from tempfile import TemporaryDirectory

import api.model as model
import api.transcription as transcription
from fastapi import FastAPI, File
from starlette.middleware.cors import CORSMiddleware

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


# Routes
@app.get("/")
async def get_index():
    return {"message": "Welcome to the API Service"}


@app.post("/predict")
async def predict(file: bytes = File(...)):
    print("predict file:", len(file), type(file))

    # Save the image
    with TemporaryDirectory() as audio_dir:
        audio_path = os.path.join(audio_dir, "test.mp3")
        with open(audio_path, "wb") as output:
            output.write(file)

        # transcribe audio file
        transcription_results = transcription.transcribe_audio_file(audio_path)
        print('Transcription:', transcription_results)
        # Make prediction
        prediction_results = model.make_prediction(transcription_results)
        print('Summary:', prediction_results)

    return prediction_results

@app.post("/apipredict")
async def predict(file: bytes = File(...)):
    print("predict file:", len(file), type(file))

    # Save the image
    with TemporaryDirectory() as audio_dir:
        audio_path = os.path.join(audio_dir, "test.mp3")
        with open(audio_path, "wb") as output:
            output.write(file)

        # transcribe audio file
        transcription_results = transcription.transcribe_audio_file(audio_path)
        print('Transcription:', transcription_results)
        # Make prediction
        prediction_results = model.make_prediction(transcription_results)
        print('Summary:', prediction_results)

    return prediction_results
