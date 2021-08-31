import os
import sys
path = os.path.abspath(os.getcwd())
sys.path.append(path)

from src.services.models_core import *
from src.services.functions_core import *
from src.services.sigss_mv import *
from src.services.pandas_core import *
from src.services.thread_core import *
from functools import partial
from random import randint
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from view.UI.ui_main import UI_Main

PATH_TMP_FILE = "./src/tmp/tmp.txt"

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("SWI")
        self.setWindowIcon(QIcon("./view/UI/images/icons/icon.png"))
        self.__finish = False
        self.__execution = False
        self.__whatsapp_is_opened = False

        self.ui = UI_Main()
        self.ui.setupUi(self)

        self.verify_settings()
        self.progress_bar(0)

        # Thread(target=self.update_logs).start()
        self.__pool = ThreadPool(processes=3)
        self.__logger = self.__pool.apply_async(func=self.update_logs)

        # ===========================================================
        # HOME PAGE
        self.ui.button_home.clicked.connect(self.show_home_page)

        # Start button
        self.ui.ui_pages.btn_start.clicked.connect(self.start)

        # Update reg button
        self.ui.ui_pages.btn_update_reg.clicked.connect(self.thread)

        # Button verify contacts
        self.ui.ui_pages.btn_verify_contacts.clicked.connect(self.verify_contacts)

        # Button send messages
        self.ui.ui_pages.btn_send_messages.clicked.connect(self.send_message)

        # Button view reg
        self.ui.ui_pages.btn_view_reg.clicked.connect(self.view_reg_file)

        # Button change reg
        self.ui.ui_pages.btn_change_reg.clicked.connect(self.change_reg_file)

        # Button generate report
        self.ui.ui_pages.btn_generate_reports.clicked.connect(self.generate_reports)

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
        self.ui.ui_pages.btn_exit.clicked.connect(self.close_app)
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
        self.change_notification("Antes de prosseguir, verifique as configurações.")
        self.ui.ui_pages.btn_update_reg.setEnabled(True)
        self.progress_bar(100)

    def thread(self):
        self.th = Thread(target=self.update_reg)
        self.th.start()
        self.progress_bar(0)
        # self.th.join()
        # del self.th

    def update_reg(self):
        self.__execution = True
        self.ui.ui_pages.btn_start.setEnabled(False)
        self.change_notification("Esta etapa pode demorar de acordo com as configurações e com a conexão com a internet, "
            "por favor, aguarde a barra de progresso terminar para realizar alguma operação no sistema.")
        self.emprestimo = Emprestimo(remove_material=True)
        self.th2 = Thread(target=self.emprestimo.get_dataframe)
        self.th2.start()
        print(self.__counter(PATH_TMP_FILE))
        qtde_reg = self.__counter(PATH_TMP_FILE)
        time_notification = f"{qtde_reg[1]} registros encontrados, tempo estimado: {str(timedelta(seconds=30*qtde_reg[1]))[3:]}"
        self.ui.ui_pages.label_notifications.setText(time_notification)
        self.ui.ui_pages.btn_update_reg.setEnabled(False)
        
        # loop até finalizar os registros
        while not self.emprestimo.finished:
            counter = self.__counter(PATH_TMP_FILE)
            self.progress_bar((counter[0]+1) * (100/counter[1]))
            print(counter, "start")
            while self.__counter(PATH_TMP_FILE) == counter:
                if self.emprestimo.finished:
                    break
                self.loop(2)
                print('wait')
        print('finished')
        
        # pool = ThreadPool(processes=1)
        # async_result = pool.apply_async(self.emprestimo.get_dataframe)


        # self.th2.join()
        # del self.th2
        self.ui.ui_pages.btn_verify_contacts.setEnabled(True)
        self.update()
        # df = async_result.get()
        self.emprestimo.save_dataframe()

        self.ui.ui_pages.btn_view_reg.setEnabled(True)
        self.ui.ui_pages.btn_change_reg.setEnabled(True)
        self.__execution = False

    def verify_contacts(self):
        self.__execution = True
        self.change_notification("Carregando contatos...")
        self.show_qr_code()
        if self.whatsapp.is_logged:
            self.ui.ui_pages.label_user_whatsapp.setText(self.whatsapp.username)
            self.update()
            self.dataframe = pd.read_excel("./docs/relatorio.xlsx")
            self.show_home_page()
            qtde_contacts = len(self.dataframe)
            time_notification = f"{qtde_contacts} contatos encontrados, tempo estimado: {str(timedelta(seconds=25*qtde_contacts))[3:]}"
            self.change_notification(time_notification)
            self.ui.ui_pages.btn_verify_contacts.setEnabled(False)
            
            for index in range(qtde_contacts):
                def verify_contact(phone):
                    self.whatsapp.numero = phone
                    return self.whatsapp.verify_number()

                self.progress_bar((index+1) * (100 / len(self.dataframe)))
                # Thread(target=self.progress_bar, args=((index+1) * (100 / len(self.dataframe)),)).start()
                phones_verified = []
                phones = self.get_phone_from_string(string=self.dataframe.loc[index, 'Phones'])
                for phone in phones:
                    if phone:
                        # pool = ThreadPool(processes=1)
                        async_result = self.__pool.apply_async(verify_contact, (phone,))
                        # Thread(target=verify_contact, args=(phone,)).start()
                        result = async_result.get()
                        if result:
                            phones_verified.append(phone)
                        self.loop(10)

                if phones_verified:
                    self.dataframe.loc[index, "WhatsApp Phones"] = f'{pd.Series(phones_verified).values}'
                # else:
                #     self.dataframe.loc[index, "WhatsApp Phones"] = pd.Series(['False']).values
                self.emprestimo.save_dataframe(self.dataframe)

            self.ui.ui_pages.btn_send_messages.setEnabled(True)

        else:
            self.change_notification("É necessário fazer login no WhatsApp para enviar mensagens.")
        self.__execution = False

    def show_qr_code(self):
        self.ui.ui_pages.btn_cancel.setEnabled(True)
        self.ui.ui_pages.btn_again.setEnabled(False)
        self.whatsapp = WhatsApp()
        self.th = Thread(target=self.whatsapp.login)
        self.th.start()
        # self.__pool.apply_async(self.whatsapp.login)

        self.cancel_operation = False

        def timer(self, new_value):
            self.animation = QPropertyAnimation(self.ui.ui_pages.timer, b"value")
            self.animation.setStartValue(self.ui.ui_pages.timer.value())
            self.animation.setEndValue(new_value)
            self.animation.setDuration(500)
            self.animation.setEasingCurve(QEasingCurve.InOutCirc)
            self.animation.start()

    
        def logged(self):
            self.__whatsapp_is_opened = True
            self.ui.ui_pages.timer.setValue(0)
            self.change_notification("Login no WhatsApp realizado com sucesso.")
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.home_page)
            self.th.join()
            # del self.th

        
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.qr_code)
        for i in range(101):
            if self.whatsapp.is_logged:
                print('verificação concluida')
                logged(self)
                break
            if self.cancel_operation:
                break
            if os.path.exists("./src/tmp/qr_code.png"):
                self.ui.ui_pages.label_img_qr_code.setPixmap(QPixmap('./src/tmp/qr_code.png'))
            self.loop(1)
            timer(self, i)

        if not self.whatsapp.is_logged:
            self.ui.ui_pages.btn_again.setEnabled(True)
            self.ui.ui_pages.btn_cancel.setEnabled(False)
            # del self.th
            self.whatsapp.delete()

    def cancel_login(self):
        self.cancel_operation = True
        self.whatsapp.cancel = True
        self.ui.ui_pages.timer.setValue(0)

        # del self.th
        self.whatsapp.delete()
        self.change_notification(message="Login no WhatsApp cancelado")
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.home_page)
        print('Cancelado')

    def send_message(self):
        self.__execution = True
        # verifica se existe uma instancia da classe WhatsApp
        if not self.__whatsapp_is_opened:
            self.show_qr_code()
        if self.whatsapp.is_logged:
            self.__whatsapp_is_opened = True
            self.ui.ui_pages.btn_send_messages.setEnabled(False)
            self.change_notification("Carregando o WhatsApp...")
            self.dataframe = pd.read_excel("./docs/relatorio.xlsx")
            self.loop(3)
            self.change_notification("O processo de envio das mensagens é variável em um intervalo de 45 à 120 segundos, "
                "isso é necessário para evitar possíveis bloqueios na conta do WhatsApp, é recomendado deixar o sistema "
                "funcionando até o fim do processo.")
            
            df_check = self.dataframe.isnull()
            for index in range(len(self.dataframe)):
                self.progress_bar((index+1) * (100 / len(self.dataframe)))
                if not df_check.loc[index, 'WhatsApp Phones']:
                    phones = self.get_phone_from_string(string=self.dataframe.loc[index, 'WhatsApp Phones'])
                    for phone in phones:
                        print(phone, ' <- ', phones)
                        interval_dates = (
                            datetime.strptime(self.dataframe.loc[index, "Date Devolution"], "%d/%m/%Y") -
                            datetime.strptime(get_date(), "%d/%m/%Y")
                        )
                        if interval_dates.days <= 0:
                            self.whatsapp.numero = phone
                            self.whatsapp.send_message(message=self.dataframe.loc[index, "Message"])
                            self.dataframe.loc[index, "Date Message Send"] = get_date()
                            print(f'mensagem enviada para -> {phone}')
                            self.loop(randint(45, 120))

                self.emprestimo.save_dataframe(self.dataframe)

            self.ui.ui_pages.btn_generate_reports.setEnabled(True)
        self.__execution = False

    def view_reg_file(self):
        self.__execution = True
        self.change_notification("Abrindo arquivo de registro...")
        os.system(".\\docs\\relatorio.xlsx")
        self.__execution = False

    def change_reg_file(self):
        self.__execution = True
        self.change_notification("Abrindo arquivo de registro...")
        os.system(".\\docs\\relatorio.xlsx")
        self.__execution = False

    def generate_reports(self):
        self.__execution = True
        self.change_notification("Gerando relatório...")
        os.system(".\\docs\\relatorio.xlsx")
        self.__execution = False


    # SETTINGS PAGE
    def show_settings_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.settings_page)
        self.ui.button_settings.set_active(True)

    def change_settings(self):
        self.__credentials["username"] = self.ui.ui_pages.input_username.text().upper()
        self.__credentials["password"] = self.ui.ui_pages.input_password.text()
        self.__filters["data_inicial"] = self.ui.ui_pages.initial_date.date().toString("dd/MM/yyyy")
        self.__filters["data_final"] = (
            None if get_date() in self.ui.ui_pages.final_date.date().toString("dd/MM/yyyy")
            else self.ui.ui_pages.final_date.date().toString("dd/MM/yyyy")
        )
        self.__filters["beneficio"] = (
            None if "TODOS" or None in self.ui.ui_pages.input_material.text()
            else self.ui.ui_pages.input_material.text().upper()
        )
        self.__filters["fornecedor"] = (
            None if "NASF" in self.ui.ui_pages.input_fornecedor.text()
            else self.ui.ui_pages.input_fornecedor.text()
        )
        with open("./src/config/credentials.json", "w") as file:
            dump(self.__credentials, file)
        with open("./src/config/filter_request.json", "w") as file:
            dump(self.__filters, file)

        self.ui.ui_pages.label_user_sigss.setText(self.__credentials["username"])
        self.verify_settings()
        self.change_notification("Configurações atualizadas.")
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
        self.__execution = True
        self.change_notification("Abrindo arquivo de log...")
        Thread(target=lambda: os.system(f'cd {path} & notepad.exe ./src/logs/logs.log')).start()
        self.__execution = False

    def send_feedback(self):
        import webbrowser
        webbrowser.open('https://forms.gle/djMisrytLVsbKLzP6')
        self.change_notification("Usuário redirecionado para página de feedback")

    def verify_updates(self):
        self.__execution = True
        self.change_notification("Verificando atualizações...")
        Thread(target=lambda: os.system(f'cd {path} & git pull')).start()
        self.__execution = False
        self.change_notification("Atualizações verificadas.")
    

    # EXIT PAGE
    def show_exit_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.exit_page)
        self.ui.button_logoff.set_active(True)
        
    def close_app(self):
        if self.__execution:
            alert = QMessageBox()
            alert.about(self, 'ALERTA', "Ainda há processos em execução")
        if self.__whatsapp_is_opened:
            if self.whatsapp.is_logged:
                self.whatsapp.delete()
        else:
            self.__finish = True
            self.loop(1)
            # self.__logger.get()
            # del self.th
            # del self.th2
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

    def get_phone_from_string(self, string: str):
        range_phones = string[1:-1].split(' ')
        return [x[1:-1] for x in range_phones]

    def update_logs(self):
        while not self.__finish:
            with open("./src/tmp/tmp_log.log", "r") as file:
                self.ui.ui_pages.label_log.setText(file.read())
                self.loop(1)
        with open("./src/tmp/tmp_log.log", "w") as file:
            file.write("Área de atividades do sistema")
        return

    def change_notification(self, message):
        self.ui.ui_pages.label_notifications.setText(message)
        self.ui.ui_pages.frame_notifications.show()

    def __counter(self, file):
        if os.path.exists(file):
            with open(file, "r") as f:
                aux = f.read().split(";")
                return [int(aux[0]), int(aux[1])]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
