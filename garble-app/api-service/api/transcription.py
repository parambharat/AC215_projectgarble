import io
import os
import pathlib
from tempfile import TemporaryDirectory

import ffmpeg

# Imports the Google Cloud client library
from google.cloud import speech


# Instantiates a client


def transcribe_audio_file(audio_path):
    print(f"Transcribing: {audio_path}")
    output_path = pathlib.Path(audio_path).stem.split(".")[0]

    client = speech.SpeechClient()

    with TemporaryDirectory() as audio_dir:
        flac_path = os.path.join(audio_dir, "audio.flac")
        stream = ffmpeg.input(audio_path)
        stream = ffmpeg.output(stream, flac_path)
        ffmpeg.run(stream)

        with io.open(flac_path, "rb") as audio_file:
            content = audio_file.read()

        # Transcribe
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(language_code="en-US")
        operation = client.long_running_recognize(config=config, audio=audio)
        response = operation.result(timeout=180)
        for result in response.results:
            transcript = result.alternatives[0].transcript
            if transcript:
                return transcript
