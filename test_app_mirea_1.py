import cv2
import os
import sys
from PySide6.QtCore import QDate, QDir, QStandardPaths, Qt, QUrl, Slot, QSize
from PySide6.QtGui import QAction, QGuiApplication, QDesktopServices, QIcon
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QTabWidget, QToolBar, QVBoxLayout, QWidget, QVBoxLayout,
                               QLineEdit, QStyle, QFileDialog, QSlider)
from PySide6.QtMultimedia import (QCamera, QImageCapture,
                                  QCameraDevice, QMediaCaptureSession,
                                  QMediaDevices, QMediaFormat, QMediaRecorder, QMediaPlayer, QAudioOutput, QAudioInput)
from PySide6.QtMultimediaWidgets import QVideoWidget
from image_generator import generator


FILE_NAME = 'C:/Users/HP/Pictures/test.jpg'
GENERATED_AUDIO = 'C:/Users/HP/Pictures/test.wav'
AUDIO_RECORDER = 'C:/Users/HP/Pictures/recorder'


def available_cameras():
    available_camera = QMediaDevices.videoInputs()  # проверка наличия камер, возвращает список названий всех доступных камер
    return available_camera[0]


class AudioPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1000, 600)
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.audio_input = QAudioInput()
        self.generate_button = QPushButton("Generate Audio")
        self.start_recording_button = QPushButton("Start Recording")
        self.stop_recording_button = QPushButton("Stop Recording")
        self.stop_recording_button.setEnabled(False)

        self.session = QMediaCaptureSession()
        self.session.setAudioInput(self.audio_input)
        self.recorder = QMediaRecorder()
        self.session.setRecorder(self.recorder)
        self.recorder.setQuality(QMediaRecorder.Quality.HighQuality)
        self.recorder.setMediaFormat(QMediaFormat.MP3)
        self.recorder.setAudioChannelCount(1)
        self.recorder.setAudioSampleRate(-1)
        self.recorder.setOutputLocation(QUrl.fromLocalFile(AUDIO_RECORDER))
        self.media_player.setAudioOutput(self.audio_output)

        # ---------------------------------------- button logic---------------------------
        self.generate_button.clicked.connect(self._generate_button)
        self.start_recording_button.clicked.connect(self._start_recording)
        self.stop_recording_button.clicked.connect(self._stop_recording)
        # ---------------------------------------- button logic---------------------------

        # ---------------------------------------- layouts---------------------------
        layout = QVBoxLayout()
        layout.addWidget(self.generate_button)
        layout.addWidget(self.start_recording_button)
        layout.addWidget(self.stop_recording_button)
        self.setLayout(layout)

    @Slot()
    def _generate_button(self):
        self.media_player.setSource(QUrl.fromLocalFile(GENERATED_AUDIO))
        self.media_player.play()

    @Slot()
    def _start_recording(self):
        self.recorder.record()
        self.stop_recording_button.setEnabled(True)

    @Slot()
    def _stop_recording(self):
        self.recorder.stop()
        self.stop_recording_button.setEnabled(False)


class MediaPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 1000, 600)
        self.mediaplayer = QMediaPlayer()
        self.audio = QAudioOutput()

        videowidget = QVideoWidget()

        # btn for opening
        openBtn = QPushButton("Open Video")
        openBtn.clicked.connect(self.open_video)

        # btn for palying
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        # slider
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        hbox = QHBoxLayout()

        hbox.addWidget(openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        vbox = QVBoxLayout()

        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.mediaplayer.setVideoOutput(videowidget)
        self.mediaplayer.setAudioOutput(self.audio)

        # media player signals
        self.mediaplayer.mediaStatusChanged.connect(self.mediastate_changed)
        self.mediaplayer.positionChanged.connect(self.position_changed)
        self.mediaplayer.durationChanged.connect(self.duration_changed)

    def open_video(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaplayer.setSource(QUrl.fromLocalFile(filename))
            self.playBtn.setEnabled(True)

    def play_video(self):
        if self.mediaplayer.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaplayer.pause()

        else:
            self.mediaplayer.play()

    def mediastate_changed(self):
        if self.mediaplayer.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
            )

        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
            )

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaplayer.setPosition(position)


class ImageGENWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()
        self._gen_picture_widget = QLabel()
        self._reference_text_widget = QLineEdit()
        self._confirm_button = QPushButton("Confirm")

        self._gen_picture_widget.setFixedSize(1000, 510)
        self._gen_picture_widget.setScaledContents(True)
        self._reference_text_widget.setFixedSize(500, 50)
        self._confirm_button.setFixedSize(200, 50)

        self._confirm_button.clicked.connect(self.picture_generation_func)

        layout = QHBoxLayout()
        layout.addWidget(self._reference_text_widget)
        layout.addWidget(self._confirm_button)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self._gen_picture_widget)
        main_layout.addLayout(layout)
        self.setLayout(main_layout)

    def picture_generation_func(self):
        self._confirm_button.setEnabled(False)
        prompt_text = str(self._reference_text_widget.text())
        file_name = generator(prompt_text)
        self._gen_picture_widget.setPixmap(QPixmap(file_name))
        self._reference_text_widget.setText("")
        self._confirm_button.setEnabled(True)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._capture_session = None
        self._camera = None
        self._camera_info = None
        self._image_capture = None

        self._tab_widget = QTabWidget()
        self.setCentralWidget(self._tab_widget)
        self.setWindowTitle('TEST APP MIREA')
        self.setGeometry(200, 200, 1000, 600)

        self._audio_generation = AudioPlayer()
        self._video_player = MediaPlayer()
        self._picture_gen = ImageGENWindow()
        self._video_widget = QVideoWidget()
        self._picture_widget = QLabel()
        self._button_widget = QWidget()
        self._main_widget = QWidget()

        self._video_widget.setFixedSize(700, 550)
        self._picture_widget.setFixedSize(300, 300)

        # ---------------------------------------- camera initialization---------------------------
        self._camera_info = available_cameras()
        self._camera = QCamera(self._camera_info)
        self._image_capture = QImageCapture(self._camera)
        self._capture_session = QMediaCaptureSession()  # штука без которой съемка не работает
        self._capture_session.setCamera(self._camera)  # выбираем какой камерой начинаем съемку
        self._capture_session.setVideoOutput(self._video_widget)  # направляет видеопоток с камеры на виджет(окно)
        self._capture_session.setImageCapture(self._image_capture)
        self._current_preview = QImage()
        self._camera.start()  # собственно включение камеры

        # ---------------------------------------- camera initialization---------------------------

        # ---------------------------------------- button initialization---------------------------
        self.start_filming_button = QPushButton("Start shooting")
        self.stop_filming_button = QPushButton("Stop shooting")
        self.stop_filming_button.setEnabled(False)
        self.take_picture_button = QPushButton("Take picture")
        # ---------------------------------------- button initialization---------------------------

        # ---------------------------------------- button logic---------------------------
        self.start_filming_button.clicked.connect(self.start_filming)
        self.stop_filming_button.clicked.connect(self.stop_filming)
        self.take_picture_button.clicked.connect(self.take_picture)
        # ---------------------------------------- button logic---------------------------

        # ---------------------------------------- video ---------------------------
        self.recorder = QMediaRecorder(self._camera)
        self._capture_session.setRecorder(self.recorder)
        settings = QMediaFormat(QMediaFormat.MPEG4)
        self.recorder.setMediaFormat(settings)
        # ---------------------------------------- video---------------------------

        # ---------------------------------------- layouts---------------------------
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.start_filming_button)
        button_layout.addWidget(self.stop_filming_button)
        button_layout.addWidget(self.take_picture_button)
        button_layout.addStretch()
        r_layout = QVBoxLayout()
        r_layout.addWidget(self._picture_widget)
        r_layout.addLayout(button_layout)
        main_layout = QHBoxLayout()
        main_layout.addWidget(self._video_widget)
        main_layout.addLayout(r_layout)
        self._main_widget.setLayout(main_layout)

        self._tab_widget.addTab(self._main_widget, "Video-Picture")
        self._tab_widget.addTab(self._picture_gen, "Picture-Generation")
        self._tab_widget.addTab(self._video_player, "Video Player")
        self._tab_widget.addTab(self._audio_generation, "Audio Generation")

    @Slot()
    def start_filming(self) -> None:
        self.stop_filming_button.setEnabled(True)
        self.recorder.record()
        print("Filming start")

    @Slot()
    def stop_filming(self) -> None:
        self.recorder.stop()
        self.stop_filming_button.setEnabled(False)
        print("Filming end")

    @Slot()
    def take_picture(self) -> None:
        self._current_preview = QImage()
        self._image_capture.captureToFile(FILE_NAME)
        self._picture_widget.setScaledContents(True)
        self._picture_widget.setPixmap(QPixmap(FILE_NAME))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
