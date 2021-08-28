import os
import sys
sys.path.append("C:\\Users\\marlo\\Dropbox\\Dev\\Python\\Projects\\sigss-whatsapp-integration\\view")

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# from py_push_button import PyPushButton
# from ui_pages import UI_Pages

from view.UI.py_push_button import PyPushButton
from view.UI.ui_pages import UI_Pages


class UI_Main(object):
    def setupUi(self, parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')

        # Define o tamanho da janela
        parent.resize(1128, 680)
        parent.setMinimumSize(1024, 680)

        # Frame principal que engloba todos os widgets
        self.main_frame = QFrame()
        # self.main_frame.setStyleSheet('background-image: url(./view/UI/images/background.png)')

        # Cria layout para as páginas
        self.main_layout = QHBoxLayout(self.main_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Cria o menu lateral de navegação
        self.left_menu_frame = QFrame()
        self.left_menu_frame.setStyleSheet('background-color: #0043A7;')
        self.left_menu_frame.setMinimumWidth(64)
        self.left_menu_frame.setMaximumWidth(64)

        # Cria o layout do menu lateral
        self.left_menu_layout = QVBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # Cria os frames para posicionar os botões
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(40)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")

        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)


        # Adiciona os botões laterais ao menu
        self.button_toggle_menu = PyPushButton(
            text = 'MENU',
            icon_path = 'menu_64.png'
        )

        self.button_home = PyPushButton(
            text = 'PÁGINA INICIAL',
            icon_path = 'home_64.png',
            is_active =True
        )

        self.button_settings = PyPushButton(
            text = 'CONFIGURAÇÕES',
            icon_path = 'settings_64.png'
        )

        self.button_info = PyPushButton(
            text = 'INFORMAÇÕES',
            icon_path = 'info_64.png'
        )

        # Adiciona os botões na parte superior do menu do menu
        self.left_menu_top_layout.addWidget(self.button_toggle_menu)
        self.left_menu_top_layout.addWidget(self.button_home)
        self.left_menu_top_layout.addWidget(self.button_settings)
        self.left_menu_top_layout.addWidget(self.button_info)

        # Cria um espaçador entre os botões
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Cria o frame inferior no menu lateral
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")

        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)

        # Botão para sair do sistema
        self.button_logoff = PyPushButton(
            text = 'SAIR',
            icon_path = 'logoff_64.png',
            icon_color= '#A50000',
            btn_color = '#C4C4C4',
            btn_hover = '#656568',
            btn_pressed = '#B1B1B1',
            text_color= '#A50000'
        )

        # Adiciona ao frame inferior do menu
        self.left_menu_bottom_layout.addWidget(self.button_logoff)


        # Adiciona ao layout do menu lateral
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)

        # Cria o frame para o conteúdo das páginas
        self.content_frame = QFrame()
        self.content_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.494, y1:0, x2:0.511364, y2:1, stop:0 rgba(0, 0, 84, 255), stop:1 rgba(0, 35, 60, 255));")
        self.content_frame_layout = QHBoxLayout(self.content_frame)
        self.content_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.content_frame_layout.setSpacing(0)

        # Adiciona as paginas ao frame de conteudo
        self.pages = QStackedWidget()
        self.ui_pages = UI_Pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.home_page)

        # Disable buttons
        self.ui_pages.btn_update_reg.setEnabled(False)
        self.ui_pages.btn_verify_contacts.setEnabled(False)
        self.ui_pages.btn_send_messages.setEnabled(False)
        self.ui_pages.btn_generate_reports.setEnabled(False)
        self.ui_pages.btn_change_reg.setEnabled(False)
        self.ui_pages.btn_view_reg.setEnabled(False)
        self.ui_pages.btn_again.setEnabled(False)

        self.content_frame_layout.addWidget(self.pages)
        self.main_layout.addWidget(self.left_menu_frame)
        self.main_layout.addWidget(self.content_frame)

        parent.setCentralWidget(self.main_frame)
