# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popupDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFrame,
    QGridLayout,
    QLabel,
    QSizePolicy,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(292, 144)
        Dialog.setMinimumSize(QSize(292, 144))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName("frame")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(274, 60))

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("Dialog", "TextLabel", None))

    # retranslateUi
