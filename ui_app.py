# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appUCUuOe.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 520)
        MainWindow.setMinimumSize(QSize(600, 520))
        MainWindow.setMaximumSize(QSize(600, 520))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 520))
        self.centralwidget.setMaximumSize(QSize(600, 520))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 600, 520))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane\n"
"{\n"
"border: 1px;\n"
"background: rgb(148, 148, 148);\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"background:rgb(76, 81, 93);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"background: rgb(35, 40, 49);\n"
"}\n"
"QTabBar::tab:hover\n"
"{\n"
"background: rgb (56, 40, 49);\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"background: rgb(35, 40, 49);")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 596, 478))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.image_label = QLabel(self.widget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMinimumSize(QSize(500, 380))
        self.image_label.setMaximumSize(QSize(500, 380))
        self.image_label.setStyleSheet(u"border: 1px solid;\n"
"border-color:rgb(130, 130, 130);\n"
"background-color: rgb(34, 34, 34);\n"
"")

        self.verticalLayout_2.addWidget(self.image_label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.text_image_label = QLineEdit(self.widget)
        self.text_image_label.setObjectName(u"text_image_label")
        self.text_image_label.setMinimumSize(QSize(200, 40))
        self.text_image_label.setMaximumSize(QSize(200, 40))
        self.text_image_label.setStyleSheet(u"QLineEdit\n"
"{\n"
"color: white;\n"
"border: 1px solid;\n"
"background-color: rgb(34, 34, 34);\n"
"border-color:rgb(130, 130, 130);\n"
"}")

        self.horizontalLayout_3.addWidget(self.text_image_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.img_button = QPushButton(self.widget)
        self.img_button.setObjectName(u"img_button")
        self.img_button.setMinimumSize(QSize(150, 40))
        self.img_button.setMaximumSize(QSize(150, 40))
        self.img_button.setStyleSheet(u"border: 1px solid;\n"
"color: rgb(255, 255, 255);\n"
"border-color:rgb(130, 130, 130);\n"
"\n"
"QPushButton::button:pressed\n"
"{\n"
"	background-color: rgb(22, 150, 37);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.img_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"background: rgb(35, 40, 49);")
        self.widget1 = QWidget(self.tab_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 594, 518))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 108, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamilies([u"PMingLiU-ExtB"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet(u"color:white;\n"
"border: 1px solid;\n"
"border-color:rgb(130, 130, 130);\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setMargin(0)

        self.verticalLayout_5.addWidget(self.label_3)

        self.audio_text_line = QLineEdit(self.widget1)
        self.audio_text_line.setObjectName(u"audio_text_line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audio_text_line.sizePolicy().hasHeightForWidth())
        self.audio_text_line.setSizePolicy(sizePolicy)
        self.audio_text_line.setMinimumSize(QSize(300, 150))
        self.audio_text_line.setStyleSheet(u"border: 1px solid;\n"
"color: rgb(255, 255, 255);\n"
"border-color:rgb(130, 130, 130);\n"
"")
        self.audio_text_line.setFrame(True)
        self.audio_text_line.setCursorPosition(0)
        self.audio_text_line.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.audio_text_line.setDragEnabled(True)

        self.verticalLayout_5.addWidget(self.audio_text_line)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.start_recording_button = QPushButton(self.widget1)
        self.start_recording_button.setObjectName(u"start_recording_button")
        self.start_recording_button.setMinimumSize(QSize(150, 40))
        self.start_recording_button.setStyleSheet(u"border: 1px solid;\n"
"color: rgb(255, 255, 255);\n"
"border-color:rgb(130, 130, 130);\n"
"")

        self.verticalLayout_4.addWidget(self.start_recording_button)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.stop_recording_button = QPushButton(self.widget1)
        self.stop_recording_button.setObjectName(u"stop_recording_button")
        self.stop_recording_button.setMinimumSize(QSize(150, 40))
        self.stop_recording_button.setStyleSheet(u"border: 1px solid;\n"
"color: rgb(255, 255, 255);\n"
"border-color:rgb(130, 130, 130);\n"
"")

        self.verticalLayout_4.addWidget(self.stop_recording_button)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.extract_text_button = QPushButton(self.widget1)
        self.extract_text_button.setObjectName(u"extract_text_button")
        self.extract_text_button.setMinimumSize(QSize(150, 40))
        self.extract_text_button.setStyleSheet(u"border: 1px solid;\n"
"color: rgb(255, 255, 255);\n"
"border-color:rgb(130, 130, 130);\n"
"")

        self.verticalLayout_4.addWidget(self.extract_text_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 178, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image_label.setText("")
        self.text_image_label.setText("")
        self.img_button.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434-\u0432\u044b\u0432\u043e\u0434 \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.audio_text_line.setText("")
        self.start_recording_button.setText(QCoreApplication.translate("MainWindow", u"Start recording", None))
        self.stop_recording_button.setText(QCoreApplication.translate("MainWindow", u"Stop recording", None))
        self.extract_text_button.setText(QCoreApplication.translate("MainWindow", u"Extract text from audio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

