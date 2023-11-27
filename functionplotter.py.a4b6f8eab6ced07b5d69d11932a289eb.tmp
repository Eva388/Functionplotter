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
        """ sets up graphical user interface creating spinboxes for start, end and numpoint values
        """
        super().__init__()

        # make widget in pop up diagram
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # create vertical box
        vbox = QtWidgets.QVBoxLayout(central_widget)

        # make plotwidget, add to vbox
        self.plot_widget = pg.PlotWidget()
        vbox.addWidget(self.plot_widget)

        # create horizontal box, add to vbox
        hbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)

        # make spinboxes for start, end and numpoint values, set default values
        self.start = QtWidgets.QSpinBox()
        self.start.setValue(0)
        self.end = QtWidgets.QSpinBox()
        self.end.setValue(2*math.pi)
        self.numpoint = QtWidgets.QSpinBox()
        self.numpoint.setValue(100)
        
        # add values to hbox
        hbox.addWidget(self.start)
        hbox.addWidget(self.end)
        hbox.addWidget(self.numpoint)

        # give values to plot function
        self.start.valueChanged.connect(self.plot)
        self.end.valueChanged.connect(self.plot)
        self.numpoint.valueChanged.connect(self.plot)

    @Slot()
    def plot(self):
        """ plots sin(x) as function of x for n numpoints where start, end and numpoint default values can be changed in the interface
        """
        # clear graph when values are changed by user
        self.plot_widget.clear()

        # call on values made in class UserInterface, make floats
        start = float(self.start.text())
        end = float(self.end.text())
        numpoint = int(self.numpoint.text())

        # determine x and sin(x) values and plot
        x = np.linspace(start, end, numpoint)
        self.plot_widget.plot(x, np.sin(x), symbol=None, pen={"color": "k", "width": 5})
        self.plot_widget.setLabel("left", "sin(x)")
        self.plot_widget.setLabel("bottom", "x [radians]")

def main():
    """ calls on class Userinterface to plot and show graph
    """
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.plot()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()  

