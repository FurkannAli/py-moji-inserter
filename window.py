# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(420, 520)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Emo = QPushButton(Form)
        self.pushButton_Emo.setObjectName(u"pushButton_Emo")

        self.horizontalLayout.addWidget(self.pushButton_Emo)

        self.pushButton_Kao = QPushButton(Form)
        self.pushButton_Kao.setObjectName(u"pushButton_Kao")

        self.horizontalLayout.addWidget(self.pushButton_Kao)

        self.pushButton_Sym = QPushButton(Form)
        self.pushButton_Sym.setObjectName(u"pushButton_Sym")

        self.horizontalLayout.addWidget(self.pushButton_Sym)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        font = QFont()
        font.setPointSize(14)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 398, 440))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.verticalLayout_5.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_Emo.setText(QCoreApplication.translate("Form", u"Emoji", None))
        self.pushButton_Kao.setText(QCoreApplication.translate("Form", u"Kaomoji", None))
        self.pushButton_Sym.setText(QCoreApplication.translate("Form", u"Symbol", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Search...", None))
    # retranslateUi

