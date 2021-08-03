from functools import partial
from time import sleep
import os
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from view.UI.ui_main import UI_Main

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SWI")

        self.ui = UI_Main()
        self.ui.setup_ui(self)

        # Botão de expandir o menu
        self.ui.button_toggle_menu.clicked.connect(self.toggle_menu)

        # -----------------------------------------------------------
        # Botão da página inicial
        self.ui.button_home.clicked.connect(self.show_home_page)

        # Botão de iniciar
        self.ui.ui_pages.btn_start.clicked.connect(self.progress_bar(64))

        # -----------------------------------------------------------
        # Botão da página de configurações
        self.ui.button_settings.clicked.connect(self.show_settings_page)

        # -----------------------------------------------------------
        # Botão da página de informações
        self.ui.button_info.clicked.connect(self.show_info_page)

        # -----------------------------------------------------------
        # Botão de sair
        self.ui.button_logoff.clicked.connect(self.show_exit_page)

        # Confirmar saída
        self.ui.ui_pages.btn_exit.clicked.connect(self.close)
        # Cancelar
        self.ui.ui_pages.btn_cancel_exit.clicked.connect(self.show_home_page) # Retorna para a página inicial



        # Exibe a aplicação
        self.show()

    # Função que expande o menu
    def toggle_menu(self):
        menu_width = self.ui.left_menu_frame.width()

        width = 64
        if menu_width == 64:
            width = 240

        # Animação da expansão do menu    
        self.animation = QPropertyAnimation(self.ui.left_menu_frame, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()
    
    def progress_bar(self, new_value):
        self.animation = QPropertyAnimation(self.ui.ui_pages.progressBar, b"value")
        self.animation.setStartValue(self.ui.ui_pages.progressBar.value())
        self.animation.setEndValue(new_value)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    # Reseta seleção do botão
    def reset_selection(self):
        for btn in self.ui.left_menu_frame.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
    
    # HOME PAGE
    def show_home_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.home_page)
        self.ui.button_home.set_active(True)

    # SETTINGS PAGE
    def show_settings_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.settings_page)
        self.ui.button_settings.set_active(True)

    # INFO PAGE
    def show_info_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.info_page)
        self.ui.button_info.set_active(True)
        
    # EXIT PAGE
    def show_exit_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.exit_page)
        self.ui.button_logoff.set_active(True)    

    # END APP
    def close_app(self):
        # TODO - salvar operações em execução
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
