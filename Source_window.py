from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
from Temperature_window import Spiderman
from Length_window import Batman
from Weight_window import Ironman
from Time_window import Blackpanter
from Area_window import Aquaman
from Volume_window import NinjaTurtle

class Maryland(QMainWindow):
    def __init__(self):
        super(Maryland, self).__init__()

        uic.loadUi("source.ui", self)

        # define content:
        self.head_label = self.findChild(QLabel, "head_label")
        self.len_button = self.findChild(QPushButton, "len_button")
        self.temp_button = self.findChild(QPushButton, "temp_button")
        self.area_button = self.findChild(QPushButton, "area_button")
        self.vol_button = self.findChild(QPushButton, "vol_button")
        self.wei_button = self.findChild(QPushButton, "wei_button")
        self.time_button = self.findChild(QPushButton, "time_button")
        self.close_button = self.findChild(QPushButton, "close_button")

        # call defined functions from here:
        self.len_button.clicked.connect(self.GoToLength)
        self.temp_button.clicked.connect(self.GoToTemperature)
        self.wei_button.clicked.connect(self.GoToWeight)
        self.time_button.clicked.connect(self.GoToTime)
        self.area_button.clicked.connect(self.GoToArea)
        self.vol_button.clicked.connect(self.GoToVolume)
        self.close_button.clicked.connect(lambda: self.close())


        self.show()
# ------------------------------------------ start -------------------------------------- #
    # define method for next windows:
    def GoToLength(self):
        self.window_len = QMainWindow()
        self.bat = Batman()
        self.close()
    
    def GoToTemperature(self):
        self.window_temp = QMainWindow()
        self.man = Spiderman()
        self.close()
    
    def GoToArea(self):
        self.window_area = QMainWindow()
        self.aqua = Aquaman()
        self.close()
    
    def GoToVolume(self):
        self.window_volume = QMainWindow()
        self.ninja = NinjaTurtle()
        self.close()

    def GoToWeight(self):
        self.window_weight = QMainWindow()
        self.iron = Ironman()
        self.close()
    
    def GoToTime(self):
        self.window_time = QMainWindow()
        self.panter = Blackpanter()
        self.close()

# ------------------------------------------- end --------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    land = Maryland()
    sys.exit(app.exec_())