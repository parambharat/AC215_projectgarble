import ffmpeg
import logging
import os
import pathlib

# Imports the Google Cloud client library
from google.cloud import speech, storage
from tempfile import TemporaryDirectory

# Instantiates a client
gcp_project = "AC215_projectgarble"
bucket_name = "ac215-project-garble-bucket"
audio_files = "garble_audio"


def transcribe_audio_file(audio_path):
    print(f"Transcribing: {audio_path}")
    output_path = pathlib.Path(audio_path).stem.split(".")[0]

    client = speech.SpeechClient()

    with TemporaryDirectory() as audio_dir:
        flac_path = os.path.join(audio_dir, "audio.flac")
        stream = ffmpeg.input(audio_path)
        stream = ffmpeg.output(stream, flac_path)
        ffmpeg.run(stream)

        logging.debug("uploading file")
        storage_client = storage.Client(project=gcp_project)
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f"{audio_files}/audio.flac"
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(flac_path)
        logging.debug(
            "File {} uploaded to {}.".format(flac_path, destination_blob_name)
        )

        # Transcribe
        audio = speech.RecognitionAudio(
            uri=f"gs://{bucket_name}/{audio_files}/audio.flac"
        )
        config = speech.RecognitionConfig(language_code="en-US", enable_automatic_punctuation=True, model="video")
        logging.debug("Calling speech recognition client")
        operation = client.long_running_recognize(config=config, audio=audio)
        response = operation.result(timeout=180)
        logging.debug("Transcribed file sucessfully")
        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript
        if transcript:
            return transcript
