from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import (QAbstractSpinBox, QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy,
                               QSlider, QSpinBox, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(542, 418)
        MainWindow.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/app-icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
                                 "    background-color: #121212;\n"
                                 "    color: white;\n"
                                 "    font-family: Verdana;\n"
                                 "    font-size: 16pt;\n"
                                 "    margin: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    border: 2px solid gray;\n"
                                 "    border-radius: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#btn_lower,\n"
                                 "#btn_upper,\n"
                                 "#btn_digits,\n"
                                 "#btn_special {\n"
                                 "    padding: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    border-color: #090;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    border: 4px solid #090;\n"
                                 "    border-radius: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:checked {\n"
                                 "    background-color: #006300;\n"
                                 "    border-color: #090;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.icon_lock = QPushButton(self.centralwidget)
        self.icon_lock.setObjectName(u"icon_lock")
        self.icon_lock.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_lock.sizePolicy().hasHeightForWidth())
        self.icon_lock.setSizePolicy(sizePolicy)
        self.icon_lock.setStyleSheet(u"border: none;\n"
                                     "")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_lock.setIcon(icon1)
        self.icon_lock.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.icon_lock)

        self.layout_password = QHBoxLayout()
        self.layout_password.setObjectName(u"layout_password")
        self.frame_password = QFrame(self.centralwidget)
        self.frame_password.setObjectName(u"frame_password")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_password.sizePolicy().hasHeightForWidth())
        self.frame_password.setSizePolicy(sizePolicy1)
        self.frame_password.setStyleSheet(u"QFrame {\n"
                                          "    border: 2px solid gray;\n"
                                          "    border-radius: 5px;\n"
                                          "    margin-right: 0;\n"
                                          "}\n"
                                          "\n"
                                          "QFrame:hover {\n"
                                          "    border-color: #090;\n"
                                          "}\n"
                                          "")
        self.frame_password.setFrameShape(QFrame.StyledPanel)
        self.frame_password.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_password)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.line_password = QLineEdit(self.frame_password)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setStyleSheet(u"QLineEdit {\n"
                                         "    border: none;\n"
                                         "    margin: 0;\n"
                                         "    font-size: 20pt;\n"
                                         "}\n"
                                         "")

        self.horizontalLayout_10.addWidget(self.line_password)

        self.btn_visibility = QPushButton(self.frame_password)
        self.btn_visibility.setObjectName(u"btn_visibility")
        self.btn_visibility.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visibility.setStyleSheet(u"QPushButton {\n"
                                          "    border: none;\n"
                                          "    margin: 0;\n"
                                          "    background-color: transparent;\n"
                                          "}\n"
                                          "")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/invisible.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icons/visible.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_visibility.setIcon(icon2)
        self.btn_visibility.setIconSize(QSize(30, 30))
        self.btn_visibility.setCheckable(True)
        self.btn_visibility.setChecked(True)

        self.horizontalLayout_10.addWidget(self.btn_visibility)

        self.layout_password.addWidget(self.frame_password)

        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton {\n"
                                       "    margin-right: 0;\n"
                                       "    margin-left: 0;\n"
                                       "}\n"
                                       "")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/refresh.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_refresh.setIcon(icon3)
        self.btn_refresh.setIconSize(QSize(52, 52))

        self.layout_password.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copy.setStyleSheet(u"QPushButton {\n"
                                    "    padding: 5px;\n"
                                    "    margin-left: 0;\n"
                                    "}\n"
                                    "")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/copy.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_copy.setIcon(icon4)
        self.btn_copy.setIconSize(QSize(42, 42))

        self.layout_password.addWidget(self.btn_copy)

        self.verticalLayout.addLayout(self.layout_password)

        self.layout_info = QHBoxLayout()
        self.layout_info.setObjectName(u"layout_info")
        self.label_strength = QLabel(self.centralwidget)
        self.label_strength.setObjectName(u"label_strength")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_strength.sizePolicy().hasHeightForWidth())
        self.label_strength.setSizePolicy(sizePolicy2)
        self.label_strength.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.label_strength)

        self.label_entropy = QLabel(self.centralwidget)
        self.label_entropy.setObjectName(u"label_entropy")
        sizePolicy2.setHeightForWidth(self.label_entropy.sizePolicy().hasHeightForWidth())
        self.label_entropy.setSizePolicy(sizePolicy2)
        self.label_entropy.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.label_entropy)

        self.verticalLayout.addLayout(self.layout_info)

        self.layout_length = QHBoxLayout()
        self.layout_length.setObjectName(u"layout_length")
        self.slider_length = QSlider(self.centralwidget)
        self.slider_length.setObjectName(u"slider_length")
        self.slider_length.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_length.setStyleSheet(u"QSlider::groove:horizontal {\n"
                                         "    background-color: transparent;\n"
                                         "    height: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "QSlider::sub-page:horizontal {\n"
                                         "    background-color: #090;\n"
                                         "}\n"
                                         "\n"
                                         "QSlider::add-page:horizontal {\n"
                                         "    background-color: gray;\n"
                                         "}\n"
                                         "\n"
                                         "QSlider::handle:horizontal {\n"
                                         "    background-color: white;\n"
                                         "    width: 22px;\n"
                                         "    border-radius: 10px;\n"
                                         "    margin-top: -8px;\n"
                                         "    margin-bottom: -8px;\n"
                                         "}\n"
                                         "")
        self.slider_length.setMaximum(100)
        self.slider_length.setValue(12)
        self.slider_length.setOrientation(Qt.Horizontal)

        self.layout_length.addWidget(self.slider_length)

        self.spinbox_length = QSpinBox(self.centralwidget)
        self.spinbox_length.setObjectName(u"spinbox_length")
        self.spinbox_length.setStyleSheet(u"QSpinBox {\n"
                                          "    border: 2px solid gray;\n"
                                          "    border-radius: 5px;\n"
                                          "    background: transparent;\n"
                                          "    padding: 2px;\n"
                                          "}\n"
                                          "\n"
                                          "QSpinBox:hover {\n"
                                          "    border-color: #009900;\n"
                                          "}\n"
                                          "")
        self.spinbox_length.setAlignment(Qt.AlignCenter)
        self.spinbox_length.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinbox_length.setMaximum(100)
        self.spinbox_length.setValue(12)

        self.layout_length.addWidget(self.spinbox_length)

        self.verticalLayout.addLayout(self.layout_length)

        self.layout_characters = QHBoxLayout()
        self.layout_characters.setObjectName(u"layout_characters")
        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_characters.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_characters.addWidget(self.btn_upper)

        self.btn_digits = QPushButton(self.centralwidget)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_digits.setCheckable(True)
        self.btn_digits.setChecked(True)

        self.layout_characters.addWidget(self.btn_digits)

        self.btn_special = QPushButton(self.centralwidget)
        self.btn_special.setObjectName(u"btn_special")
        self.btn_special.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_special.setCheckable(True)

        self.layout_characters.addWidget(self.btn_special)

        self.verticalLayout.addLayout(self.layout_characters)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.icon_lock.setText("")
        self.btn_visibility.setText("")
        self.btn_refresh.setText("")
        self.btn_refresh.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
        self.btn_copy.setText("")
        self.btn_copy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
        self.label_strength.setText("")
        self.label_entropy.setText("")
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_special.setText(QCoreApplication.translate("MainWindow", u"#$%", None))
