# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_pagesAbfqaM.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class UI_Pages(object):
    def setupUi(self, pages):
        if not pages.objectName():
            pages.setObjectName(u"pages")
        pages.resize(960, 680)
        pages.setMinimumSize(QSize(960, 680))
        font = QFont()
        pages.setFont(font)
        pages.setStyleSheet(u"font-family: Montserrat; font-size: 16px; color: white;\n"
"")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout = QVBoxLayout(self.home_page)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, -1, -1)
        self.frame_notifications = QFrame(self.home_page)
        self.frame_notifications.setObjectName(u"frame_notifications")
        self.frame_notifications.setMinimumSize(QSize(940, 64))
        self.frame_notifications.setMaximumSize(QSize(940, 64))
        self.frame_notifications.setStyleSheet(u"background-color: #C4C4C4; border-radius: 12px; color: black;")
        self.frame_notifications.setFrameShape(QFrame.StyledPanel)
        self.frame_notifications.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_notifications)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_notifications = QLabel(self.frame_notifications)
        self.label_notifications.setObjectName(u"label_notifications")
        self.label_notifications.setMinimumSize(QSize(940, 0))
        self.label_notifications.setMaximumSize(QSize(16777215, 16777215))
        self.label_notifications.setLayoutDirection(Qt.LeftToRight)
        self.label_notifications.setAutoFillBackground(False)
        self.label_notifications.setStyleSheet(u"")
        self.label_notifications.setFrameShape(QFrame.NoFrame)
        self.label_notifications.setFrameShadow(QFrame.Plain)
        self.label_notifications.setScaledContents(False)
        self.label_notifications.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_notifications.setWordWrap(True)
        self.label_notifications.setMargin(4)
        self.label_notifications.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.label_notifications, 0, 0, 1, 1)

        self.btn_close_notification = QPushButton(self.frame_notifications)
        self.btn_close_notification.setObjectName(u"btn_close_notification")
        self.btn_close_notification.setMinimumSize(QSize(24, 24))
        self.btn_close_notification.setMaximumSize(QSize(24, 24))
        self.btn_close_notification.setStyleSheet(u"QPushButton {\n"
"	\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: white;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./view/UI/images/icons/close_64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close_notification.setIcon(icon)

        self.gridLayout.addWidget(self.btn_close_notification, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_notifications, 0, Qt.AlignHCenter)

        self.frame_content_home = QFrame(self.home_page)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFont(font)
        self.frame_content_home.setStyleSheet(u"border-radius: 12px;")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_content_home)
        self.horizontalLayout.setSpacing(64)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 32, 12, 9)
        self.frame_info_user = QFrame(self.frame_content_home)
        self.frame_info_user.setObjectName(u"frame_info_user")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_info_user.sizePolicy().hasHeightForWidth())
        self.frame_info_user.setSizePolicy(sizePolicy)
        self.frame_info_user.setMaximumSize(QSize(256, 256))
        self.frame_info_user.setFrameShape(QFrame.StyledPanel)
        self.frame_info_user.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info_user)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(8, 8, 0, 0)
        self.label_info_user = QLabel(self.frame_info_user)
        self.label_info_user.setObjectName(u"label_info_user")
        self.label_info_user.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_5.addWidget(self.label_info_user)

        self.label_sigss = QLabel(self.frame_info_user)
        self.label_sigss.setObjectName(u"label_sigss")
        self.label_sigss.setStyleSheet(u"padding-top: 16px")

        self.verticalLayout_5.addWidget(self.label_sigss)

        self.label_user_sigss = QLabel(self.frame_info_user)
        self.label_user_sigss.setObjectName(u"label_user_sigss")

        self.verticalLayout_5.addWidget(self.label_user_sigss)

        self.label_whatsapp = QLabel(self.frame_info_user)
        self.label_whatsapp.setObjectName(u"label_whatsapp")
        self.label_whatsapp.setStyleSheet(u"padding-top: 16px;")

        self.verticalLayout_5.addWidget(self.label_whatsapp)

        self.label_user_whatsapp = QLabel(self.frame_info_user)
        self.label_user_whatsapp.setObjectName(u"label_user_whatsapp")

        self.verticalLayout_5.addWidget(self.label_user_whatsapp)


        self.horizontalLayout.addWidget(self.frame_info_user, 0, Qt.AlignTop)

        self.frame_main_buttons = QFrame(self.frame_content_home)
        self.frame_main_buttons.setObjectName(u"frame_main_buttons")
        self.frame_main_buttons.setMaximumSize(QSize(340, 16777215))
        self.frame_main_buttons.setStyleSheet(u"QPushButton {\n"
"	background-color: #005012;\n"
"	border-radius: 8px;\n"
"	color: white;\n"
"	padding: 12px;\n"
"	width: 256px\n"
"}\n"
"\n"
"#btn_start {\n"
"	background-color: #339047;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#btn_start:hover {\n"
"	background-color: #005500;\n"
"}\n"
"\n"
"#btn_start:pressed {\n"
"	background-color: #005012;\n"
"}\n"
"#btn_start:disabled {\n"
"	background-color: #656568;\n"
"}\n"

"QPushButton:disabled {\n"
"	background: #656568;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: #019421;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #54cb62;\n"
"}")
        self.frame_main_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_main_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_main_buttons)
        self.verticalLayout_3.setSpacing(48)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_start = QPushButton(self.frame_main_buttons)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(256, 0))
        self.btn_start.setMaximumSize(QSize(256, 16777215))
        self.btn_start.setStyleSheet(u"padding: 16px;")

        self.verticalLayout_3.addWidget(self.btn_start, 0, Qt.AlignHCenter)

        self.btn_update_reg = QPushButton(self.frame_main_buttons)
        self.btn_update_reg.setObjectName(u"btn_update_reg")

        self.verticalLayout_3.addWidget(self.btn_update_reg)

        self.btn_verify_contacts = QPushButton(self.frame_main_buttons)
        self.btn_verify_contacts.setObjectName(u"btn_verify_contacts")

        self.verticalLayout_3.addWidget(self.btn_verify_contacts)

        self.btn_send_messages = QPushButton(self.frame_main_buttons)
        self.btn_send_messages.setObjectName(u"btn_send_messages")

        self.verticalLayout_3.addWidget(self.btn_send_messages)

        self.btn_generate_reports = QPushButton(self.frame_main_buttons)
        self.btn_generate_reports.setObjectName(u"btn_generate_reports")

        self.verticalLayout_3.addWidget(self.btn_generate_reports)


        self.horizontalLayout.addWidget(self.frame_main_buttons)

        self.frame_tools = QFrame(self.frame_content_home)
        self.frame_tools.setObjectName(u"frame_tools")
        self.frame_tools.setMinimumSize(QSize(0, 0))
        self.frame_tools.setMaximumSize(QSize(256, 16777215))
        self.frame_tools.setLayoutDirection(Qt.LeftToRight)
        self.frame_tools.setStyleSheet(u"QPushButton {\n"
"background: #00B4A9;\n"
"padding: 12px;\n"
"border-radius: 12px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #75E3DD\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #93e2e3\n"
"}")
        self.frame_tools.setFrameShape(QFrame.StyledPanel)
        self.frame_tools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_tools)
        self.verticalLayout_4.setSpacing(48)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_view_reg = QPushButton(self.frame_tools)
        self.btn_view_reg.setObjectName(u"btn_view_reg")
        self.btn_view_reg.setMinimumSize(QSize(256, 48))
        self.btn_view_reg.setMaximumSize(QSize(16777215, 48))
        self.btn_view_reg.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_view_reg, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.btn_change_reg = QPushButton(self.frame_tools)
        self.btn_change_reg.setObjectName(u"btn_change_reg")
        self.btn_change_reg.setMinimumSize(QSize(256, 48))
        self.btn_change_reg.setMaximumSize(QSize(16777215, 48))
        self.btn_change_reg.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_change_reg, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_tools, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_content_home, 0, Qt.AlignVCenter)

        self.frame_footer = QFrame(self.home_page)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_footer)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_log = QFrame(self.frame_footer)
        self.frame_log.setObjectName(u"frame_log")
        self.frame_log.setMaximumSize(QSize(940, 64))
        self.frame_log.setFrameShape(QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_log)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_log = QLabel(self.frame_log)
        self.label_log.setObjectName(u"label_log")
        self.label_log.setMinimumSize(QSize(940, 64))
        self.label_log.setMaximumSize(QSize(940, 64))
        self.label_log.setStyleSheet(u"background-color: #F2D68E; color: black; padding: 8px; border-radius: 12px;")
        self.label_log.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_log.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_log, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_log)

        self.progressBar = QProgressBar(self.frame_footer)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setMinimumSize(QSize(0, 12))
        self.progressBar.setMaximumSize(QSize(16777215, 12))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"        border: none;  \n"
"        text-align: center;\n"
"        background: white;\n"
"        border-radius:6px;\n"
"} \n"
"\n"
"QProgressBar::chunk {\n"
"        background: lime; \n"
"        border-radius:6px;\n"
"} ")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_12.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame_footer, 0, Qt.AlignHCenter|Qt.AlignBottom)

        pages.addWidget(self.home_page)
        self.qr_code = QWidget()
        self.qr_code.setObjectName(u"qr_code")
        self.horizontalLayout_2 = QHBoxLayout(self.qr_code)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_content_qr_code = QFrame(self.qr_code)
        self.frame_content_qr_code.setObjectName(u"frame_content_qr_code")
        self.frame_content_qr_code.setMinimumSize(QSize(720, 540))
        self.frame_content_qr_code.setMaximumSize(QSize(720, 540))
        self.frame_content_qr_code.setStyleSheet(u"")
        self.frame_content_qr_code.setFrameShape(QFrame.StyledPanel)
        self.frame_content_qr_code.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_content_qr_code)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_content_qr_code)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_img_qr_code = QFrame(self.frame_2)
        self.frame_img_qr_code.setObjectName(u"frame_img_qr_code")
        sizePolicy.setHeightForWidth(self.frame_img_qr_code.sizePolicy().hasHeightForWidth())
        self.frame_img_qr_code.setSizePolicy(sizePolicy)
        self.frame_img_qr_code.setMinimumSize(QSize(340, 340))
        self.frame_img_qr_code.setMaximumSize(QSize(340, 340))
        self.frame_img_qr_code.setStyleSheet(u"background: white; border-radius: 12px;")
        self.frame_img_qr_code.setFrameShape(QFrame.NoFrame)
        self.frame_img_qr_code.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_img_qr_code)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, 9, -1, -1)
        self.label_img_qr_code = QLabel(self.frame_img_qr_code)
        self.label_img_qr_code.setObjectName(u"label_img_qr_code")
        self.label_img_qr_code.setMinimumSize(QSize(300, 300))
        self.label_img_qr_code.setMaximumSize(QSize(300, 300))
        self.label_img_qr_code.setStyleSheet(u"background: #c1c1c1; color: b;")
        self.label_img_qr_code.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_img_qr_code)


        self.horizontalLayout_7.addWidget(self.frame_img_qr_code)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_label_and_buttons = QFrame(self.frame_content_qr_code)
        self.frame_label_and_buttons.setObjectName(u"frame_label_and_buttons")
        self.frame_label_and_buttons.setMinimumSize(QSize(720, 0))
        self.frame_label_and_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_label_and_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_label_and_buttons)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.timer = QProgressBar(self.frame_label_and_buttons)
        self.timer.setObjectName(u"timer")
        self.timer.setMinimumSize(QSize(0, 12))
        self.timer.setMaximumSize(QSize(16777215, 12))
        self.timer.setStyleSheet(u"QProgressBar{\n"
"        border: none;  \n"
"        text-align: center;\n"
"		 color: b;\n"
"		 font-size: 12px;\n"
"        background: white;\n"
"        border-radius:6px;\n"
"} \n"
"\n"
"QProgressBar::chunk {\n"
"        background: lime; \n"
"        border-radius:6px;\n"
"} ")
        self.timer.setMinimum(0)
        self.timer.setMaximum(100)
        self.timer.setValue(24)
        self.timer.setInvertedAppearance(False)

        self.verticalLayout_13.addWidget(self.timer)

        self.label_info = QLabel(self.frame_label_and_buttons)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setAlignment(Qt.AlignCenter)
        self.label_info.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_info)

        self.splitter = QSplitter(self.frame_label_and_buttons)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setMinimumSize(QSize(0, 0))
        self.splitter.setMaximumSize(QSize(536, 44))
        self.splitter.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 12px;\n"
"	border-radius: 12px;\n"
"	background: #A50000;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background: #DB1F1F\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #fe5243;\n"
"}")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(24)
        self.splitter.setChildrenCollapsible(True)
        self.btn_again = QPushButton(self.splitter)
        self.btn_again.setObjectName(u"btn_again")
        self.btn_again.setMinimumSize(QSize(256, 44))
        self.btn_again.setMaximumSize(QSize(256, 44))
        self.btn_again.setStyleSheet(u"QPushButton {\n"
"	background-color: #005012;\n"
"	border-radius: 8px;\n"
"	color: white;\n"
"	padding: 12px;\n"
"	width: 256px\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background: #656568;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: #019421;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #54cb62;\n"
"}")
        self.splitter.addWidget(self.btn_again)
        self.btn_cancel = QPushButton(self.splitter)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(256, 44))
        self.btn_cancel.setMaximumSize(QSize(256, 44))
        self.splitter.addWidget(self.btn_cancel)

        self.verticalLayout_13.addWidget(self.splitter, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_label_and_buttons)


        self.horizontalLayout_2.addWidget(self.frame_content_qr_code)

        pages.addWidget(self.qr_code)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        sizePolicy.setHeightForWidth(self.settings_page.sizePolicy().hasHeightForWidth())
        self.settings_page.setSizePolicy(sizePolicy)
        self.settings_page.setMinimumSize(QSize(0, 0))
        self.settings_page.setMaximumSize(QSize(16777215, 16777215))
        self.settings_page.setStyleSheet(u"QLabel {\n"
"color: white !important;\n"
"}\n"
"\n"
"QLineEdit {\n"
"background: white;\n"
"color: black;\n"
"padding: 8px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QDateEdit {\n"
"background: white;\n"
"color: black;\n"
"padding: 8px;\n"
"border-radius: 4px;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.settings_page)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_credentials = QFrame(self.settings_page)
        self.frame_credentials.setObjectName(u"frame_credentials")
        self.frame_credentials.setMinimumSize(QSize(512, 0))
        self.frame_credentials.setMaximumSize(QSize(512, 16777215))
        self.frame_credentials.setStyleSheet(u"background: #00008F; border-radius: 12px;")
        self.frame_credentials.setFrameShape(QFrame.StyledPanel)
        self.frame_credentials.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_credentials)
        self.verticalLayout_9.setSpacing(35)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.splitter_username = QSplitter(self.frame_credentials)
        self.splitter_username.setObjectName(u"splitter_username")
        self.splitter_username.setOrientation(Qt.Horizontal)
        self.splitter_username.setChildrenCollapsible(False)
        self.label_username = QLabel(self.splitter_username)
        self.label_username.setObjectName(u"label_username")
        self.splitter_username.addWidget(self.label_username)
        self.input_username = QLineEdit(self.splitter_username)
        self.input_username.setObjectName(u"input_username")
        self.input_username.setMinimumSize(QSize(340, 0))
        self.input_username.setMaximumSize(QSize(340, 16777215))
        self.input_username.setStyleSheet(u"background: white;\n"
"color: black;")
        self.splitter_username.addWidget(self.input_username)

        self.verticalLayout_9.addWidget(self.splitter_username)

        self.splitter_password = QSplitter(self.frame_credentials)
        self.splitter_password.setObjectName(u"splitter_password")
        self.splitter_password.setOrientation(Qt.Horizontal)
        self.splitter_password.setChildrenCollapsible(False)
        self.label_password = QLabel(self.splitter_password)
        self.label_password.setObjectName(u"label_password")
        self.splitter_password.addWidget(self.label_password)
        self.input_password = QLineEdit(self.splitter_password)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setMinimumSize(QSize(340, 0))
        self.input_password.setMaximumSize(QSize(340, 16777215))
        self.input_password.setFocusPolicy(Qt.StrongFocus)
        self.input_password.setStyleSheet(u"background: white;\n"
"color: black;")
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setClearButtonEnabled(False)
        self.splitter_password.addWidget(self.input_password)

        self.verticalLayout_9.addWidget(self.splitter_password)


        self.verticalLayout_15.addWidget(self.frame_credentials, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_filters = QFrame(self.settings_page)
        self.frame_filters.setObjectName(u"frame_filters")
        self.frame_filters.setMinimumSize(QSize(720, 256))
        self.frame_filters.setMaximumSize(QSize(720, 256))
        self.frame_filters.setStyleSheet(u"background: #00008F; border-radius: 12px;")
        self.frame_filters.setFrameShape(QFrame.StyledPanel)
        self.frame_filters.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_filters)
        self.verticalLayout_14.setSpacing(32)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 16)
        self.splitter_interval_dates = QSplitter(self.frame_filters)
        self.splitter_interval_dates.setObjectName(u"splitter_interval_dates")
        self.splitter_interval_dates.setMinimumSize(QSize(0, 64))
        self.splitter_interval_dates.setMaximumSize(QSize(664, 16777215))
        self.splitter_interval_dates.setLineWidth(1)
        self.splitter_interval_dates.setOrientation(Qt.Horizontal)
        self.splitter_interval_dates.setHandleWidth(64)
        self.splitter_initial = QSplitter(self.splitter_interval_dates)
        self.splitter_initial.setObjectName(u"splitter_initial")
        self.splitter_initial.setOrientation(Qt.Vertical)
        self.label_initial_date = QLabel(self.splitter_initial)
        self.label_initial_date.setObjectName(u"label_initial_date")
        self.splitter_initial.addWidget(self.label_initial_date)
        self.initial_date = QDateEdit(self.splitter_initial)
        self.initial_date.setObjectName(u"initial_date")
        self.initial_date.setMinimumSize(QSize(300, 0))
        self.initial_date.setMaximumSize(QSize(300, 16777215))
        self.initial_date.setStyleSheet(u"background: white;\n"
"color: black;")
        self.initial_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.splitter_initial.addWidget(self.initial_date)
        self.splitter_interval_dates.addWidget(self.splitter_initial)
        self.splitter_5 = QSplitter(self.splitter_interval_dates)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Vertical)
        self.label_final_date = QLabel(self.splitter_5)
        self.label_final_date.setObjectName(u"label_final_date")
        self.splitter_5.addWidget(self.label_final_date)
        self.final_date = QDateEdit(self.splitter_5)
        self.final_date.setObjectName(u"final_date")
        self.final_date.setMinimumSize(QSize(300, 0))
        self.final_date.setMaximumSize(QSize(300, 16777215))
        self.final_date.setStyleSheet(u"background: white;\n"
"color: black;")
        self.final_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.splitter_5.addWidget(self.final_date)
        self.splitter_interval_dates.addWidget(self.splitter_5)

        self.verticalLayout_14.addWidget(self.splitter_interval_dates, 0, Qt.AlignHCenter)

        self.splitter_7 = QSplitter(self.frame_filters)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Horizontal)
        self.splitter_7.setChildrenCollapsible(False)
        self.label_material = QLabel(self.splitter_7)
        self.label_material.setObjectName(u"label_material")
        self.label_material.setMinimumSize(QSize(96, 0))
        self.label_material.setMaximumSize(QSize(96, 16777215))
        self.splitter_7.addWidget(self.label_material)
        self.input_material = QLineEdit(self.splitter_7)
        self.input_material.setObjectName(u"input_material")
        self.input_material.setMinimumSize(QSize(512, 0))
        self.input_material.setMaximumSize(QSize(512, 16777215))
        self.input_material.setStyleSheet(u"background: white;\n"
"color: black;")
        self.splitter_7.addWidget(self.input_material)

        self.verticalLayout_14.addWidget(self.splitter_7, 0, Qt.AlignHCenter)

        self.splitter_8 = QSplitter(self.frame_filters)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Horizontal)
        self.splitter_8.setChildrenCollapsible(False)
        self.label_fornecedor = QLabel(self.splitter_8)
        self.label_fornecedor.setObjectName(u"label_fornecedor")
        self.label_fornecedor.setMinimumSize(QSize(96, 0))
        self.label_fornecedor.setMaximumSize(QSize(96, 16777215))
        self.splitter_8.addWidget(self.label_fornecedor)
        self.input_fornecedor = QLineEdit(self.splitter_8)
        self.input_fornecedor.setObjectName(u"input_fornecedor")
        self.input_fornecedor.setMinimumSize(QSize(512, 0))
        self.input_fornecedor.setMaximumSize(QSize(512, 16777215))
        self.input_fornecedor.setStyleSheet(u"background: white;\n"
"color: black;")
        self.splitter_8.addWidget(self.input_fornecedor)

        self.verticalLayout_14.addWidget(self.splitter_8, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_filters, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_settings_buttons = QFrame(self.settings_page)
        self.frame_settings_buttons.setObjectName(u"frame_settings_buttons")
        self.frame_settings_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_settings_buttons)
        self.horizontalLayout_8.setSpacing(64)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_confirm_settings = QPushButton(self.frame_settings_buttons)
        self.btn_confirm_settings.setObjectName(u"btn_confirm_settings")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_confirm_settings.sizePolicy().hasHeightForWidth())
        self.btn_confirm_settings.setSizePolicy(sizePolicy2)
        self.btn_confirm_settings.setMinimumSize(QSize(140, 0))
        self.btn_confirm_settings.setMaximumSize(QSize(140, 16777215))
        self.btn_confirm_settings.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 12px;\n"
"	border-radius: 12px;\n"
"	background: #005012;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background: #019421\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #54cb62;\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_confirm_settings)

        self.btn_cancel_settings = QPushButton(self.frame_settings_buttons)
        self.btn_cancel_settings.setObjectName(u"btn_cancel_settings")
        self.btn_cancel_settings.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_cancel_settings.sizePolicy().hasHeightForWidth())
        self.btn_cancel_settings.setSizePolicy(sizePolicy3)
        self.btn_cancel_settings.setMinimumSize(QSize(140, 0))
        self.btn_cancel_settings.setMaximumSize(QSize(140, 16777215))
        self.btn_cancel_settings.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 12px;\n"
"	border-radius: 12px;\n"
"	background: #A50000;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background: #DB1F1F\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #fe5243;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background: #656568;\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_cancel_settings)


        self.verticalLayout_15.addWidget(self.frame_settings_buttons, 0, Qt.AlignHCenter)

        pages.addWidget(self.settings_page)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.verticalLayout_6 = QVBoxLayout(self.info_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_info = QFrame(self.info_page)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMinimumSize(QSize(512, 300))
        self.frame_info.setMaximumSize(QSize(512, 340))
        self.frame_info.setStyleSheet(u"background: #C4C4C4; border-radius: 12px; color: black;")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_info)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 9, -1, -1)
        self.label_name_icon = QLabel(self.frame_info)
        self.label_name_icon.setObjectName(u"label_name_icon")
        self.label_name_icon.setMinimumSize(QSize(0, 18))
        self.label_name_icon.setMaximumSize(QSize(16777215, 18))
        self.label_name_icon.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.label_name_icon)

        self.label_logo = QLabel(self.frame_info)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setPixmap(QPixmap(u"./view/UI/images/icons/swi_logo.png"))
        self.label_logo.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_logo)

        self.label_version_info = QLabel(self.frame_info)
        self.label_version_info.setObjectName(u"label_version_info")

        self.verticalLayout_10.addWidget(self.label_version_info, 0, Qt.AlignVCenter)

        self.label_author_info = QLabel(self.frame_info)
        self.label_author_info.setObjectName(u"label_author_info")
        self.label_author_info.setWordWrap(False)
        self.label_author_info.setOpenExternalLinks(True)

        self.verticalLayout_10.addWidget(self.label_author_info, 0, Qt.AlignVCenter)


        self.verticalLayout_6.addWidget(self.frame_info, 0, Qt.AlignHCenter)

        self.frame_buttons_info = QFrame(self.info_page)
        self.frame_buttons_info.setObjectName(u"frame_buttons_info")
        self.frame_buttons_info.setMaximumSize(QSize(256, 256))
        self.frame_buttons_info.setStyleSheet(u"QPushButton {\n"
"background: #00B4A9;\n"
"padding: 12px;\n"
"border-radius: 12px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #75E3DD;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #93e2e3;\n"
"}\n"
"\n"
"#btn_check_update {\n"
"background: #0E89CE;\n"
"}\n"
"\n"
"#btn_check_update:hover {\n"
"background: #60A2C7;\n"
"}\n"
"\n"
"#btn_check_update:pressed {\n"
"background: #7bbedd;\n"
"}")
        self.frame_buttons_info.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_buttons_info)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_check_update = QPushButton(self.frame_buttons_info)
        self.btn_check_update.setObjectName(u"btn_check_update")
        self.btn_check_update.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.btn_check_update)

        self.btn_view_log = QPushButton(self.frame_buttons_info)
        self.btn_view_log.setObjectName(u"btn_view_log")

        self.verticalLayout_11.addWidget(self.btn_view_log)

        self.btn_feedback = QPushButton(self.frame_buttons_info)
        self.btn_feedback.setObjectName(u"btn_feedback")
        self.btn_feedback.setStyleSheet(u"margin-top: 72px")

        self.verticalLayout_11.addWidget(self.btn_feedback)


        self.verticalLayout_6.addWidget(self.frame_buttons_info, 0, Qt.AlignHCenter)

        pages.addWidget(self.info_page)
        self.exit_page = QWidget()
        self.exit_page.setObjectName(u"exit_page")
        self.horizontalLayout_6 = QHBoxLayout(self.exit_page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame = QFrame(self.exit_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_content_exit = QFrame(self.frame)
        self.frame_content_exit.setObjectName(u"frame_content_exit")
        self.frame_content_exit.setMinimumSize(QSize(512, 172))
        self.frame_content_exit.setMaximumSize(QSize(512, 200))
        self.frame_content_exit.setStyleSheet(u"background-color: #C4C4C4; border-radius: 12px;")
        self.frame_content_exit.setFrameShape(QFrame.Panel)
        self.frame_content_exit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_content_exit)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_text = QFrame(self.frame_content_exit)
        self.frame_text.setObjectName(u"frame_text")
        self.frame_text.setLayoutDirection(Qt.LeftToRight)
        self.frame_text.setAutoFillBackground(False)
        self.frame_text.setFrameShape(QFrame.StyledPanel)
        self.frame_text.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_text)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 18, -1, -1)
        self.label_confirm_exit = QLabel(self.frame_text)
        self.label_confirm_exit.setObjectName(u"label_confirm_exit")
        sizePolicy.setHeightForWidth(self.label_confirm_exit.sizePolicy().hasHeightForWidth())
        self.label_confirm_exit.setSizePolicy(sizePolicy)
        self.label_confirm_exit.setStyleSheet(u"font-weight: bold; font-size: 24px; color: black; margin-bottom: 24px")
        self.label_confirm_exit.setFrameShape(QFrame.StyledPanel)
        self.label_confirm_exit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_confirm_exit)

        self.label_info_exit = QLabel(self.frame_text)
        self.label_info_exit.setObjectName(u"label_info_exit")
        self.label_info_exit.setStyleSheet(u"color: black;")
        self.label_info_exit.setScaledContents(False)
        self.label_info_exit.setAlignment(Qt.AlignCenter)
        self.label_info_exit.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_info_exit)


        self.verticalLayout_7.addWidget(self.frame_text, 0, Qt.AlignTop)

        self.frame_buttons = QFrame(self.frame_content_exit)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setStyleSheet(u"QPushButton {\n"
"border-radius: 12px;\n"
"padding: 12px;\n"
"}")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_exit = QPushButton(self.frame_buttons)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setStyleSheet(u"QPushButton {\n"
"background: #A50000;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #DB1F1F\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #fe5243;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_exit)

        self.btn_cancel_exit = QPushButton(self.frame_buttons)
        self.btn_cancel_exit.setObjectName(u"btn_cancel_exit")
        self.btn_cancel_exit.setStyleSheet(u"QPushButton {\n"
"font-weight: bold;\n"
"background: #0E89CE;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #60A2C7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #7bbedd;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_cancel_exit)


        self.verticalLayout_7.addWidget(self.frame_buttons, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_content_exit)


        self.horizontalLayout_6.addWidget(self.frame)

        pages.addWidget(self.exit_page)

        self.retranslateUi(pages)

        pages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(pages)
    # setupUi

    def retranslateUi(self, pages):
        pages.setWindowTitle("")
        self.label_notifications.setText(QCoreApplication.translate("pages", u"Zona de notifica\u00e7\u00f5es", None))
        self.btn_close_notification.setText("")
        self.label_info_user.setText(QCoreApplication.translate("pages", u"Informa\u00e7\u00f5es do usu\u00e1rio:", None))
        self.label_sigss.setText(QCoreApplication.translate("pages", u"SIGSS:", None))
        self.label_user_sigss.setText(QCoreApplication.translate("pages", u"Nenhum usu\u00e1rio conectado.", None))
        self.label_whatsapp.setText(QCoreApplication.translate("pages", u"WhatsApp:", None))
        self.label_user_whatsapp.setText(QCoreApplication.translate("pages", u"Nenhum usu\u00e1rio conectado.", None))
        self.btn_start.setText(QCoreApplication.translate("pages", u"INICIAR", None))
        self.btn_update_reg.setText(QCoreApplication.translate("pages", u"ATUALIZAR CADASTRO", None))
        self.btn_verify_contacts.setText(QCoreApplication.translate("pages", u"VERIFICAR CONTATOS", None))
        self.btn_send_messages.setText(QCoreApplication.translate("pages", u"REALIZAR COBRAN\u00c7A", None))
        self.btn_generate_reports.setText(QCoreApplication.translate("pages", u"GERAR RELAT\u00d3RIO", None))
        self.btn_view_reg.setText(QCoreApplication.translate("pages", u"VISUALIZAR CADASTRO", None))
        self.btn_change_reg.setText(QCoreApplication.translate("pages", u"ALTERAR CADASTRO", None))
        self.label_log.setText(QCoreApplication.translate("pages", u"Log de eventos", None))
        self.label_img_qr_code.setText(QCoreApplication.translate("pages", u"Aguarde o QR Code", None))
        self.timer.setFormat(QCoreApplication.translate("pages", u"%p", None))
        self.label_info.setText(QCoreApplication.translate("pages", u"<html><head/><body><p align=\"center\">Para efetuar o login, escaneie o QR Code acima, se a barra de tempo acabar \u00e9 poss\u00edvel tentar novamente.</p></body></html>", None))
        self.btn_again.setText(QCoreApplication.translate("pages", u"TENTAR NOVAMENTE", None))
        self.btn_cancel.setText(QCoreApplication.translate("pages", u"CANCELAR", None))
        self.label_username.setText(QCoreApplication.translate("pages", u"Usu\u00e1rio", None))
        self.label_password.setText(QCoreApplication.translate("pages", u"Senha", None))
        self.label_initial_date.setText(QCoreApplication.translate("pages", u"Data Inicial:", None))
        self.label_final_date.setText(QCoreApplication.translate("pages", u"Data Final:", None))
        self.label_material.setText(QCoreApplication.translate("pages", u"Material", None))
        self.label_fornecedor.setText(QCoreApplication.translate("pages", u"Fornecedor", None))
        self.btn_confirm_settings.setText(QCoreApplication.translate("pages", u"SALVAR", None))
        self.btn_cancel_settings.setText(QCoreApplication.translate("pages", u"CANCELAR", None))
        self.label_name_icon.setText(QCoreApplication.translate("pages", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Informa\u00e7\u00f5es do Sistema</span></p></body></html>", None))
        self.label_logo.setText("")
        self.label_version_info.setText(QCoreApplication.translate("pages", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; text-decoration: underline;\">SWI</span></p><p align=\"center\">Vers\u00e3o: 1.0</p><p align=\"center\">Data da vers\u00e3o: 01/08/2021</p></body></html>", None))
        self.label_author_info.setText(QCoreApplication.translate("pages", u"<html>\n"
"<head/>\n"
"<body>\n"
"  <p align=\"center\">\n"
"    Criado por: <span style=\" font-style:italic;\">Marlon Angeli</span>\n"
"  </p>\n"
"  <p align=\"center\">\n"
"    <a href=\"https://github.com/marlonangeli/sigss-whatsapp-integration\"><span style=\" text-decoration: underline; color:#0000ff;\">Abrir GitHub</span></a>\n"
"  </p>\n"
"</body>\n"
"</html>", None))
        self.btn_check_update.setText(QCoreApplication.translate("pages", u"VERIFICAR ATUALIZA\u00c7\u00d5ES", None))
        self.btn_view_log.setText(QCoreApplication.translate("pages", u"REGISTRO DE ATIVIDADES", None))
        self.btn_feedback.setText(QCoreApplication.translate("pages", u"ENVIAR FEEDBACK", None))
        self.label_confirm_exit.setText(QCoreApplication.translate("pages", u"Deseja sair do sistema?", None))
        self.label_info_exit.setText(QCoreApplication.translate("pages", u"<html><head/><body><p align=\"center\">Ao sair do sistema, os processos em execu\u00e7\u00e3o ser\u00e3o finalizados, registros n\u00e3o salvos podem ser perdidos.</p></body></html>", None))
        self.btn_exit.setText(QCoreApplication.translate("pages", u"SAIR", None))
        self.btn_cancel_exit.setText(QCoreApplication.translate("pages", u"CANCELAR", None))
    # retranslateUi

