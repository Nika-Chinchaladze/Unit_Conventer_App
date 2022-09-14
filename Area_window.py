from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QLineEdit
from PyQt5 import uic

class Aquaman(QMainWindow):
    def __init__(self):
        super(Aquaman, self).__init__()

        uic.loadUi("area.ui", self)

        # define content:
        self.area_label = self.findChild(QLabel, "area_label")
        self.from_label = self.findChild(QLabel, "from_label")
        self.to_label = self.findChild(QLabel, "to_label")
        self.answer_label = self.findChild(QLabel, "answer_label")
        # --------------------------------------------------------------- #
        self.meter_button = self.findChild(QPushButton, "meter_button")
        self.km_button = self.findChild(QPushButton, "km_button")
        self.cm_button = self.findChild(QPushButton, "cm_button")
        self.mili_button = self.findChild(QPushButton, "mili_button")
        self.micro_button = self.findChild(QPushButton, "micro_button")
        self.hect_button = self.findChild(QPushButton, "hect_button")
        self.mile_button = self.findChild(QPushButton, "mile_button")
        self.yard_button = self.findChild(QPushButton, "yard_button")
        self.foot_button = self.findChild(QPushButton, "foot_button")
        self.inch_button = self.findChild(QPushButton, "inch_button")
        self.acre_button = self.findChild(QPushButton, "acre_button")
        # --------------------------------------------------------------- #
        self.meter_button_2 = self.findChild(QPushButton, "meter_button_2")
        self.km_button_2 = self.findChild(QPushButton, "km_button_2")
        self.cm_button_2 = self.findChild(QPushButton, "cm_button_2")
        self.mili_button_2 = self.findChild(QPushButton, "mili_button_2")
        self.micro_button_2 = self.findChild(QPushButton, "micro_button_2")
        self.hect_button_2 = self.findChild(QPushButton, "hect_button_2")
        self.mile_button_2 = self.findChild(QPushButton, "mile_button_2")
        self.yard_button_2 = self.findChild(QPushButton, "yard_button_2")
        self.foot_button_2 = self.findChild(QPushButton, "foot_button_2")
        self.inch_button_2 = self.findChild(QPushButton, "inch_button_2")
        self.acre_button_2 = self.findChild(QPushButton, "acre_button_2")
        # --------------------------------------------------------------- #
        self.back_button = self.findChild(QPushButton, "back_button")
        self.convert_button = self.findChild(QPushButton, "convert_button")
        # --------------------------------------------------------------- #
        self.line_1 = self.findChild(QFrame, "line_1")
        self.line_2 = self.findChild(QFrame, "line_2")
        self.frame_1 = self.findChild(QFrame, "frame_1")
        self.frame_2 = self.findChild(QFrame, "frame_2")
        # --------------------------------------------------------------- #
        self.value_line = self.findChild(QLineEdit, "value_line")
        self.value_line.setPlaceholderText("value")

        # call defined functions from here:
        self.back_button.clicked.connect(self.ComeToSource)
        self.convert_button.clicked.connect(self.Convert_Into)
        self.meter_button.clicked.connect(self.Meter_1)
        self.meter_button_2.clicked.connect(self.Meter_2)
        self.km_button.clicked.connect(self.Km_meter_1)
        self.km_button_2.clicked.connect(self.Km_meter_2)
        self.cm_button.clicked.connect(self.Cm_meter_1)
        self.cm_button_2.clicked.connect(self.Cm_meter_2)
        self.mili_button.clicked.connect(self.Mili_meter_1)
        self.mili_button_2.clicked.connect(self.Mili_meter_2)
        self.micro_button.clicked.connect(self.Micro_meter_1)
        self.micro_button_2.clicked.connect(self.Micro_meter_2)
        self.hect_button.clicked.connect(self.Hect_meter_1)
        self.hect_button_2.clicked.connect(self.Hect_meter_2)
        self.mile_button.clicked.connect(self.Mile_1)
        self.mile_button_2.clicked.connect(self.Mile_2)
        self.yard_button.clicked.connect(self.Yard_1)
        self.yard_button_2.clicked.connect(self.Yard_2)
        self.foot_button.clicked.connect(self.Foot_1)
        self.foot_button_2.clicked.connect(self.Foot_2)
        self.inch_button.clicked.connect(self.Inch_1)
        self.inch_button_2.clicked.connect(self.Inch_2)
        self.acre_button.clicked.connect(self.Acre_1)
        self.acre_button_2.clicked.connect(self.Acre_2)

        self.show()
# ------------------------------------------ start -------------------------------------- #
    # define some colors:
    def Green_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(176, 255, 208);")
    
    def Red_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(255, 178, 216);")

    # define method for back button:
    def ComeToSource(self):
        from Source_window import Maryland
        self.window_land = QMainWindow()
        self.randy = Maryland()
        self.close()
    
    # define methods for temperature button:
    def Meter_1(self):
        self.from_label.setText("Square Meter")
    def Km_meter_1(self):
        self.from_label.setText("Square Kilometer")
    def Cm_meter_1(self):
        self.from_label.setText("Square Centimeter")
    def Mili_meter_1(self):
        self.from_label.setText("Square Millimeter")
    def Micro_meter_1(self):
        self.from_label.setText("Square Micrometer")
    def Hect_meter_1(self):
        self.from_label.setText("Hectare")
    def Mile_1(self):
        self.from_label.setText("Square Mile")
    def Yard_1(self):
        self.from_label.setText("Square Yard")
    def Foot_1(self):
        self.from_label.setText("Square Foot")
    def Inch_1(self):
        self.from_label.setText("Square Inch")
    def Acre_1(self):
        self.from_label.setText("Acre")
    
    def Meter_2(self):
        self.to_label.setText("Square Meter")
    def Km_meter_2(self):
        self.to_label.setText("Square Kilometer")
    def Cm_meter_2(self):
        self.to_label.setText("Square Centimeter")
    def Mili_meter_2(self):
        self.to_label.setText("Square Millimeter")
    def Micro_meter_2(self):
        self.to_label.setText("Square Micrometer")
    def Hect_meter_2(self):
        self.to_label.setText("Hectare")
    def Mile_2(self):
        self.to_label.setText("Square Mile")
    def Yard_2(self):
        self.to_label.setText("Square Yard")
    def Foot_2(self):
        self.to_label.setText("Square Foot")
    def Inch_2(self):
        self.to_label.setText("Square Inch")
    def Acre_2(self):
        self.to_label.setText("Acre")
    
    
    # define method for convert button:
    def Convert_Into(self):
        ent_value = self.value_line.text()
        from_value = self.from_label.text()
        to_value = self.to_label.text()
        answer = 0
        if len(ent_value) > 0:
            try:
                ent_value = float(ent_value)
                if from_value == "Square Meter":
                    if to_value == "Square Meter":
                        answer = ent_value
                    elif to_value == "Square Kilometer":
                        answer = ent_value / (10**6)
                    elif to_value == "Square Centimeter":
                        answer = ent_value * (10**4)
                    elif to_value == "Square Millimeter":
                        answer = ent_value * (10**6)
                    elif to_value == "Square Micrometer":
                        answer = ent_value * (10**12)
                    elif to_value == "Hectare":
                        answer = ent_value * 0.0001
                    elif to_value == "Square Mile":
                        answer = (ent_value * 3.86102159) / (10**7)
                    elif to_value == "Square Yard":
                        answer = ent_value * 1.19599005
                    elif to_value == "Square Foot":
                        answer = ent_value * 10.7639104
                    elif to_value == "Square Inch":
                        answer = ent_value * 1550.0031
                    elif to_value == "Acre":
                        answer = ent_value * 0.000247105381
                
                elif from_value == "Square Kilometer":
                    if to_value == "Square Meter":
                        answer = ent_value * (10**6)
                    elif to_value == "Square Kilometer":
                        answer = ent_value
                    elif to_value == "Square Centimeter":
                        answer = ent_value * (10**10)
                    elif to_value == "Square Millimeter":
                        answer = ent_value * (10**12)
                    elif to_value == "Square Micrometer":
                        answer = ent_value * (10**18)
                    elif to_value == "Hectare":
                        answer = ent_value * 100
                    elif to_value == "Square Mile":
                        answer = ent_value * 0.386102159
                    elif to_value == "Square Yard":
                        answer = ent_value * 1195990.05
                    elif to_value == "Square Foot":
                        answer = ent_value * 10763910.4
                    elif to_value == "Square Inch":
                        answer = ent_value * 1.5500031 * (10**9)
                    elif to_value == "Acre":
                        answer = ent_value * 247.105381

                elif from_value == "Square Centimeter":
                    if to_value == "Square Meter":
                        answer = ent_value * 0.0001
                    elif to_value == "Square Kilometer":
                        answer = ent_value / (10**10)
                    elif to_value == "Square Centimeter":
                        answer = ent_value
                    elif to_value == "Square Millimeter":
                        answer = ent_value * 100
                    elif to_value == "Square Micrometer":
                        answer = ent_value * (10**9)
                    elif to_value == "Hectare":
                        answer = ent_value / (10**8)
                    elif to_value == "Square Mile":
                        answer = (ent_value * 3.86102159) / (10**11)
                    elif to_value == "Square Yard":
                        answer = ent_value * 0.000119599005
                    elif to_value == "Square Foot":
                        answer = ent_value * 0.00107639104
                    elif to_value == "Square Inch":
                        answer = ent_value * 0.15500031
                    elif to_value == "Acre":
                        answer = (ent_value * 2.47105381) / (10**8)

                elif from_value == "Square Millimeter":
                    if to_value == "Square Meter":
                        answer = ent_value / (10**6)
                    elif to_value == "Square Kilometer":
                        answer = ent_value / (10**12)
                    elif to_value == "Square Centimeter":
                        answer = ent_value * 0.01
                    elif to_value == "Square Millimeter":
                        answer = ent_value
                    elif to_value == "Square Micrometer":
                        answer = ent_value * (10**6)
                    elif to_value == "Hectare":
                        answer = ent_value / (10**10)
                    elif to_value == "Square Mile":
                        answer = (ent_value * 3.86102159) / (10**13)
                    elif to_value == "Square Yard":
                        answer = (ent_value * 1.19599005) / (10**6)
                    elif to_value == "Square Foot":
                        answer = ent_value * 1.07639104 / (10**5)
                    elif to_value == "Square Inch":
                        answer = ent_value * 0.0015500031
                    elif to_value == "Acre":
                        answer = (ent_value * 2.47105381) / (10**10)

                elif from_value == "Square Micrometer":
                    if to_value == "Square Meter":
                        answer = ent_value / (10**12)
                    elif to_value == "Square Kilometer":
                        answer = ent_value / (10**18)
                    elif to_value == "Square Centimeter":
                        answer = ent_value / (10**8)
                    elif to_value == "Square Millimeter":
                        answer = ent_value / (10**6)
                    elif to_value == "Square Micrometer":
                        answer = ent_value
                    elif to_value == "Hectare":
                        answer = ent_value / (10**16)
                    elif to_value == "Square Mile":
                        answer = (ent_value * 3.86102159) / (10**19)
                    elif to_value == "Square Yard":
                        answer = (ent_value * 1.19599005) / (10**12)
                    elif to_value == "Square Foot":
                        answer = ent_value * 1.07639104 / (10**11)
                    elif to_value == "Square Inch":
                        answer = (ent_value * 1.5500031) / (10**9)
                    elif to_value == "Acre":
                        answer = (ent_value * 2.47105381) / (10**16)
               
                elif from_value == "Hectare":
                    if to_value == "Square Meter":
                        answer = ent_value * 10000
                    elif to_value == "Square Kilometer":
                        answer = ent_value * 0.01
                    elif to_value == "Square Centimeter":
                        answer = ent_value * (10**8)
                    elif to_value == "Square Millimeter":
                        answer = ent_value * (10**10)
                    elif to_value == "Square Micrometer":
                        answer = ent_value * (10**16)
                    elif to_value == "Hectare":
                        answer = ent_value
                    elif to_value == "Square Mile":
                        answer = ent_value * 0.00386102159
                    elif to_value == "Square Yard":
                        answer = ent_value * 11959.9005
                    elif to_value == "Square Foot":
                        answer = ent_value * 107639.104
                    elif to_value == "Square Inch":
                        answer = ent_value * 15500031
                    elif to_value == "Acre":
                        answer = ent_value * 2.47105381

                elif from_value == "Square Mile":
                    if to_value == "Square Meter":
                        answer = ent_value * 2589988.11
                    elif to_value == "Square Kilometer":
                        answer = ent_value * 2.58998811
                    elif to_value == "Square Centimeter":
                        answer = ent_value * 2.58998811 * (10**10)
                    elif to_value == "Square Millimeter":
                        answer = ent_value * 2589988110336
                    elif to_value == "Square Micrometer":
                        answer = ent_value * 2.58998811 * (10**18)
                    elif to_value == "Hectare":
                        answer = ent_value * 258.998811
                    elif to_value == "Square Mile":
                        answer = ent_value
                    elif to_value == "Square Yard":
                        answer = ent_value * 3097600
                    elif to_value == "Square Foot":
                        answer = ent_value * 27878400
                    elif to_value == "Square Inch":
                        answer = ent_value * 4014489600
                    elif to_value == "Acre":
                        answer = ent_value * 640

                elif from_value == "Square Yard":
                    if to_value == "Square Meter":
                        answer = ent_value * 0.83612736
                    elif to_value == "Square Kilometer":
                        answer = (ent_value * 8.3612736) / (10**7)
                    elif to_value == "Square Centimeter":
                        answer = ent_value * 8361.2736
                    elif to_value == "Square Millimeter":
                        answer = ent_value * 836127.36
                    elif to_value == "Square Micrometer":
                        answer = ent_value * 83612736 * (10**4)
                    elif to_value == "Hectare":
                        answer = (ent_value * 8.3612736) / (10**5)
                    elif to_value == "Square Mile":
                        answer = (ent_value * 3.22830579) / (10**7)
                    elif to_value == "Square Yard":
                        answer = ent_value
                    elif to_value == "Square Foot":
                        answer = ent_value * 9
                    elif to_value == "Square Inch":
                        answer = ent_value * 1296
                    elif to_value == "Acre":
                        answer = ent_value * 0.00020661157

                elif from_value == "Square Foot":
                    if to_value == "Square Meter":
                        answer = ent_value * 0.09290304
                    elif to_value == "Square Kilometer":
                        answer = (ent_value * 9.290304) / (10**8)
                    elif to_value == "Square Centimeter":
                        answer = ent_value * 929.0304
                    elif to_value == "Square Millimeter":
                        answer = ent_value * 92903.04
                    elif to_value == "Square Micrometer":
                        answer = ent_value * 9290304 * (10**4)
                    elif to_value == "Hectare":
                        answer = (ent_value * 9.290304) / (10**6)
                    elif to_value == "Square Mile":
                        answer = (ent_value * 3.58700643) / (10**8)
                    elif to_value == "Square Yard":
                        answer = ent_value * 0.111111111
                    elif to_value == "Square Foot":
                        answer = ent_value
                    elif to_value == "Square Inch":
                        answer = ent_value * 144
                    elif to_value == "Acre":
                        answer = (ent_value * 2.29568411) / (10**5)

                elif from_value == "Square Inch":
                    if to_value == "Square Meter":
                        answer = ent_value * 0.00064516
                    elif to_value == "Square Kilometer":
                        answer = (ent_value * 6.4516) / (10**10)
                    elif to_value == "Square Centimeter":
                        answer = ent_value * 6.4516
                    elif to_value == "Square Millimeter":
                        answer = ent_value * 645.16
                    elif to_value == "Square Micrometer":
                        answer = ent_value * 64516 * (10**4)
                    elif to_value == "Hectare":
                        answer = (ent_value * 6.4516) / (10**8)
                    elif to_value == "Square Mile":
                        answer = (ent_value * 2.49097669) / (10**10)
                    elif to_value == "Square Yard":
                        answer = ent_value * 0.000771604938
                    elif to_value == "Square Foot":
                        answer = ent_value * 0.00694444444
                    elif to_value == "Square Inch":
                        answer = ent_value
                    elif to_value == "Acre":
                        answer = (ent_value * 1.59422508) / (10**7)

                elif from_value == "Acre":
                    if to_value == "Square Meter":
                        answer = ent_value * 4046.85642
                    elif to_value == "Square Kilometer":
                        answer = ent_value * 0.00404685642
                    elif to_value == "Square Centimeter":
                        answer = ent_value * 40468564.2
                    elif to_value == "Square Millimeter":
                        answer = ent_value * 4.04685642 * (10**9)
                    elif to_value == "Square Micrometer":
                        answer = ent_value * 4.04685642 * (10**15)
                    elif to_value == "Hectare":
                        answer = ent_value * 0.404685642
                    elif to_value == "Square Mile":
                        answer = ent_value * 0.0015625
                    elif to_value == "Square Yard":
                        answer = ent_value * 4840
                    elif to_value == "Square Foot":
                        answer = ent_value * 43560
                    elif to_value == "Square Inch":
                        answer = ent_value * 6272640
                    elif to_value == "Acre":
                        answer = ent_value

                self.answer_label.setText(f"<font color='red'><b>Result:</b></font><font color='black'> <b>{ent_value}</b> {from_value} = <b>{answer}</b> {to_value}</font>")
                self.Green_color()
            except ValueError:
                self.answer_label.setText("Please enter only Numeric values!")
                self.Red_color()
        else:
            self.answer_label.setText("Please enter value!")
            self.Red_color()

# ------------------------------------------- end --------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    aqua = Aquaman()
    sys.exit(app.exec_())