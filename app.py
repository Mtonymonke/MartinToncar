import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QFile, QIODevice
from converter import Converter

class App:
    def __init__(self):
        self._window = None

    def fire_app(self):
        app = QApplication(sys.argv)
        ui_file = QFile(r"C:\Users\START\OneDrive\Plocha\škola\PVA\convertor\Form.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            self.show_error("Nepodařilo se načíst šablonu UI.")
        
        self._window = QUiLoader().load(ui_file)
        ui_file.close()
        if not self._window:
            self.show_error("Nepodařilo se načíst uživatelské okno.")

        self._window.pushButton.clicked.connect(self.handle_calculation)
        self._window.show()
        sys.exit(app.exec())

    def handle_calculation(self):
        try:
            value = float(self._window.textEdit.toPlainText())
            from_unit = self._window.comboBox_2.currentText()
            to_unit = self._window.comboBox.currentText()

            result = Converter.convert(value, from_unit, to_unit)
            if(result!=None):
                self._window.lineEdit_5.setText(str(result))
            else:
                self.show_error("Nelze.")
        except ValueError:
            self.show_error("Zadejte prosím číselnou hodnotu.")

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(message)
        msg.setWindowTitle("Chyba")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

if __name__ == "__main__":
    App().fire_app()
