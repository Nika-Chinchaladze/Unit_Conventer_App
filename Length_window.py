from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QLineEdit
from PyQt5 import uic

class Batman(QMainWindow):
    def __init__(self):
        super(Batman, self).__init__()

        uic.loadUi("length.ui", self)

        # define content:
        self.len_label = self.findChild(QLabel, "len_label")
        self.from_label = self.findChild(QLabel, "from_label")
        self.to_label = self.findChild(QLabel, "to_label")
        self.answer_label = self.findChild(QLabel, "answer_label")
        # --------------------------------------------------------------- #
        self.meter_button = self.findChild(QPushButton, "meter_button")
        self.km_button = self.findChild(QPushButton, "km_button")
        self.cm_button = self.findChild(QPushButton, "cm_button")
        self.mili_button = self.findChild(QPushButton, "mili_button")
        self.micro_button = self.findChild(QPushButton, "micro_button")
        self.nano_button = self.findChild(QPushButton, "nano_button")
        self.mile_button = self.findChild(QPushButton, "mile_button")
        self.yard_button = self.findChild(QPushButton, "yard_button")
        self.foot_button = self.findChild(QPushButton, "foot_button")
        self.inch_button = self.findChild(QPushButton, "inch_button")
        self.light_button = self.findChild(QPushButton, "light_button")
        # --------------------------------------------------------------- #
        self.meter_button_3 = self.findChild(QPushButton, "meter_button_3")
        self.km_button_3 = self.findChild(QPushButton, "km_button_3")
        self.cm_button_3 = self.findChild(QPushButton, "cm_button_3")
        self.mili_button_3 = self.findChild(QPushButton, "mili_button_3")
        self.micro_button_3 = self.findChild(QPushButton, "micro_button_3")
        self.nano_button_3 = self.findChild(QPushButton, "nano_button_3")
        self.mile_button_3 = self.findChild(QPushButton, "mile_button_3")
        self.yard_button_3 = self.findChild(QPushButton, "yard_button_3")
        self.foot_button_3 = self.findChild(QPushButton, "foot_button_3")
        self.inch_button_3 = self.findChild(QPushButton, "inch_button_3")
        self.light_button_3 = self.findChild(QPushButton, "light_button_3")
        # --------------------------------------------------------------- #
        self.back_button = self.findChild(QPushButton, "back_button")
        # --------------------------------------------------------------- #
        self.line_1 = self.findChild(QFrame, "line_1")
        self.line_2 = self.findChild(QFrame, "line_2")
        self.frame_1 = self.findChild(QFrame, "frame_1")
        self.frame_2 = self.findChild(QFrame, "frame_2")
        # --------------------------------------------------------------- #
        self.value_line = self.findChild(QLineEdit, "value_line")
        self.value_line.setPlaceholderText("value")

        # call defined functions from here:
        self.back_button.clicked.connect(self.BackToSource)
        self.meter_button.clicked.connect(self.Meter_1)
        self.meter_button_3.clicked.connect(self.Meter_2)
        self.km_button.clicked.connect(self.Km_meter_1)
        self.km_button_3.clicked.connect(self.Km_meter_2)
        self.cm_button.clicked.connect(self.Cm_meter_1)
        self.cm_button_3.clicked.connect(self.Cm_meter_2)
        self.mili_button.clicked.connect(self.Mili_meter_1)
        self.mili_button_3.clicked.connect(self.Mili_meter_2)
        self.micro_button.clicked.connect(self.Micro_meter_1)
        self.micro_button_3.clicked.connect(self.Micro_meter_2)
        self.nano_button.clicked.connect(self.Nano_meter_1)
        self.nano_button_3.clicked.connect(self.Nano_meter_2)
        self.mile_button.clicked.connect(self.Mile_1)
        self.mile_button_3.clicked.connect(self.Mile_2)
        self.yard_button.clicked.connect(self.Yard_1)
        self.yard_button_3.clicked.connect(self.Yard_2)
        self.foot_button.clicked.connect(self.Foot_1)
        self.foot_button_3.clicked.connect(self.Foot_2)
        self.inch_button.clicked.connect(self.Inch_1)
        self.inch_button_3.clicked.connect(self.Inch_2)
        self.light_button.clicked.connect(self.Light_year_1)
        self.light_button_3.clicked.connect(self.Light_year_2)
        self.convert_button.clicked.connect(self.Convert_Into)

        self.show()
# ------------------------------------------ start -------------------------------------- #
    # define some colors:
    def Green_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(176, 255, 208);")
    
    def Red_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(255, 178, 216);")

    # define method for back button:
    def BackToSource(self):
        from Source_window import Maryland
        self.window_land = QMainWindow()
        self.randy = Maryland()
        self.close()
    
    # define methods for temperature button:
    def Meter_1(self):
        self.from_label.setText("Meter")
    def Km_meter_1(self):
        self.from_label.setText("Kilometer")
    def Cm_meter_1(self):
        self.from_label.setText("Centimeter")
    def Mili_meter_1(self):
        self.from_label.setText("Millimeter")
    def Micro_meter_1(self):
        self.from_label.setText("Micrometer")
    def Nano_meter_1(self):
        self.from_label.setText("Nanometer")
    def Mile_1(self):
        self.from_label.setText("Mile")
    def Yard_1(self):
        self.from_label.setText("Yard")
    def Foot_1(self):
        self.from_label.setText("Foot")
    def Inch_1(self):
        self.from_label.setText("Inch")
    def Light_year_1(self):
        self.from_label.setText("Light Year")
    
    def Meter_2(self):
        self.to_label.setText("Meter")
    def Km_meter_2(self):
        self.to_label.setText("Kilometer")
    def Cm_meter_2(self):
        self.to_label.setText("Centimeter")
    def Mili_meter_2(self):
        self.to_label.setText("Millimeter")
    def Micro_meter_2(self):
        self.to_label.setText("Micrometer")
    def Nano_meter_2(self):
        self.to_label.setText("Nanometer")
    def Mile_2(self):
        self.to_label.setText("Mile")
    def Yard_2(self):
        self.to_label.setText("Yard")
    def Foot_2(self):
        self.to_label.setText("Foot")
    def Inch_2(self):
        self.to_label.setText("Inch")
    def Light_year_2(self):
        self.to_label.setText("Light Year")
    
    
    # define method for convert button:
    def Convert_Into(self):
        ent_value = self.value_line.text()
        from_value = self.from_label.text()
        to_value = self.to_label.text()
        answer = 0
        if len(ent_value) > 0:
            try:
                ent_value = float(ent_value)
                if from_value == "Meter":
                    if to_value == "Meter":
                        answer = ent_value
                    elif to_value == "Kilometer":
                        answer = ent_value / 1000
                    elif to_value == "Centimeter":
                        answer = ent_value * 100
                    elif to_value == "Millimeter":
                        answer = ent_value * 1000
                    elif to_value == "Micrometer":
                        answer = ent_value * (10**6)
                    elif to_value == "Nanometer":
                        answer = ent_value * (10**9)
                    elif to_value == "Mile":
                        answer = ent_value / 1609.35
                    elif to_value == "Yard":
                        answer = ent_value * 1.0936132983
                    elif to_value == "Foot":
                        answer = ent_value * 3.280839895
                    elif to_value == "Inch":
                        answer = ent_value * 39.37007874
                    elif to_value == "Light Year":
                        answer = (ent_value * 1.05702341) / (10**16)
                
                elif from_value == "Kilometer":
                    if to_value == "Meter":
                        answer = ent_value * 1000
                    elif to_value == "Kilometer":
                        answer = ent_value
                    elif to_value == "Centimeter":
                        answer = ent_value * (10**5)
                    elif to_value == "Millimeter":
                        answer = ent_value * (10**6)
                    elif to_value == "Micrometer":
                        answer = ent_value * (10**9)
                    elif to_value == "Nanometer":
                        answer = ent_value * (10**12)
                    elif to_value == "Mile":
                        answer = ent_value * 0.6213688756
                    elif to_value == "Yard":
                        answer = ent_value * 1093.6132983
                    elif to_value == "Foot":
                        answer = ent_value * 3280.839895
                    elif to_value == "Inch":
                        answer = ent_value * 39370.07874
                    elif to_value == "Light Year":
                        answer = (ent_value * 1.05702341) / (10**13)

                elif from_value == "Centimeter":
                    if to_value == "Meter":
                        answer = ent_value * 0.01
                    elif to_value == "Kilometer":
                        answer = ent_value * 0.00001
                    elif to_value == "Centimeter":
                        answer = ent_value
                    elif to_value == "Millimeter":
                        answer = ent_value * 10
                    elif to_value == "Micrometer":
                        answer = ent_value * 10000
                    elif to_value == "Nanometer":
                        answer = ent_value * (10**7)
                    elif to_value == "Mile":
                        answer = ent_value * 0.0000062137
                    elif to_value == "Yard":
                        answer = ent_value * 0.010936133
                    elif to_value == "Foot":
                        answer = ent_value * 0.032808399
                    elif to_value == "Inch":
                        answer = ent_value * 0.3937007874
                    elif to_value == "Light Year":
                        answer = (ent_value * 1.05702341) / (10**18)

                elif from_value == "Millimeter":
                    if to_value == "Meter":
                        answer = ent_value * 0.001
                    elif to_value == "Kilometer":
                        answer = ent_value / (10**6)
                    elif to_value == "Centimeter":
                        answer = ent_value * 0.1
                    elif to_value == "Millimeter":
                        answer = ent_value
                    elif to_value == "Micrometer":
                        answer = ent_value * 1000
                    elif to_value == "Nanometer":
                        answer = ent_value * (10**6)
                    elif to_value == "Mile":
                        answer = (ent_value * 6.21371192) / (10**7)
                    elif to_value == "Yard":
                        answer = ent_value * 0.0010936133
                    elif to_value == "Foot":
                        answer = ent_value * 0.0032808399
                    elif to_value == "Inch":
                        answer = ent_value * 0.0393700787
                    elif to_value == "Light Year":
                        answer = (ent_value * 1.05702341) / (10**19)

                elif from_value == "Micrometer":
                    if to_value == "Meter":
                        answer = ent_value / (10**6)
                    elif to_value == "Kilometer":
                        answer = ent_value / (10**9)
                    elif to_value == "Centimeter":
                        answer = ent_value * 0.0001
                    elif to_value == "Millimeter":
                        answer = ent_value * 0.001
                    elif to_value == "Micrometer":
                        answer = ent_value
                    elif to_value == "Nanometer":
                        answer = ent_value * 1000
                    elif to_value == "Mile":
                        answer = (ent_value * 6.21371192) / (10**10)
                    elif to_value == "Yard":
                        answer = (ent_value * 1.0936133) / (10**6)
                    elif to_value == "Foot":
                        answer = (ent_value * 3.2808399) / (10**6)
                    elif to_value == "Inch":
                        answer = (ent_value * 3.93700787) / (10**5)
                    elif to_value == "Light Year":
                        answer = (ent_value * 1.05702341) / (10**22)

                elif from_value == "Nanometer":
                    if to_value == "Meter":
                        answer = ent_value / (10**9)
                    elif to_value == "Kilometer":
                        answer = ent_value / (10**12)
                    elif to_value == "Centimeter":
                        answer = ent_value / (10**7)
                    elif to_value == "Millimeter":
                        answer = ent_value / (10**6)
                    elif to_value == "Micrometer":
                        answer = ent_value * 0.001
                    elif to_value == "Nanometer":
                        answer = ent_value
                    elif to_value == "Mile":
                        answer = (ent_value * 6.21371192) / (10**13)
                    elif to_value == "Yard":
                        answer = (ent_value * 1.0936133) / (10**9)
                    elif to_value == "Foot":
                        answer = (ent_value * 3.2808399) / (10**9)
                    elif to_value == "Inch":
                        answer = (ent_value * 3.93700787) / (10**8)
                    elif to_value == "Light Year":
                        answer = (ent_value * 1.05702341) / (10**25)

                elif from_value == "Mile":
                    if to_value == "Meter":
                        answer = ent_value * 1609.44
                    elif to_value == "Kilometer":
                        answer = ent_value * 1.609344
                    elif to_value == "Centimeter":
                        answer = ent_value * 160934.4
                    elif to_value == "Millimeter":
                        answer = ent_value * 1609344
                    elif to_value == "Micrometer":
                        answer = ent_value * 1609344 * (10**3)
                    elif to_value == "Nanometer":
                        answer = ent_value * 1609344 * (10**6)
                    elif to_value == "Mile":
                        answer = ent_value
                    elif to_value == "Yard":
                        answer = ent_value * 1760
                    elif to_value == "Foot":
                        answer = ent_value * 5280
                    elif to_value == "Inch":
                        answer = ent_value * 63360
                    elif to_value == "Light Year":
                        answer = (ent_value * 1.70111428) / (10**13)

                elif from_value == "Yard":
                    if to_value == "Meter":
                        answer = ent_value * 0.9144
                    elif to_value == "Kilometer":
                        answer = ent_value * 0.0009144
                    elif to_value == "Centimeter":
                        answer = ent_value * 91.44
                    elif to_value == "Millimeter":
                        answer = ent_value * 914.4
                    elif to_value == "Micrometer":
                        answer = ent_value * 914400
                    elif to_value == "Nanometer":
                        answer = ent_value * 914400 * (10**3)
                    elif to_value == "Mile":
                        answer = ent_value * 0.000568181818
                    elif to_value == "Yard":
                        answer = ent_value
                    elif to_value == "Foot":
                        answer = ent_value * 3
                    elif to_value == "Inch":
                        answer = ent_value * 36
                    elif to_value == "Light Year":
                        answer = (ent_value * 9.66542207) / (10**17)

                elif from_value == "Foot":
                    if to_value == "Meter":
                        answer = ent_value * 0.3048
                    elif to_value == "Kilometer":
                        answer = ent_value * 0.0003048
                    elif to_value == "Centimeter":
                        answer = ent_value * 30.48
                    elif to_value == "Millimeter":
                        answer = ent_value * 304.8
                    elif to_value == "Micrometer":
                        answer = ent_value * 304800
                    elif to_value == "Nanometer":
                        answer = ent_value * 304800 * (10**3)
                    elif to_value == "Mile":
                        answer = ent_value * 0.000189393939
                    elif to_value == "Yard":
                        answer = ent_value * 0.333333333
                    elif to_value == "Foot":
                        answer = ent_value
                    elif to_value == "Inch":
                        answer = ent_value * 12
                    elif to_value == "Light Year":
                        answer = (ent_value * 3.22180736) / (10**17)

                elif from_value == "Inch":
                    if to_value == "Meter":
                        answer = ent_value * 0.0254
                    elif to_value == "Kilometer":
                        answer = (ent_value * 2.54) / (10**5)
                    elif to_value == "Centimeter":
                        answer = ent_value * 2.54
                    elif to_value == "Millimeter":
                        answer = ent_value * 25.4
                    elif to_value == "Micrometer":
                        answer = ent_value * 25400
                    elif to_value == "Nanometer":
                        answer = ent_value * 25400 * (10**3)
                    elif to_value == "Mile":
                        answer = (ent_value * 1.57828283) / (10**5)
                    elif to_value == "Yard":
                        answer = ent_value * 0.0277777778
                    elif to_value == "Foot":
                        answer = ent_value * 0.0833333333
                    elif to_value == "Inch":
                        answer = ent_value
                    elif to_value == "Light Year":
                        answer = (ent_value * 2.68483946) / (10**18)

                elif from_value == "Light Year":
                    if to_value == "Meter":
                        answer = ent_value * 9.4605284 * (10**15)
                    elif to_value == "Kilometer":
                        answer = ent_value * 9.4605284 * (10**12)
                    elif to_value == "Centimeter":
                        answer = ent_value * 9.4605284 * (10**17)
                    elif to_value == "Millimeter":
                        answer = ent_value * 9.4605284 * (10**18)
                    elif to_value == "Micrometer":
                        answer = ent_value * 9.4605284 * (10**21)
                    elif to_value == "Nanometer":
                        answer = ent_value * 9.4605284 * (10**24)
                    elif to_value == "Mile":
                        answer = ent_value * 5.87849981 * (10**12)
                    elif to_value == "Yard":
                        answer = ent_value * 1.03461597 * (10**16)
                    elif to_value == "Foot":
                        answer = ent_value * 3.1038479 * (10**16)
                    elif to_value == "Inch":
                        answer = ent_value * 3.72461748 * (10**17)
                    elif to_value == "Light Year":
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
    bat = Batman()
    sys.exit(app.exec_())