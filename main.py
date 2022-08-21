from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class SimpleTextEditGUI(QMainWindow):

    def __init__(self):
        super(SimpleTextEditGUI, self).__init__()
        uic.loadUi('windowEditor.ui', self)
        self.show()

        # set initial window title
        self.set_window_title("SimpleTextEdit")

        # handle font size actions
        self.action12pt.triggered.connect(lambda: self.change_font_size(12))
        self.action18pt.triggered.connect(lambda: self.change_font_size(18))
        self.action24pt.triggered.connect(lambda: self.change_font_size(24))

        # handle font style actions
        self.actionArial.triggered.connect(lambda: self.change_font_style("Arial"))
        self.actionTimes.triggered.connect(lambda: self.change_font_style("Times"))
        self.actionHelvetica.triggered.connect(lambda: self.change_font_style("Helvetica"))

        # handle file actions
        self.actionOpen.triggered.connect(self.open_file_local)
        self.actionSave.triggered.connect(self.save_file_local)

        # handle program exit/close
        self.actionClose.triggered.connect(exit)

    def open_file_local(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)", options=options)

        if filename != "":
            with open(filename, "r") as f:
                self.set_window_title(self.clean_file_path(filename))
                self.mainTextEdit.setPlainText(f.read())

    def save_file_local(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)", options=options)

        if filename != "":
            with open(filename, "w") as f:
                f.write(self.mainTextEdit.toPlainText())

    def closeEvent(self, QCloseEvent):
        dialogue = QMessageBox()
        dialogue.setText("Do you want to save this file before closing?")
        dialogue.addButton("Yes", QMessageBox.YesRole)
        dialogue.addButton("No", QMessageBox.NoRole)
        dialogue.addButton("Cancel", QMessageBox.RejectRole)

        response = dialogue.exec()

        # continue exit if response is == 1 (NoRole)

        if response == 0:
            self.save_file_local()
            QCloseEvent.accept()

        elif response == 2:
            QCloseEvent.ignore()

    def change_font_size(self, font_size):
        font = self.mainTextEdit.font()
        font_style = font.family()
        self.mainTextEdit.setFont(QFont(font_style, font_size))

    def change_font_style(self, font_style):
        font = self.mainTextEdit.font()
        font_size = font.pointSize()
        self.mainTextEdit.setFont(QFont(font_style, font_size))

    def set_window_title(self, window_title):
        self.setWindowTitle(window_title)

    def clean_file_path(self, file_path):
        path_arr = file_path.split("/")
        return path_arr[len(path_arr) - 1]


def main():
    app = QApplication([])
    window = SimpleTextEditGUI()
    app.exec()

if __name__ == '__main__':
    main()

