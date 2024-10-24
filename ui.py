import flet as ft
from TTS.api import TTS
import requests
import io, subprocess, os, base64
from PIL import Image
from playsound import playsound as play
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import sounddevice as sd
from scipy.io.wavfile import write
import json as js

import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

def record(e):
    fs = 22050  # Sample rate
    seconds = 5  # Duration of recording

    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write('source.wav', fs, recording)  # Save as WAV file

def rvc_gen(old, new):
    write('source.wav', old[0], old[1])
    write('target.wav', new[0], new[1])
    os.system("python inference.py")
    return "./output_rvc.wav"

demo = gr.Interface(
    fn=rvc_gen,
    inputs=["audio", "audio"],
    outputs=["audio"],
)

demo.launch(share=True)


API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def main(page: ft.Page):
    progress = ft.ProgressRing()

    def generate_image(e):
        # try:
        #     os.remove("output.jpg")
        # except:
        #     pass
        # imageTab.controls.remove(imageSrc)
        imageRow.controls.remove(imageButton)
        imageRow.controls.append(progress)
        page.update()

        image_bytes = query({"inputs": imageField.value})
        image = Image.open(io.BytesIO(image_bytes))

        buff = io.BytesIO()
        image.save(buff, format="JPEG")

        newstring = base64.b64encode(buff.getvalue()).decode("utf-8")

        imageSrc.src_base64 = newstring
        imageRow.controls.remove(progress)
        imageRow.controls.append(imageButton)
        page.update()

        #os.remove("output.jpg")


    def generate_music(e):
        audioRow.controls.remove(musicButton)
        audioRow.controls.append(progress)
        page.update()
        text = [musicField.value]
        model = MusicGen.get_pretrained("medium", "cuda")
        model.set_generation_params(duration=10)
        audio = model.generate(text)
        audio_write("output_ag", audio[0].cpu(), model.sample_rate, strategy="loudness")
        audioRow.controls.remove(progress)
        audioRow.controls.append(musicButton)
        page.update()

    def cloneTTS(e):
        ttsRow.controls.remove(ttsButton)
        ttsRow.controls.append(progress)
        page.update()

        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

        tts.tts_to_file(
            text = ttsField.value,
            file_path = "output_tts.wav",
            speaker_wav = "target.wav",
            language = "ru"
            )

        ttsRow.controls.remove(progress)
        ttsRow.controls.append(ttsButton)
        page.update()

    def record(e):
        rvcRec.icon = ft.icons.PAUSE_CIRCLE
        rvcRec.disabled = True
        page.update()
        fs = 22050  # Sample rate
        seconds = 5  # Duration of recording

        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()  # Wait until recording is finished
        write('source.wav', fs, recording)  # Save as WAV file
        rvcRec.icon = ft.icons.PLAY_ARROW_ROUNDED
        rvcRec.disabled = False
        page.update()

    def generate_rvc(e):
        rvcText.value = "Processing..."
        page.update()
        os.system("python inference.py")
        rvcText.value = ""
        page.update()

    def clear(e):
        # pass
        os.system("rm /r output_tts.wav")
        os.remove("output_ag.wav")
        os.remove("output.jpg")
        os.remove("output1.jpg")

    imageField = ft.TextField(hint_text="What's needs to be done?", autofocus=True)
    imageButton = ft.IconButton(icon=ft.icons.SEND, on_click=generate_image)
    imageSrc = ft.Image(src="output.jpg", width=300)

    imageRow = ft.Row(
                controls=[
                    imageField,
                    imageButton
                ],
            )

    imageTab = ft.Column(
        controls=[
            ft.Text(value="Опишите картинку и нажмите на кнопку для обработки"),
            imageRow,
            ft.Text(value="Сгенерированное изображение"),
            imageSrc
        ],
    )

    musicField = ft.TextField(hint_text="Type of music")
    musicButton = ft.IconButton(icon=ft.icons.SEND, on_click=generate_music)

    audioRow = ft.Row(
                controls=[
                    musicField,
                    musicButton
                ]
            )

    audioTab = ft.Column(
        controls=[
            ft.Text(value="Впишите жанры, которые хотите услышать и нажмите на кнопку для обработки"),
            audioRow,
            ft.Text(value="Нажмите на кнопку play чтобы прослушать результат"),
            ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=lambda e: play("output_ag.wav"))
        ]
    )

    ttsField = ft.TextField(hint_text="TTS")
    ttsButton = ft.IconButton(icon=ft.icons.SEND, on_click=cloneTTS)

    ttsRow =  ft.Row(
                controls=[
                    ttsField,
                    ttsButton
                ]
            )

    ttsTab = ft.Column(
        controls=[
            ft.Text(value="Впишите текст, который хотите озвучить и нажмите на кнопку для обработки"),
            ttsRow,
            ft.Text(value="Нажмите на кнопку play чтобы прослушать результат"),
            ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=lambda e: play("output_tts.wav")),
        ]
    )

    rvcRec = ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=record)
    rvcText = ft.Text(value="")
    rvcButton = ft.IconButton(icon=ft.icons.SEND, on_click=generate_rvc)

    rvcRow = ft.Row(
                controls=[
                    rvcButton,
                    rvcText
                ]
            )

    rvcTab = ft.Column(
        controls=[
            ft.Text(value="Нажми, чтобы начать запись аудио на 5 секунд"),
            rvcRec,
            ft.Text(value="Нажми, чтобы изменить голос"),
            rvcRow,
            ft.Text(value="Нажми, чтобы услышать изменённый голос"),
            ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=lambda e: play("output_rvc.wav"))
        ]
    )

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Image",
                content=imageTab
            ),
            ft.Tab(
                text="Audio",
                content=audioTab
            ),
            ft.Tab(
                text="TTS",
                content=ttsTab
            ),
            ft.Tab(
                text="RVC",
                content=rvcTab,

            )
        ]
    )

    gerb = ft.Image(src='output1.jpg', height=100)
    gerbContainer = ft.Container(width=300, content=gerb, border=ft.border.only(right=ft.border.BorderSide(2, "black")))
    lab_text = ft.Text(value='laba luchshe vseh', text_align=ft.alignment.center)
    top_row = ft.Row(
        controls=[
            gerbContainer,
            lab_text
        ]
    )

    #page.add(top_row)

    l_column = ft.Column(
        controls=[

        ],
        width=300,
        height=800
    )

    left_column = ft.Container(
        content=l_column,
        border=ft.border.only(right=ft.border.BorderSide(2, "black"), top=ft.border.BorderSide(2, "black"))
    )

    main_column = ft.Column(
            controls=[
                ft.Text(value='Main')
            ]
        )

    m_column = ft.Container(
        height=800,
        width=800,
        content=main_column,
        border=ft.border.only(top=ft.border.BorderSide(2, "black")),
        alignment=ft.alignment.top_left
    )

    main_row = ft.Row(
        controls=[
            left_column,
            m_column
        ]
    )

    #page.add(main_row)
    page.add(rvcTab)

    def get_tab(name):
        tab = ft.Text(value="None")
        match name:
            case "SD":
                tab = imageTab
            case "ac":
                tab = audioTab
            case "tts":
                tab = ttsTab
            case "rvc":
                tab = rvcTab
        return tab

    def change_tab(cat, name):
        with open('main.json') as f:
            d = js.load(f)
            main_column.controls.clear()
            main_column.controls.append(ft.Text(value='Long'))
            main_column.controls.append(ft.Text(value=d[cat][name]["desc"], weight=ft.FontWeight.BOLD))
            main_column.controls.append(ft.Text(value='Short'))
            main_column.controls.append(ft.Text(d[cat][name]["short_desc"], weight=ft.FontWeight.BOLD))
            main_column.controls.append(get_tab(name))
            page.update()

    def js_print_name(t):
        l_column.controls.append(ft.Text(value=t))
        page.update()

    def js_print_button(i, t):
        l_column.controls.append(
            ft.Row(controls=[ft.Text(value="- "), ft.TextButton(text=t, on_click=lambda e: change_tab(i, t))]))
        page.update()

    with open('main.json') as f:
        d = js.load(f)
        for i in d:
            js_print_name(i)
            for j in d[i]:
                js_print_button(i, j)

    # page.add(tabs)
    page.on_connect=clear

# ft.app(
#     main,
#     assets_dir=""
# )