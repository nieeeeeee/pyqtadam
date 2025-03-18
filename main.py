import sys
import random
import string

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox
import layout

class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = layout.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonGenerate.clicked.connect(self.generate_password)
        self.ui.zatwierdz.clicked.connect(self.zatwierdz)
        self.show()

    def generate_password(self):
        num_chars = self.ui.spinBox.value()

        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        special_chars = "!@#$%^&*()_+-="

        char_set = lowercase_letters

        if self.ui.checkUperLower.isChecked():
            char_set += uppercase_letters
        if self.ui.checkCyfry.isChecked():
            char_set += digits
        if self.ui.checkSpecialCharacters.isChecked():
            char_set += special_chars

        password = [random.choice(digits)] if self.ui.checkCyfry.isChecked() else []

        if self.ui.checkSpecialCharacters.isChecked():
            password.append(random.choice(special_chars))

        password += random.choices(char_set, k=num_chars - len(password))

        random.shuffle(password)

        password = ''.join(password)

        return password

    def zatwierdz(self):
        imie = self.ui.EditImie.text()
        nazwisko = self.ui.EditNazwisko.text()

        stanowisko = self.ui.comboBox.currentText()

        password = self.generate_password()

        message = f"Dane pracownika:\nImię: {imie}\nNazwisko: {nazwisko}\nStanowisko: {stanowisko}\nHasło: {password}"
        QMessageBox.information(self, "Dane pracownika", message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
