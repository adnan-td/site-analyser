# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_pagesJaoTvf.ui'
##
# Created by: Qt User Interface Compiler version 6.4.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLayout, QSizePolicy, QStackedWidget, QVBoxLayout,
                               QWidget)


class Ui_MainPages(object):
  def setupUi(self, MainPages):
    if not MainPages.objectName():
      MainPages.setObjectName(u"MainPages")
    MainPages.resize(851, 613)
    self.main_pages_layout = QVBoxLayout(MainPages)
    self.main_pages_layout.setSpacing(0)
    self.main_pages_layout.setObjectName(u"main_pages_layout")
    self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
    self.pages = QStackedWidget(MainPages)
    self.pages.setObjectName(u"pages")
    self.pages.setEnabled(True)
    self.pages.setFrameShape(QFrame.Box)
    self.home = QWidget()
    self.home.setObjectName(u"home")
    self.home.setStyleSheet(u"font-size: 16pt")
    self.page_1_layout = QVBoxLayout(self.home)
    self.page_1_layout.setSpacing(5)
    self.page_1_layout.setObjectName(u"page_1_layout")
    self.page_1_layout.setContentsMargins(5, 5, 5, 5)
    self.welcome_base = QFrame(self.home)
    self.welcome_base.setObjectName(u"welcome_base")
    self.welcome_base.setMinimumSize(QSize(300, 150))
    self.welcome_base.setMaximumSize(QSize(300, 150))
    self.welcome_base.setFrameShape(QFrame.NoFrame)
    self.welcome_base.setFrameShadow(QFrame.Raised)
    self.center_page_layout = QVBoxLayout(self.welcome_base)
    self.center_page_layout.setSpacing(10)
    self.center_page_layout.setObjectName(u"center_page_layout")
    self.center_page_layout.setContentsMargins(0, 0, 0, 0)
    self.logo = QFrame(self.welcome_base)
    self.logo.setObjectName(u"logo")
    self.logo.setMinimumSize(QSize(300, 120))
    self.logo.setMaximumSize(QSize(300, 120))
    self.logo.setFrameShape(QFrame.NoFrame)
    self.logo.setFrameShadow(QFrame.Raised)
    self.logo_layout = QVBoxLayout(self.logo)
    self.logo_layout.setSpacing(0)
    self.logo_layout.setObjectName(u"logo_layout")
    self.logo_layout.setContentsMargins(0, 0, 0, 0)

    self.center_page_layout.addWidget(self.logo)

    self.label = QLabel(self.welcome_base)
    self.label.setObjectName(u"label")
    font = QFont()
    font.setPointSize(14)
    self.label.setFont(font)
    self.label.setAlignment(Qt.AlignCenter)

    self.center_page_layout.addWidget(self.label)

    self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

    self.pages.addWidget(self.home)
    self.dns = QWidget()
    self.dns.setObjectName(u"dns")
    self.page_2_layout = QVBoxLayout(self.dns)
    self.page_2_layout.setSpacing(5)
    self.page_2_layout.setObjectName(u"page_2_layout")
    self.page_2_layout.setContentsMargins(5, 5, 5, 5)
    self.label_4 = QLabel(self.dns)
    self.label_4.setObjectName(u"label_4")
    font1 = QFont()
    font1.setPointSize(16)
    self.label_4.setFont(font1)

    self.page_2_layout.addWidget(self.label_4)

    self.dns_main_layout = QVBoxLayout()
    self.dns_main_layout.setObjectName(u"dns_main_layout")
    self.dns_top_layout = QHBoxLayout()
    self.dns_top_layout.setObjectName(u"dns_top_layout")

    self.dns_main_layout.addLayout(self.dns_top_layout)

    self.page_2_layout.addLayout(self.dns_main_layout)

    self.pages.addWidget(self.dns)
    self.loading_speed = QWidget()
    self.loading_speed.setObjectName(u"loading_speed")
    self.loading_speed.setStyleSheet(u"QFrame {\n"
                                     "	font-size: 16pt;\n"
                                     "}")
    self.page_3_layout = QVBoxLayout(self.loading_speed)
    self.page_3_layout.setObjectName(u"page_3_layout")
    self.ls_main_layout = QVBoxLayout()
    self.ls_main_layout.setObjectName(u"ls_main_layout")
    self.label_2 = QLabel(self.loading_speed)
    self.label_2.setObjectName(u"label_2")

    self.ls_main_layout.addWidget(self.label_2)

    self.ls_top_layout = QHBoxLayout()
    self.ls_top_layout.setSpacing(6)
    self.ls_top_layout.setObjectName(u"ls_top_layout")
    self.ls_top_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
    self.ls_top_layout.setContentsMargins(-1, 20, -1, 20)
    self.ls_btn_layout = QVBoxLayout()
    self.ls_btn_layout.setObjectName(u"ls_btn_layout")

    self.ls_top_layout.addLayout(self.ls_btn_layout)

    self.ls_main_layout.addLayout(self.ls_top_layout)

    self.page_3_layout.addLayout(self.ls_main_layout)

    self.pages.addWidget(self.loading_speed)
    self.internet_speed = QWidget()
    self.internet_speed.setObjectName(u"internet_speed")
    self.verticalLayout_2 = QVBoxLayout(self.internet_speed)
    self.verticalLayout_2.setObjectName(u"verticalLayout_2")
    self.st_main_layout = QVBoxLayout()
    self.st_main_layout.setObjectName(u"st_main_layout")
    self.st_top_layout = QHBoxLayout()
    self.st_top_layout.setSpacing(15)
    self.st_top_layout.setObjectName(u"st_top_layout")
    self.label_5 = QLabel(self.internet_speed)
    self.label_5.setObjectName(u"label_5")
    self.label_5.setMaximumSize(QSize(16777215, 100))
    font2 = QFont()
    font2.setPointSize(15)
    self.label_5.setFont(font2)

    self.st_top_layout.addWidget(self.label_5)

    self.st_main_layout.addLayout(self.st_top_layout)

    self.verticalLayout_2.addLayout(self.st_main_layout)

    self.pages.addWidget(self.internet_speed)
    self.response_time = QWidget()
    self.response_time.setObjectName(u"response_time")
    self.verticalLayout = QVBoxLayout(self.response_time)
    self.verticalLayout.setObjectName(u"verticalLayout")
    self.rs_main_layout = QVBoxLayout()
    self.rs_main_layout.setObjectName(u"rs_main_layout")
    self.label_3 = QLabel(self.response_time)
    self.label_3.setObjectName(u"label_3")
    self.label_3.setFont(font1)

    self.rs_main_layout.addWidget(self.label_3)

    self.rs_top_layout = QHBoxLayout()
    self.rs_top_layout.setSpacing(6)
    self.rs_top_layout.setObjectName(u"rs_top_layout")
    self.rs_top_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
    self.rs_top_layout.setContentsMargins(-1, 20, -1, 20)
    self.rs_btn_layout = QVBoxLayout()
    self.rs_btn_layout.setObjectName(u"rs_btn_layout")

    self.rs_top_layout.addLayout(self.rs_btn_layout)

    self.rs_main_layout.addLayout(self.rs_top_layout)

    self.verticalLayout.addLayout(self.rs_main_layout)

    self.pages.addWidget(self.response_time)

    self.main_pages_layout.addWidget(self.pages)

    self.retranslateUi(MainPages)

    self.pages.setCurrentIndex(1)

    QMetaObject.connectSlotsByName(MainPages)
  # setupUi

  def retranslateUi(self, MainPages):
    MainPages.setWindowTitle(
        QCoreApplication.translate("MainPages", u"Form", None))
    self.label.setText(QCoreApplication.translate(
        "MainPages", u"Welcome To WebAnalyser", None))
    self.label_4.setText(QCoreApplication.translate(
        "MainPages", u"Analyse Site DNS information", None))
    self.label_2.setText(QCoreApplication.translate(
        "MainPages", u"Analyse Site Loading Speed", None))
    self.label_5.setText(QCoreApplication.translate(
        "MainPages", u"Network Speed Test", None))
    self.label_3.setText(QCoreApplication.translate(
        "MainPages", u"Analyse Site Response Time", None))
  # retranslateUi
