from functools import partial
from time import sleep
import os
import sys
from json import JSONDecoder, dump
from threading import Thread
from multiprocessing.pool import ThreadPool

path = os.path.abspath(os.getcwd())

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from view.UI.ui_main import UI_Main

from src.models.whatsapp import WhatsApp
from src.models.emprestimo import Emprestimo
from src.tools.date import get_date


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("SWI")
        self.setWindowIcon(QIcon("./view/UI/images/icons/icon.png"))

        self.ui = UI_Main()
        self.ui.setupUi(self)

        self.verify_settings()

        # ===========================================================
        # HOME PAGE
        self.ui.button_home.clicked.connect(self.show_home_page)

        # Start button
        self.ui.ui_pages.btn_start.clicked.connect(self.start)

        # Update reg button
        self.ui.ui_pages.btn_update_reg.clicked.connect(self.thread)

        # Button verify contacts
        self.ui.ui_pages.btn_verify_contacts.clicked.connect(self.verify_contacts)

        # Close notification
        self.ui.ui_pages.btn_close_notification.clicked.connect(self.ui.ui_pages.frame_notifications.hide)

        # -----------------------------------------------------------
        # QR CODE PAGE        
        # Cancel verification
        self.ui.ui_pages.btn_cancel.clicked.connect(self.cancel_login)

        # Try again
        self.ui.ui_pages.btn_again.clicked.connect(self.verify_contacts)

        # ===========================================================
        # SETTINGS PAGE
        self.ui.button_settings.clicked.connect(self.show_settings_page)

        # Save changes
        self.ui.ui_pages.btn_confirm_settings.clicked.connect(self.change_settings)

        # Cancel changes
        self.ui.ui_pages.btn_cancel_settings.clicked.connect(self.verify_settings)

        # ===========================================================
        # INFO PAGE
        self.ui.button_info.clicked.connect(self.show_info_page)

        # Feedback button
        self.ui.ui_pages.btn_feedback.clicked.connect(self.send_feedback)

        # Button view log
        self.ui.ui_pages.btn_view_log.clicked.connect(self.view_log_file)


        # ===========================================================
        # LOGOFF PAGE
        self.ui.button_logoff.clicked.connect(self.show_exit_page)

        # Confirmar saída
        self.ui.ui_pages.btn_exit.clicked.connect(self.close)
        # Cancelar
        self.ui.ui_pages.btn_cancel_exit.clicked.connect(self.show_home_page) # Retorna para a página inicial      

        # Toggle menu
        self.ui.button_toggle_menu.clicked.connect(self.toggle_menu)

        # Exibe a aplicação
        self.show()

    
    # HOME PAGE
    def show_home_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.home_page)
        self.ui.button_home.set_active(True)

    def start(self):
        self.ui.ui_pages.label_notifications.setText("Antes de prosseguir, verifique as configurações.")
        self.ui.ui_pages.frame_notifications.show()
        self.ui.ui_pages.btn_update_reg.setEnabled(True)
        self.progress_bar(100)


    def thread(self):
        self.th = Thread(target=self.update_reg)
        self.th.start()


    def update_reg(self):
        self.ui.ui_pages.btn_start.setEnabled(False)
        self.ui.ui_pages.label_notifications.setText(
            "Esta etapa pode demorar de acordo com as configurações e com a conexão com a internet, "
            "por favor, aguarde a barra de progresso terminar para realizar alguma operação no sistema."
        )
        self.ui.ui_pages.frame_notifications.show()
        self.emprestimo = Emprestimo()
        # self.th2 = Thread(target=self.emprestimo.get_dataframe)
        # self.th2.start()
        pool = ThreadPool(processes=1)
        async_result = pool.apply_async(self.emprestimo.get_dataframe)
        self.ui.ui_pages.btn_update_reg.setEnabled(False)
        # self.th2.join()
        self.ui.ui_pages.btn_verify_contacts.setEnabled(True)
        # self.update()
        self.dataframe = async_result.get()
        
        

    def verify_contacts(self):
        self.ui.ui_pages.label_notifications.setText("Carregando contatos...")
        self.ui.ui_pages.frame_notifications.show()
        self.show_qr_code()
        if self.whatsapp.is_logged:
            self.ui.ui_pages.btn_send_messages.setEnabled(True)
            self.ui.ui_pages.btn_verify_contacts.setEnabled(False)


    def show_qr_code(self):
        self.ui.ui_pages.btn_cancel.setEnabled(True)
        self.ui.ui_pages.btn_again.setEnabled(False)
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
            self.th.join()
            del self.th

        
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.qr_code)
        for i in range(101):
            if self.whatsapp.is_logged:
                print('verificação concluida')
                logged(self)
                break
            if self.cancel_operation:
                break
            if os.path.exists("src/tmp/qrcode.png"):
                self.ui.ui_pages.label_img_qr_code.setPixmap(QPixmap('src/tmp/qrcode.png'))
            self.loop(1)
            timer(self, i)

        if not self.whatsapp.is_logged:
            self.ui.ui_pages.btn_again.setEnabled(True)
            self.ui.ui_pages.btn_cancel.setEnabled(False)
            self.th.join()
            del self.th
            self.whatsapp.delete()

    def cancel_login(self):
        print('Indo cancelar')
        self.cancel_operation = True
        self.whatsapp.cancel = True
        self.ui.ui_pages.timer.setValue(0)

        self.th.join()
        del self.th
        self.whatsapp.delete()
        self.ui.ui_pages.label_notifications.setText("Login no WhatsApp cancelado.")
        self.ui.ui_pages.label_notifications.show()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.home_page)
        print('Cancelado')

    def send_message(self):
        self.ui.ui_pages.btn_send_messages.setEnabled(False)
        self.ui.ui_pages.label_notifications.setText("Enviando mensagens...")
        self.ui.ui_pages.frame_notifications.show()

    # SETTINGS PAGE
    def show_settings_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.settings_page)
        self.ui.button_settings.set_active(True)

    def change_settings(self):
        self.__credentials["username"] = self.ui.ui_pages.input_username.text()
        self.__credentials["password"] = self.ui.ui_pages.input_password.text()
        self.__filters["data_inicial"] = self.ui.ui_pages.initial_date.date().toString("dd/MM/yyyy")
        self.__filters["data_final"] = (
            None if get_date() in self.ui.ui_pages.final_date.date().toString("dd/MM/yyyy")
            else self.ui.ui_pages.final_date.date().toString("dd/MM/yyyy")
        )
        self.__filters["beneficio"] = (
            None if "TODOS" in self.ui.ui_pages.input_material.text()
            else self.ui.ui_pages.input_material.text()
        )
        self.__filters["fornecedor"] = (
            None if "NASF" in self.ui.ui_pages.input_fornecedor.text()
            else self.ui.ui_pages.input_fornecedor.text()
        )

        with open("./src/config/credentials.json", "w") as file:
            dump(self.__credentials, file)
        with open("./src/config/filter_request.json", "w") as file:
            dump(self.__filters, file)

        self.show_home_page()

    def verify_settings(self):
        self.__credentials = JSONDecoder().decode(str(open("./src/config/credentials.json", "r").read()))
        self.__filters = JSONDecoder().decode(str(open("./src/config/filter_request.json", "r").read()))
        self.ui.ui_pages.input_username.setText(self.__credentials['username'])
        self.ui.ui_pages.input_password.setText(self.__credentials['password'])
        self.ui.ui_pages.initial_date.setDate(QDate.fromString(self.__filters['data_inicial'], "dd/MM/yyyy"))
        self.ui.ui_pages.final_date.setDate(
            QDate.fromString(get_date()
                            if self.__filters['data_final'] is None
                            else self.__filters['data_final'], "dd/MM/yyyy")
        )
        self.ui.ui_pages.input_fornecedor.setText(
            "NASF" if self.__filters['fornecedor'] is None
            else self.__filters['fornecedor']
        )
        self.ui.ui_pages.input_material.setText(
            "TODOS" if self.__filters['beneficio'] is None
            else self.__filters['beneficio']
        )
        self.ui.ui_pages.label_user_sigss.setText(self.__credentials['username'])
    

    # INFO PAGE
    def show_info_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.info_page)
        self.ui.button_info.set_active(True)

    def view_log_file(self):
        os.system(f'cd {path} & notepad.exe ./src/logs/logs.log')

    def send_feedback(self):
        import webbrowser
        webbrowser.open('https://forms.gle/djMisrytLVsbKLzP6')
    

    # EXIT PAGE
    def show_exit_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.exit_page)
        self.ui.button_logoff.set_active(True)    

    def close_app(self):
        # TODO - salvar operações em execução
        self.close()


    # AUX FUNCTIONS
    def loop(self, secs):
        loop = QEventLoop()
        QTimer.singleShot(secs*1000, loop.quit)
        loop.exec()

    def progress_bar(self, new_value):
        self.animation = QPropertyAnimation(self.ui.ui_pages.progressBar, b"value")
        self.animation.setStartValue(self.ui.ui_pages.progressBar.value())
        self.animation.setEndValue(new_value)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    def reset_selection(self):
        for btn in self.ui.left_menu_frame.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def disable_button(self, btn):
        btn.setEnabled(False)
        btn.setStyleSheet()

    def toggle_menu(self):
        menu_width = self.ui.left_menu_frame.width()
        self.progress_bar(15)

        width = 64
        if menu_width == 64:
            width = 240

        # Animate side menu
        self.animation = QPropertyAnimation(self.ui.left_menu_frame, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
