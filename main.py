from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class SimpleTextEditGUI(QMainWindow):

    def __init__(self):
        super(SimpleTextEditGUI, self).__init__()
        uic.loadUi('windowEditor.ui', self)
        self.show()

        # set initial window title
        self.setWindowTitle("SimpleTextEdit") # change to file name once loaded

        # select font size actions
        self.action12pt.triggered.connect(lambda: self.change_font_size(12))
        self.action18pt.triggered.connect(lambda: self.change_font_size(18))
        self.action24pt.triggered.connect(lambda: self.change_font_size(24))

    def change_font_size(self, font_size):
        self.mainTextEdit.setFont(QFont("Arial", font_size))



def main():
    app = QApplication([])
    window = SimpleTextEditGUI()
    app.exec()

if __name__ == '__main__':
    main()

