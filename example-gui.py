import sys
from PySide6 import QtWidgets

from PySide6.QtCore import Slot


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # make place in pop up diagram
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # add option to write
        vbox = QtWidgets.QVBoxLayout(central_widget)
        self.textedit = QtWidgets.QTextEdit()
        vbox.addWidget(self.textedit)

        # add horizontal box
        hbox = QtWidgets.QHBoxLayout()
        hbox2 = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)

        # make buttons
        clear_button = QtWidgets.QPushButton("Clear")
        hbox.addWidget(clear_button)

        add_text_button = QtWidgets.QPushButton("Add text")
        hbox.addWidget(add_text_button)

        # hello world button
        hello_world_button = QtWidgets.QPushButton("Hello, world")
        hbox.addWidget(hello_world_button)

        # quit button
        quit_button = QtWidgets.QPushButton("Quit")
        hbox2.addWidget(quit_button)
        
        # connect button with function
        clear_button.clicked.connect(self.textedit.clear)
        add_text_button.clicked.connect(self.add_text_button_clicked)
        hello_world_button.clicked.connect(self.hello_world_button_clicked)
        quit_button.clicked.connect(self.quit_button_clicked)

    @Slot()
    def add_text_button_clicked(self):
        self.textedit.append("You clicked me.")

    def hello_world_button_clicked(self):
        self.textedit.append("Hello, world")
    
    def quit_button_clicked(self):
        self.close()



def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  

