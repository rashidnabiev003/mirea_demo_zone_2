import os
import sys
import pyaudio
import wavio as wv
import wave
from ui_app import Ui_MainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QUrl, Slot, QFile, QIODevice
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QLabel,
                               QMainWindow, QPushButton, QTabWidget, QWidget, QVBoxLayout,
                               QLineEdit)
from PySide6.QtMultimedia import (QCamera, QImageCapture,
                                  QCameraDevice, QMediaCaptureSession,
                                  QMediaDevices, QMediaFormat, QMediaRecorder, QMediaPlayer, QAudioOutput, QAudioInput)

from image_generator import generate_image_api
from speech_recognition_module import speech_to_text
#from audio_generator import generate_audio


GENERATED_IMAGE = './test.jpg'
GENERATED_AUDIO = 'test'
AUDIO_RECORDER = "recorder.mp3"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.tab_2.setLayout(self.verticalLayout)
        self.setCentralWidget(self.tabWidget)

        self.session = QMediaCaptureSession()
        self.audioInput = QAudioInput()
        self.session.setAudioInput(self.audioInput)
        self.recorder = QMediaRecorder()
        self.session.setRecorder(self.recorder)
        self.recorder.setMediaFormat(QMediaFormat.MP3)
        self.recorder.setQuality(QMediaRecorder.Quality.HighQuality)
        self.recorder.setOutputLocation(QUrl.fromLocalFile("test.mp3"))


        #button logic
        self.img_button.clicked.connect(self._picture_generation_func)
        self.extract_text_button.clicked.connect(self._text_exctractor)
        self.start_recording_button.clicked.connect(self._start_recording)
        self.stop_recording_button.clicked.connect(self._stop_recording)

    @Slot()
    def _picture_generation_func(self):
        self.img_button.setEnabled(False)
        prompt_text = str(self.text_image_label.text())
        file_name = generate_image_api(prompt_text, GENERATED_IMAGE)
        self.image_label.setPixmap(QPixmap(file_name))
        self.text_image_label.setText("")
        self.img_button.setEnabled(True)

    @Slot()
    def _text_exctractor(self):
        self.extract_text_button.setEnabled(False)
        self.audio_text_line.setText(speech_to_text(AUDIO_RECORDER))
        self.extract_text_button.setEnabled(True)

    @Slot()
    def _start_recording(self):
        self.recorder.record()

    @Slot()
    def _stop_recording(self):
        self.recorder.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
