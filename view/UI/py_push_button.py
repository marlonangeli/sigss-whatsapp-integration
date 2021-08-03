import os
import sys
sys.path.append("C:\\Users\\marlo\\Dropbox\\Dev\\Python\\Projects\\sigss-whatsapp-integration\\view")

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PyPushButton(QPushButton):
    def __init__(
        self,
        text = "",
        height = 64,
        minimum_width = 64,
        text_padding = 72,
        text_color = "white",
        icon_path = "",
        icon_color = "white",
        btn_color = "#0043A7",
        btn_hover = "#010A38",
        btn_pressed = "#0D62C6",
        is_active = False
    ):
        super().__init__()

        # Define os parâmetros padrões
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Parâmetros customizaveis
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Define o estilo do botão
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )
    
    # Define o botão como ativo
    def set_active(self, is_active_menu):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_menu
        )

    # Define o estilo do botão
    def set_style(
        self,
        text_padding = 64,
        text_color = "white",
        btn_color = "#0043A7",
        btn_hover = "#010A38",
        btn_pressed = "#0D62C6",
        is_active = False
    ):
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
            font-family: Montserrat;
            font-weight: bold;
            font-size: 16px;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """

        active_style = f"""
        QPushButton {{
            background-color: {btn_hover};
        }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)


    # Função para adicionar os ícones aos botões
    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)

        # Painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        # rect = QRect(0,0, self.minimum_width, self.height())
        rect = QRect(0,0, self.minimum_width, self.height())

        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()


    # Desenha o ícone
    def draw_icon(self, qp, image, rect, color):
        # Busca o caminho da imagem
        app_path = os.path.abspath(os.getcwd())
        folder = "./view/UI/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Desenha o ícone selecionado
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        # Centraliza o ícone no botão
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()
