import pyqtgraph as pg
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import math
import numpy as np

# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        # make place in pop up diagram
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # add option to write
        vbox = QtWidgets.QVBoxLayout(central_widget)

        # graph
        self.plot_widget = pg.PlotWidget()
        vbox.addWidget(self.plot_widget)

        # add horizontal box
        hbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)

        # make buttons
        self.start = QtWidgets.QSpinBox()
        self.start.setValue(0)
        hbox.addWidget(self.start)

        self.end = QtWidgets.QSpinBox()
        self.end.setValue(2*math.pi)
        hbox.addWidget(self.end)

        self.numpoint = QtWidgets.QSpinBox()
        self.numpoint.setValue(100)
        hbox.addWidget(self.numpoint)

        # # connect button with function
        self.start.valueChanged.connect(self.plot)
        self.end.valueChanged.connect(self.plot)
        self.numpoint.valueChanged.connect(self.plot)

    @Slot()
    def clear(self):
        self.plot_widget.clear()

    def plot(self):
        self.plot_widget.clear()
        start = float(self.start.text())
        end = float(self.end.text())
        numpoint = int(self.numpoint.text())
        x = np.linspace(start, end, numpoint)
        self.plot_widget.plot(x, np.sin(x), symbol=None, pen={"color": "k", "width": 5})
        self.plot_widget.setLabel("left", "sin(x)")
        self.plot_widget.setLabel("bottom", "x [radians]")

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.plot()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()  

