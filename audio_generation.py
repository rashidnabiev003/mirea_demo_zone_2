import requests
from IPython.display import Audio
import scipy
import numpy

API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-medium"
headers = {"Authorization": "Bearer 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"}


def generate_audio():
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    audio_bytes = query({"inputs": "liquid drum and bass, atmospheric synths, airy sounds", })
    sampling_rate = 48000
    #scipy.io.wavfile.write("musicgen_out.wav", rate=sampling_rate, data=audio_bytes)
    print(audio_bytes)

generate_audio()