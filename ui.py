import flet as ft
from TTS.api import TTS
import requests
import io, os
from PIL import Image
from playsound import playsound as play
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import sounddevice as sd
from scipy.io.wavfile import write

def main(page: ft.Page):
    imageGen = ft.TextField(hint_text="What's needs to be done?", autofocus=True)
    musicField = ft.TextField(hint_text="Type of music")
    ttsField = ft.TextField(hint_text="TTS")

    def generate_image(e):
        API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
        headers = {"Authorization": "Bearer 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"}
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.content

        image_bytes = query({"inputs": imageGen.value})
        image = Image.open(io.BytesIO(image_bytes))
        image.save("output.jpg")
        page.update()

    def generate_music(e):
        text = [musicField.value]
        model = MusicGen.get_pretrained("medium", "cuda")
        model.set_generation_params(duration=10)
        audio = model.generate(text)
        audio_write("output_ag", audio[0].cpu(), model.sample_rate, strategy="loudness")

    def cloneTTS(e):
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

        tts.tts_to_file(
            text = ttsField.value,
            file_path = "output_tts.wav",
            speaker_wav = "target.wav",
            language = "ru"
            )
        page.update()

    def record(e):
        fs = 44100  # Sample rate
        seconds = 5  # Duration of recording

        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write('source.wav', fs, recording)  # Save as WAV file

    def generate_rvc(e):
        os.system("python inference.py --source source.wav --target target.wav --output ./")
    def play_music(e):
        play("output_ag.wav")
    def play_tts(e):
        play("output_tts.wav")
    def play_rvc(e):
            play("vc_source_target_1.0_30_0.7.wav")
    def clear(e):
        os.remove("output_tts.wav")
        os.remove("output.wav")
        os.remove("output.jpg")


    image_tab = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    imageGen,
                    ft.IconButton(icon=ft.icons.SEND, on_click=generate_image),
                ],
            ),
            ft.Image(src="output.jpg", width=300)
        ],
    )

    audio_tab = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    musicField,
                    ft.IconButton(icon=ft.icons.SEND, on_click=generate_music)
                ]
            ),
            ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=play_music)
                ]
            )
        ]
    )

    tts_tab = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ttsField,
                    ft.IconButton(icon=ft.icons.SEND, on_click=cloneTTS)
                ]
            ),
            ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=play_tts)
                ]
            )
        ]
    )

    rvc_tab = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.START, on_click=record),
                    ft.IconButton(icon=ft.icons.SEND, on_click=generate_rvc)
                ]
            ),
            ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=play_rvc)
                ]
            )
        ]
    )

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Image",
                content=image_tab
            ),
            ft.Tab(
                text="Audio",
                content=audio_tab
            ),
            ft.Tab(
                text="TTS",
                content=tts_tab
            ),
            ft.Tab(
                text="RVC",
                content=rvc_tab
            )
        ]
    )

    page.add(tabs)
    page.on_close=clear

ft.app(main)