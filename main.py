from functools import partial
from time import sleep
import os
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from view.UI.ui_main import UI_Main

from src.models.whatsapp import WhatsApp
from threading import Thread


AUX_BUTTON_STYLESHEET = """
QPushButton {
    background-color: #2c3e50;
    color: white;
    border-radius: 5px;
    font-size: 12px;    
}
"""


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("SWI")
        self.setWindowIcon(QIcon("src/img/icons/icon.png"))

        self.ui = UI_Main()
        self.ui.setupUi(self)

        # Botão de expandir o menu
        self.ui.button_toggle_menu.clicked.connect(self.toggle_menu)

        # -----------------------------------------------------------
        # Botão da página inicial
        self.ui.button_home.clicked.connect(self.show_home_page)

        # Botão iniciar
        self.ui.ui_pages.btn_start.clicked.connect(self.start)

        # -----------------------------------------------------------
        # Botão da página de configurações
        self.ui.button_settings.clicked.connect(self.show_settings_page)

        # -----------------------------------------------------------
        # Botão da página de informações
        self.ui.button_info.clicked.connect(self.show_info_page)

        self.ui.ui_pages.btn_feedback.clicked.connect(
            lambda: self.ui.ui_pages.btn_feedback.setEnabled(False)
        )

        # -----------------------------------------------------------
        # Botão de sair
        self.ui.button_logoff.clicked.connect(self.show_exit_page)

        # Confirmar saída
        self.ui.ui_pages.btn_exit.clicked.connect(self.close)
        # Cancelar
        self.ui.ui_pages.btn_cancel_exit.clicked.connect(self.show_home_page) # Retorna para a página inicial

        # -----------------------------------------------------------
        # Fechar notificações
        self.ui.ui_pages.btn_close_notification.clicked.connect(self.ui.ui_pages.frame_notifications.hide)

        # -----------------------------------------------------------
        # Cancelar QR Code
        self.ui.ui_pages.btn_cancel.clicked.connect(self.cancel_login)

        self.ui.ui_pages.btn_verify_contacts.clicked.connect(self.verify_contacts)


        # Exibe a aplicação
        self.show()


    # Funcção que desabilita o botao
    def disable_button(self, btn):
        btn.setEnabled(False)
        btn.setStyleSheet()

    # Função que expande o menu
    def toggle_menu(self):
        menu_width = self.ui.left_menu_frame.width()
        self.progress_bar(15)

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
    
    def start(self):
        print('a funcao esta funcionando')
        self.ui.ui_pages.label_notifications.setText("Iniciando...")
        self.ui.ui_pages.frame_notifications.show()
        self.progress_bar(54)
        # self.progress_bar(64)
        # sleep(5)
        # self.ui.ui_pages.label_notifications.setText("Concluído!")
        # self.progress_bar(100)
        # sleep(2)
        # self.show_qr_code()
        loop = QEventLoop()
        QTimer.singleShot(5000, loop.quit)
        loop.exec()


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

    def verify_config(self):
        # TODO - verificar configurações
        pass

    def show_qr_code(self):
        self.whatsapp = WhatsApp()
        self.th = Thread(target=self.whatsapp.login)
        self.th.start()

        self.cancel_operation = False

        def timer(self, new_value):
            self.animation = QPropertyAnimation(self.ui.ui_pages.timer, b"value")
            self.animation.setStartValue(self.ui.ui_pages.timer.value())
            self.animation.setEndValue(new_value)
            self.animation.setDuration(500)
            self.animation.setEasingCurve(QEasingCurve.InOutCirc)
            self.animation.start()

    
        def logged(self):
            self.ui.ui_pages.timer.setValue(0)
            self.ui.ui_pages.label_notifications.setText("Login no WhatsApp realizado com sucesso.")
            self.ui.ui_pages.label_notifications.show()
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.home_page)
        
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.qr_code)
        for i in range(101):
            if self.whatsapp.is_logged:
                logged(self)
                break
            if self.cancel_operation:
                break
            if os.path.exists("src/tmp/qrcode.png"):
                self.ui.ui_pages.label_img_qr_code.setPixmap(QPixmap('src/tmp/qrcode.png'))
            self.loop(1)
            timer(self, i)


    def cancel_login(self):
        print('Indo cancelar')
        self.cancel_operation = True
        self.whatsapp.cancel = True
        self.ui.ui_pages.timer.setValue(0)

        self.th.join()
        del self.th
        self.ui.ui_pages.label_notifications.setText("Login no WhatsApp cancelado.")
        self.ui.ui_pages.label_notifications.show()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.home_page)
        print('Cancelado')


    def verify_contacts(self):
        self.ui.ui_pages.label_notifications.setText("Carregando contatos...")
        self.ui.ui_pages.frame_notifications.show()
        self.progress_bar(54)
        self.ui.ui_pages.label_notifications.setText("Concluído!")
        self.loop(2)
        self.show_qr_code()

    def loop(self, secs):
        loop = QEventLoop()
        QTimer.singleShot(secs*1000, loop.quit)
        loop.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
