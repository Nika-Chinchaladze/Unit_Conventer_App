from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QLineEdit
from PyQt5 import uic

class NinjaTurtle(QMainWindow):
    def __init__(self):
        super(NinjaTurtle, self).__init__()

        uic.loadUi("volume.ui", self)

        # define content:
        self.volume_label = self.findChild(QLabel, "volume_label")
        self.from_label = self.findChild(QLabel, "from_label")
        self.to_label = self.findChild(QLabel, "to_label")
        self.answer_label = self.findChild(QLabel, "answer_label")
        # --------------------------------------------------------------- #
        self.meter_button = self.findChild(QPushButton, "meter_button")
        self.km_button = self.findChild(QPushButton, "km_button")
        self.cm_button = self.findChild(QPushButton, "cm_button")
        self.mili_button = self.findChild(QPushButton, "mili_button")
        self.liter_button = self.findChild(QPushButton, "liter_button")
        self.ml_button = self.findChild(QPushButton, "ml_button")
        self.gallon_button = self.findChild(QPushButton, "gallon_button")
        self.quart_button = self.findChild(QPushButton, "quart_button")
        self.pint_button = self.findChild(QPushButton, "pint_button")
        self.cup_button = self.findChild(QPushButton, "cup_button")
        self.fluid_button = self.findChild(QPushButton, "fluid_button")
        self.table_button = self.findChild(QPushButton, "table_button")
        self.tea_button = self.findChild(QPushButton, "tea_button")
        self.imp_gall_button = self.findChild(QPushButton, "imp_gall_button")
        self.imp_quart_button = self.findChild(QPushButton, "imp_quart_button")
        self.imp_pint_button = self.findChild(QPushButton, "imp_pint_button")
        self.imp_fluid_button = self.findChild(QPushButton, "imp_fluid_button")
        self.imp_table_button = self.findChild(QPushButton, "imp_table_button")
        self.imp_tea_button = self.findChild(QPushButton, "imp_tea_button")
        self.cubic_button = self.findChild(QPushButton, "cubic_button")
        self.yard_button = self.findChild(QPushButton, "yard_button")
        self.foot_button = self.findChild(QPushButton, "foot_button")
        self.inch_button = self.findChild(QPushButton, "inch_button")
        # --------------------------------------------------------------- #
        self.meter_button_2 = self.findChild(QPushButton, "meter_button_2")
        self.km_button_2 = self.findChild(QPushButton, "km_button_2")
        self.cm_button_2 = self.findChild(QPushButton, "cm_button_2")
        self.mili_button_2 = self.findChild(QPushButton, "mili_button_2")
        self.liter_button_2 = self.findChild(QPushButton, "liter_button_2")
        self.ml_button_2 = self.findChild(QPushButton, "ml_button_2")
        self.gallon_button_2 = self.findChild(QPushButton, "gallon_button_2")
        self.quart_button_2 = self.findChild(QPushButton, "quart_button_2")
        self.pint_button_2 = self.findChild(QPushButton, "pint_button_2")
        self.cup_button_2 = self.findChild(QPushButton, "cup_button_2")
        self.fluid_button_2 = self.findChild(QPushButton, "fluid_button_2")
        self.table_button_2 = self.findChild(QPushButton, "table_button_2")
        self.tea_button_2 = self.findChild(QPushButton, "tea_button_2")
        self.imp_gall_button_2 = self.findChild(QPushButton, "imp_gall_button_2")
        self.imp_quart_button_2 = self.findChild(QPushButton, "imp_quart_button_2")
        self.imp_pint_button_2 = self.findChild(QPushButton, "imp_pint_button_2")
        self.imp_fluid_button_2 = self.findChild(QPushButton, "imp_fluid_button_2")
        self.imp_table_button_2 = self.findChild(QPushButton, "imp_table_button_2")
        self.imp_tea_button_2 = self.findChild(QPushButton, "imp_tea_button_2")
        self.cubic_button_2 = self.findChild(QPushButton, "cubic_button_2")
        self.yard_button_2 = self.findChild(QPushButton, "yard_button_2")
        self.foot_button_2 = self.findChild(QPushButton, "foot_button_2")
        self.inch_button_2 = self.findChild(QPushButton, "inch_button_2")
        # --------------------------------------------------------------- #
        self.back_button = self.findChild(QPushButton, "back_button")
        self.convert_button = self.findChild(QPushButton, "convert_button")
        # --------------------------------------------------------------- #
        self.line_1 = self.findChild(QFrame, "line_1")
        self.line_2 = self.findChild(QFrame, "line_2")
        self.frame_1 = self.findChild(QFrame, "frame_1")
        self.frame_2 = self.findChild(QFrame, "frame_2")
        self.frame_3 = self.findChild(QFrame, "frame_3")
        self.frame_4 = self.findChild(QFrame, "frame_4")
        # --------------------------------------------------------------- #
        self.value_line = self.findChild(QLineEdit, "value_line")
        self.value_line.setPlaceholderText("value")

        # call defined functions from here:
        self.back_button.clicked.connect(self.ReturnBackToSource)
        self.convert_button.clicked.connect(self.Convert_Into)
        self.meter_button.clicked.connect(self.Meter_1)
        self.meter_button_2.clicked.connect(self.Meter_2)
        self.km_button.clicked.connect(self.Km_meter_1)
        self.km_button_2.clicked.connect(self.Km_meter_2)
        self.cm_button.clicked.connect(self.Cm_meter_1)
        self.cm_button_2.clicked.connect(self.Cm_meter_2)
        self.mili_button.clicked.connect(self.Mili_meter_1)
        self.mili_button_2.clicked.connect(self.Mili_meter_2)
        self.liter_button.clicked.connect(self.Liter_1)
        self.liter_button_2.clicked.connect(self.Liter_2)
        self.ml_button.clicked.connect(self.Milliliter_1)
        self.ml_button_2.clicked.connect(self.Milliliter_2)
        self.gallon_button.clicked.connect(self.US_gallon_1)
        self.gallon_button_2.clicked.connect(self.US_gallon_2)
        self.quart_button.clicked.connect(self.US_quart_1)
        self.quart_button_2.clicked.connect(self.US_quart_2)
        self.pint_button.clicked.connect(self.US_pint_1)
        self.pint_button_2.clicked.connect(self.US_pint_2)
        self.cup_button.clicked.connect(self.US_cup_1)
        self.cup_button_2.clicked.connect(self.US_cup_2)
        self.fluid_button.clicked.connect(self.US_fluid_1)
        self.fluid_button_2.clicked.connect(self.US_fluid_2)
        self.table_button.clicked.connect(self.US_table_1)
        self.table_button_2.clicked.connect(self.US_table_2)
        self.tea_button.clicked.connect(self.US_tea_1)
        self.tea_button_2.clicked.connect(self.US_tea_2)
        self.imp_gall_button.clicked.connect(self.IMP_gallon_1)
        self.imp_gall_button_2.clicked.connect(self.IMP_gallon_2)
        self.imp_quart_button.clicked.connect(self.IMP_quart_1)
        self.imp_quart_button_2.clicked.connect(self.IMP_quart_2)
        self.imp_pint_button.clicked.connect(self.IMP_pint_1)
        self.imp_pint_button_2.clicked.connect(self.IMP_pint_2)
        self.imp_fluid_button.clicked.connect(self.IMP_fluid_1)
        self.imp_fluid_button_2.clicked.connect(self.IMP_fluid_2)
        self.imp_table_button.clicked.connect(self.IMP_table_1)
        self.imp_table_button_2.clicked.connect(self.IMP_table_2)
        self.imp_tea_button.clicked.connect(self.IMP_tea_1)
        self.imp_tea_button_2.clicked.connect(self.IMP_tea_2)
        self.cubic_button.clicked.connect(self.Cubic_mile_1)
        self.cubic_button_2.clicked.connect(self.Cubic_mile_2)
        self.yard_button.clicked.connect(self.Cubic_yard_1)
        self.yard_button_2.clicked.connect(self.Cubic_yard_2)
        self.foot_button.clicked.connect(self.Cubic_foot_1)
        self.foot_button_2.clicked.connect(self.Cubic_foot_2)
        self.inch_button.clicked.connect(self.Cubic_inch_1)
        self.inch_button_2.clicked.connect(self.Cubic_inch_2)
        
        

        self.show()
# ------------------------------------------ start -------------------------------------- #
    # define some colors:
    def Green_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(176, 255, 208);")
    
    def Red_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(255, 178, 216);")

    # define method for back button:
    def ReturnBackToSource(self):
        from Source_window import Maryland
        self.window_land = QMainWindow()
        self.randy = Maryland()
        self.close()
    
    # define methods for temperature button:
    def Meter_1(self):
        self.from_label.setText("Cubic Meter")
    def Km_meter_1(self):
        self.from_label.setText("Cubic Kilometer")
    def Cm_meter_1(self):
        self.from_label.setText("Cubic Centimeter")
    def Mili_meter_1(self):
        self.from_label.setText("Cubic Millimeter")
    def Liter_1(self):
        self.from_label.setText("Liter")
    def Milliliter_1(self):
        self.from_label.setText("Milliliter")
    def US_gallon_1(self):
        self.from_label.setText("US Gallon")
    def US_quart_1(self):
        self.from_label.setText("US Quart")
    def US_pint_1(self):
        self.from_label.setText("US Pint")
    def US_cup_1(self):
        self.from_label.setText("US Cup")
    def US_fluid_1(self):
        self.from_label.setText("US Fluid Ounce")
    def US_table_1(self):
        self.from_label.setText("US Table Spoon")
    def US_tea_1(self):
        self.from_label.setText("US Tea Spoon")
    def IMP_gallon_1(self):
        self.from_label.setText("Imperial Gallon")
    def IMP_quart_1(self):
        self.from_label.setText("Imperial Quart")
    def IMP_pint_1(self):
        self.from_label.setText("Imperial Pint")
    def IMP_fluid_1(self):
        self.from_label.setText("Imperial Fluid Ounce")
    def IMP_table_1(self):
        self.from_label.setText("Imperial Table Spoon")
    def IMP_tea_1(self):
        self.from_label.setText("Imperial Tea Spoon")
    def Cubic_mile_1(self):
        self.from_label.setText("Cubic Mile")
    def Cubic_yard_1(self):
        self.from_label.setText("Cubic Yard")
    def Cubic_foot_1(self):
        self.from_label.setText("Cubic Foot")
    def Cubic_inch_1(self):
        self.from_label.setText("Cubic Inch")

    def Meter_2(self):
        self.to_label.setText("Cubic Meter")
    def Km_meter_2(self):
        self.to_label.setText("Cubic Kilometer")
    def Cm_meter_2(self):
        self.to_label.setText("Cubic Centimeter")
    def Mili_meter_2(self):
        self.to_label.setText("Cubic Millimeter")
    def Liter_2(self):
        self.to_label.setText("Liter")
    def Milliliter_2(self):
        self.to_label.setText("Milliliter")
    def US_gallon_2(self):
        self.to_label.setText("US Gallon")
    def US_quart_2(self):
        self.to_label.setText("US Quart")
    def US_pint_2(self):
        self.to_label.setText("US Pint")
    def US_cup_2(self):
        self.to_label.setText("US Cup")
    def US_fluid_2(self):
        self.to_label.setText("US Fluid Ounce")
    def US_table_2(self):
        self.to_label.setText("US Table Spoon")
    def US_tea_2(self):
        self.to_label.setText("US Tea Spoon")
    def IMP_gallon_2(self):
        self.to_label.setText("Imperial Gallon")
    def IMP_quart_2(self):
        self.to_label.setText("Imperial Quart")
    def IMP_pint_2(self):
        self.to_label.setText("Imperial Pint")
    def IMP_fluid_2(self):
        self.to_label.setText("Imperial Fluid Ounce")
    def IMP_table_2(self):
        self.to_label.setText("Imperial Table Spoon")
    def IMP_tea_2(self):
        self.to_label.setText("Imperial Tea Spoon")
    def Cubic_mile_2(self):
        self.to_label.setText("Cubic Mile")
    def Cubic_yard_2(self):
        self.to_label.setText("Cubic Yard")
    def Cubic_foot_2(self):
        self.to_label.setText("Cubic Foot")
    def Cubic_inch_2(self):
        self.to_label.setText("Cubic Inch")
    
    
    
    
    # define method for convert button:
    def Convert_Into(self):
        ent_value = self.value_line.text()
        from_value = self.from_label.text()
        to_value = self.to_label.text()
        answer = 0
        if len(ent_value) > 0:
            try:
                ent_value = float(ent_value)
                if from_value == "Cubic Meter":
                    if to_value == "Cubic Meter":
                        answer = ent_value
                    elif to_value == "Cubic Kilometer":
                        answer = ent_value / (10**9)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * (10**6)
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * (10**9)
                    elif to_value == "Liter":
                        answer = ent_value * (10**3)
                    elif to_value == "Milliliter":
                        answer = ent_value * (10**6)
                    elif to_value == "US Gallon":
                        answer = ent_value * 264.172
                    elif to_value == "US Quart":
                        answer = ent_value * 1056.69
                    elif to_value == "US Pint":
                        answer = ent_value * 2113.38
                    elif to_value == "US Cup":
                        answer = ent_value * 4226.75
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 33814
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 67628
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 202884
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 219.969
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 879.877
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 1759.75
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 35195.1
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 56312.1
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 168936
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 2.39913) / (10**10)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 1.30795
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 35.3147
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 61023.7
                
                elif from_value == "Cubic Kilometer":
                    if to_value == "Cubic Meter":
                        answer = ent_value * (10**9)
                    elif to_value == "Cubic Kilometer":
                        answer = ent_value
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * (10**15)
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * (10**18)
                    elif to_value == "Liter":
                        answer = ent_value * (10**12)
                    elif to_value == "Milliliter":
                        answer = ent_value * (10**15)
                    elif to_value == "US Gallon":
                        answer = ent_value * 2.642 * (10**11)
                    elif to_value == "US Quart":
                        answer = ent_value * 1.057 * (10**12)
                    elif to_value == "US Pint":
                        answer = ent_value * 2.113 * (10**12)
                    elif to_value == "US Cup":
                        answer = ent_value * 4.227 * (10**12)
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 3.381 * (10**13)
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 6.763 * (10**13)
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 2.029 * (10**14)
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 2.2 * (10**11)
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 8.799 * (10**11)
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 1.76 * (10**12)
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 3.52 * (10**13)
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 5.631 * (10**13)
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 1.689 * (10**14)
                    elif to_value == "Cubic Mile":
                        answer = ent_value * 0.239913
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 1.308 * (10**9)
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 3.531 * (10**10)
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 6.102 * (10**13)


                elif from_value == "Cubic Centimeter":
                    if to_value == "Cubic Meter":
                        answer = ent_value / (10**6)
                    elif to_value == "Cubic Kilometer":
                        answer = ent_value / (10**15)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * (10**3)
                    elif to_value == "Liter":
                        answer = ent_value * 0.001
                    elif to_value == "Milliliter":
                        answer = ent_value
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.000264172
                    elif to_value == "US Quart":
                        answer = ent_value * 0.00105669
                    elif to_value == "US Pint":
                        answer = ent_value * 0.00211338
                    elif to_value == "US Cup":
                        answer = ent_value * 0.00422675
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 0.033814
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 0.067628
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 0.202884
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.000219969
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.000879877
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 0.00175975
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 0.0351951
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 0.0563121
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 0.168936
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 2.39913) / (10**16)
                    elif to_value == "Cubic Yard":
                        answer = (ent_value * 1.308) / (10**6)
                    elif to_value == "Cubic Foot":
                        answer = (ent_value * 3.531) / (10**5)
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 0.0610237

                elif from_value == "Cubic Millimeter":
                    if to_value == "Cubic Meter":
                        answer = ent_value / (10**9)
                    elif to_value == "Cubic Kilometer":
                        answer = ent_value / (10**18)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 0.001
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value
                    elif to_value == "Liter":
                        answer = ent_value / (10**6)
                    elif to_value == "Milliliter":
                        answer = ent_value * 0.001
                    elif to_value == "US Gallon":
                        answer = (ent_value * 2.642) / (10**7)
                    elif to_value == "US Quart":
                        answer = (ent_value * 1.057) / (10**6)
                    elif to_value == "US Pint":
                        answer = (ent_value * 2.113) / (10**6)
                    elif to_value == "US Cup":
                        answer = (ent_value * 4.227) / (10**6)
                    elif to_value == "US Fluid Ounce":
                        answer = (ent_value * 3.381) / (10**5)
                    elif to_value == "US Table Spoon":
                        answer = (ent_value * 6.763) / (10**5)
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 0.000202884
                    elif to_value == "Imperial Gallon":
                        answer = (ent_value * 2.2) / (10**7)
                    elif to_value == "Imperial Quart":
                        answer = (ent_value * 8.799) / (10**7)
                    elif to_value == "Imperial Pint":
                        answer = (ent_value * 1.76) / (10**6)
                    elif to_value == "Imperial Fluid Ounce":
                        answer = (ent_value * 3.52) / (10**5)
                    elif to_value == "Imperial Table Spoon":
                        answer = (ent_value * 5.631) / (10**5)
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 0.000168936
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 2.39913) / (10**19)
                    elif to_value == "Cubic Yard":
                        answer = (ent_value * 1.308) / (10**9)
                    elif to_value == "Cubic Foot":
                        answer = (ent_value * 3.531) / (10**8)
                    elif to_value == "Cubic Inch":
                        answer = (ent_value * 6.102) / (10**5)

                elif from_value == "Liter":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.001
                    elif to_value == "Cubic Kilometer":
                        answer = ent_value / (10**12)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * (10**3)
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * (10**6)
                    elif to_value == "Liter":
                        answer = ent_value
                    elif to_value == "Milliliter":
                        answer = ent_value * (10**3)
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.264172
                    elif to_value == "US Quart":
                        answer = ent_value * 1.05669
                    elif to_value == "US Pint":
                        answer = ent_value * 2.11338
                    elif to_value == "US Cup":
                        answer = ent_value * 4.22675
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 33.814
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 67.628
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 202.884
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.219969
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.879877
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 1.75975
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 35.1951
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 56.3121
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 168.936
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 2.39913) / (10**13)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.001308
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.03531
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 61.0237

                elif from_value == "Milliliter":
                    if to_value == "Cubic Meter":
                        answer = ent_value / (10**6)
                    elif to_value == "Cubic Kilometer":
                        answer = ent_value / (10**15)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 1000
                    elif to_value == "Liter":
                        answer = ent_value / (10**3)
                    elif to_value == "Milliliter":
                        answer = ent_value
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.0002642
                    elif to_value == "US Quart":
                        answer = ent_value * 0.001057
                    elif to_value == "US Pint":
                        answer = ent_value * 0.002113
                    elif to_value == "US Cup":
                        answer = ent_value * 0.004227
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 0.033814
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 0.06763
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 0.202884
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.000219969
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.0008799
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 0.00176
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 0.0352
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 0.05631
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 0.168936
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 2.39913) / (10**16)
                    elif to_value == "Cubic Yard":
                        answer = (ent_value * 1.308) / (10**6)
                    elif to_value == "Cubic Foot":
                        answer = (ent_value * 3.531) / (10**5)
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 0.0610237

                elif from_value == "US Gallon":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.00378541
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 3.78541) / (10**12)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 3785.41
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 3.785 * (10**6)
                    elif to_value == "Liter":
                        answer = ent_value * 3.78541
                    elif to_value == "Milliliter":
                        answer = ent_value * 3785.41
                    elif to_value == "US Gallon":
                        answer = ent_value
                    elif to_value == "US Quart":
                        answer = ent_value * 4
                    elif to_value == "US Pint":
                        answer = ent_value * 8
                    elif to_value == "US Cup":
                        answer = ent_value * 16
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 128
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 256
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 768
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.832674
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 3.3307
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 6.66139
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 133.228
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 213.165
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 639.494
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 9.08169) / (10**13)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.00495113
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.133681
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 231

                elif from_value == "US Quart":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.000946353
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 9.46353) / (10**13)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 946.353
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 946353
                    elif to_value == "Liter":
                        answer = ent_value * 0.946353
                    elif to_value == "Milliliter":
                        answer = ent_value * 946.353
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.25
                    elif to_value == "US Quart":
                        answer = ent_value
                    elif to_value == "US Pint":
                        answer = ent_value * 2
                    elif to_value == "US Cup":
                        answer = ent_value * 4
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 32
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 64
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 192
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.208169
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.832674
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 1.66535
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 33.307
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 53.2911
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 159.873
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 2.27042) / (10**13)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.00123778
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.0334201
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 57.75

                elif from_value == "US Pint":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.000473176
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 4.73176) / (10**13)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 473.176
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 473176
                    elif to_value == "Liter":
                        answer = ent_value * 0.473176
                    elif to_value == "Milliliter":
                        answer = ent_value * 473.176
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.125
                    elif to_value == "US Quart":
                        answer = ent_value * 0.5
                    elif to_value == "US Pint":
                        answer = ent_value
                    elif to_value == "US Cup":
                        answer = ent_value * 2
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 16
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 32
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 96
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.104084
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.416337
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 0.832674
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 16.6535
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 26.6456
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 79.9367
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 1.13521) / (10**13)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.000618891
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.0167101
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 28.875

                elif from_value == "US Cup":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.000236588
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 2.36588) / (10**13)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 236.588
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 236588
                    elif to_value == "Liter":
                        answer = ent_value * 0.236588
                    elif to_value == "Milliliter":
                        answer = ent_value * 236.588
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.0625
                    elif to_value == "US Quart":
                        answer = ent_value * 0.25
                    elif to_value == "US Pint":
                        answer = ent_value * 0.5
                    elif to_value == "US Cup":
                        answer = ent_value
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 8
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 16
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 48
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.0520421
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.208169
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 0.416337
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 8.32674
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 13.3228
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 39.9683
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 5.67605) / (10**14)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.000309446
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.00835503
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 14.4375

                elif from_value == "US Fluid Ounce":
                    if to_value == "Cubic Meter":
                        answer = (ent_value * 2.95735) / (10**5)
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 2.95735) / (10**14)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 29.5735
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 29573.5
                    elif to_value == "Liter":
                        answer = ent_value * 0.0295735
                    elif to_value == "Milliliter":
                        answer = ent_value * 29.5735
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.0078125
                    elif to_value == "US Quart":
                        answer = ent_value * 0.03125
                    elif to_value == "US Pint":
                        answer = ent_value * 0.0625
                    elif to_value == "US Cup":
                        answer = ent_value * 0.125
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 2
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 6
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.00650527
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.0260211
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 0.0520421
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 1.0408422403
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 1.66535
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 4.99604
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 7.09507) / (10**15)
                    elif to_value == "Cubic Yard":
                        answer = (ent_value * 3.86807) / (10**5)
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.00104438
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 1.80469

                elif from_value == "US Table Spoon":
                    if to_value == "Cubic Meter":
                        answer = (ent_value * 1.47868) / (10**5)
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 1.47868) / (10**14)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 14.7868
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 14786.8
                    elif to_value == "Liter":
                        answer = ent_value * 0.0147868
                    elif to_value == "Milliliter":
                        answer = ent_value * 14.7868
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.00390625
                    elif to_value == "US Quart":
                        answer = ent_value * 0.015625
                    elif to_value == "US Pint":
                        answer = ent_value * 0.03125
                    elif to_value == "US Cup":
                        answer = ent_value * 0.0625
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 0.5
                    elif to_value == "US Table Spoon":
                        answer = ent_value
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 3
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.00325263
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.0130105
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 0.0260211
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 0.520421
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 0.832674
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 2.49802
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 3.54753) / (10**15)
                    elif to_value == "Cubic Yard":
                        answer = (ent_value * 1.93404) / (10**5)
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.00052219
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 0.902344

                elif from_value == "US Tea Spoon":
                    if to_value == "Cubic Meter":
                        answer = (ent_value * 4.92892) / (10**6)
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 4.92892) / (10**15)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 4.92892
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 4928.92
                    elif to_value == "Liter":
                        answer = ent_value * 0.00492892
                    elif to_value == "Milliliter":
                        answer = ent_value * 4.92892
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.00130208
                    elif to_value == "US Quart":
                        answer = ent_value * 0.00520833
                    elif to_value == "US Pint":
                        answer = ent_value * 0.0104167
                    elif to_value == "US Cup":
                        answer = ent_value * 0.0208333
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 0.166667
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 0.333333
                    elif to_value == "US Tea Spoon":
                        answer = ent_value
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.00108421
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.00433684
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 0.00867369
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 0.173474
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 0.277558
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 0.832674
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 1.18251) / (10**15)
                    elif to_value == "Cubic Yard":
                        answer = (ent_value * 6.44678) / (10**6)
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.000174063
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 0.300781

                elif from_value == "Imperial Gallon":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.00454609
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 4.54609) / (10**12)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 4546.09
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 4.546 * (10**6)
                    elif to_value == "Liter":
                        answer = ent_value * 4.54609
                    elif to_value == "Milliliter":
                        answer = ent_value * 4546.09
                    elif to_value == "US Gallon":
                        answer = ent_value * 1.20095
                    elif to_value == "US Quart":
                        answer = ent_value * 4.8038
                    elif to_value == "US Pint":
                        answer = ent_value * 9.6076
                    elif to_value == "US Cup":
                        answer = ent_value * 19.2152
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 153.722
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 307.443
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 922.33
                    elif to_value == "Imperial Gallon":
                        answer = ent_value
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 4
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 8
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 160
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 256
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 768
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 1.09066) / (10**12)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.00594606
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.160544
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 277.419

                elif from_value == "Imperial Quart":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.00113652
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 1.13652) / (10**12)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 1136.52
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 1.13652 * (10**6)
                    elif to_value == "Liter":
                        answer = ent_value * 1.13652
                    elif to_value == "Milliliter":
                        answer = ent_value * 1136.52
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.300237
                    elif to_value == "US Quart":
                        answer = ent_value * 1.20095
                    elif to_value == "US Pint":
                        answer = ent_value * 2.4019
                    elif to_value == "US Cup":
                        answer = ent_value * 4.8038
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 38.4304
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 76.8608
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 230.582
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.25
                    elif to_value == "Imperial Quart":
                        answer = ent_value
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 2
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 40
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 64
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 192
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 2.72666) / (10**13)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.00148652
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.0401359
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 69.3549

                elif from_value == "Imperial Pint":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.000568261
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 5.68261) / (10**13)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 568.261
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 568261
                    elif to_value == "Liter":
                        answer = ent_value * 0.568261
                    elif to_value == "Milliliter":
                        answer = ent_value * 568.261
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.150119
                    elif to_value == "US Quart":
                        answer = ent_value * 0.600475
                    elif to_value == "US Pint":
                        answer = ent_value * 1.20095
                    elif to_value == "US Cup":
                        answer = ent_value * 2.4019
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 19.2152
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 38.4304
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 115.291
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.125
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.5
                    elif to_value == "Imperial Pint":
                        answer = ent_value
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 20
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 32
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 96
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 1.36333) / (10**13)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.000743258
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.020068
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 34.6774

                elif from_value == "Imperial Fluid Ounce":
                    if to_value == "Cubic Meter":
                        answer = (ent_value * 2.84131) / (10**5)
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 2.84131) / (10**14)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 28.4131
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 28413.1
                    elif to_value == "Liter":
                        answer = ent_value * 0.0284131
                    elif to_value == "Milliliter":
                        answer = ent_value * 28.4131
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.00750594
                    elif to_value == "US Quart":
                        answer = ent_value * 0.0300237
                    elif to_value == "US Pint":
                        answer = ent_value * 0.0600475
                    elif to_value == "US Cup":
                        answer = ent_value * 0.120095
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 0.9607603932
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 1.9215207864
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 5.7645623592
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.00625
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.025
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 0.05
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 1.6
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 4.8
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 6.816659189) / (10**15)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.0000371629
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.0010033978
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 1.7338714549

                elif from_value == "Imperial Table Spoon":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.0000177582
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 1.775816406) / (10**14)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 17.758164063
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 17758.16406
                    elif to_value == "Liter":
                        answer = ent_value * 0.0177581641
                    elif to_value == "Milliliter":
                        answer = ent_value * 17.75816406
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.0046912129
                    elif to_value == "US Quart":
                        answer = ent_value * 0.0187648514
                    elif to_value == "US Pint":
                        answer = ent_value * 0.0375297029
                    elif to_value == "US Cup":
                        answer = ent_value * 0.0750594057
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 0.6004752457
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 1.2009504915
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 3.6028514745
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.00390625
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.015625
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 0.03125
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 0.625
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 3
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 4.260411993) / (10**15)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.0000232268
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.0006271236
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 1.0836696593

                elif from_value == "Imperial Tea Spoon":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.0000059194
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 5.91938802) / (10**15)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 5.91938802
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 5919.3880208
                    elif to_value == "Liter":
                        answer = ent_value * 0.005919388
                    elif to_value == "Milliliter":
                        answer = ent_value * 5.9193880208
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.0015637376
                    elif to_value == "US Quart":
                        answer = ent_value * 0.0062549505
                    elif to_value == "US Pint":
                        answer = ent_value * 0.012509901
                    elif to_value == "US Cup":
                        answer = ent_value * 0.0250198019
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 0.2001584152
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 0.4003168305
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 1.2009504915
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.0013020833
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.0052083333
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 0.0104166667
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 0.2083333333
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 0.3333333333
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 1.420137331) / (10**15)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.0000077423
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.0002090412
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 0.3612232198

                elif from_value == "Cubic Mile":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 4168180000
                    elif to_value == "Cubic Kilometer":
                        answer = ent_value * 4.16818
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 4.16818 * (10**15)
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 4.16818 * (10**18)
                    elif to_value == "Liter":
                        answer = ent_value * 4.16818 * (10**12)
                    elif to_value == "Milliliter":
                        answer = ent_value * 4.16818 * (10**15)
                    elif to_value == "US Gallon":
                        answer = ent_value * 1.101 * (10**12)
                    elif to_value == "US Quart":
                        answer = ent_value * 4.404 * (10**12)
                    elif to_value == "US Pint":
                        answer = ent_value * 8.809 * (10**12)
                    elif to_value == "US Cup":
                        answer = ent_value * 1.762 * (10**13)
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 1.409 * (10**14)
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 2.819 * (10**14)
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 8.457 * (10**14)
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 9.169 * (10**11)
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 3.667 * (10**12)
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 7.335 * (10**12)
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 1.467 * (10**14)
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 2.347 * (10**14)
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 7.042 * (10**14)
                    elif to_value == "Cubic Mile":
                        answer = ent_value
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 5.452 * (10**9)
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 1.472 * (10**11)
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 2.544 * (10**14)

                elif from_value == "Cubic Yard":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.764555
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 7.64555) / (10**10)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 764555
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 7.64555 * (10**8)
                    elif to_value == "Liter":
                        answer = ent_value * 764.555
                    elif to_value == "Milliliter":
                        answer = ent_value * 764555
                    elif to_value == "US Gallon":
                        answer = ent_value * 201.974
                    elif to_value == "US Quart":
                        answer = ent_value * 807.896
                    elif to_value == "US Pint":
                        answer = ent_value * 1615.79
                    elif to_value == "US Cup":
                        answer = ent_value * 3231.58
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 25852.7
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 51705.4
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 155116
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 168.179
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 672.714
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 1345.43
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 26908.6
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 43053.7
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 129161
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 1.83426) / (10**10)
                    elif to_value == "Cubic Yard":
                        answer = ent_value
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 27
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 46656

                elif from_value == "Cubic Foot":
                    if to_value == "Cubic Meter":
                        answer = ent_value * 0.0283168
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 2.83168) / (10**11)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 28316.8
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 2.83168 * (10**7)
                    elif to_value == "Liter":
                        answer = ent_value * 28.3168
                    elif to_value == "Milliliter":
                        answer = ent_value * 28316.8
                    elif to_value == "US Gallon":
                        answer = ent_value * 7.48052
                    elif to_value == "US Quart":
                        answer = ent_value * 29.9221
                    elif to_value == "US Pint":
                        answer = ent_value * 59.8442
                    elif to_value == "US Cup":
                        answer = ent_value * 119.688
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 957.506
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 1915.01
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 5745.04
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 6.22884
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 24.9153
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 49.8307
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 996.614
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 1594.58
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 4783.74
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 6.79357) / (10**12)
                    elif to_value == "Cubic Yard":
                        answer = ent_value * 0.037037
                    elif to_value == "Cubic Foot":
                        answer = ent_value
                    elif to_value == "Cubic Inch":
                        answer = ent_value * 1728

                elif from_value == "Cubic Inch":
                    if to_value == "Cubic Meter":
                        answer = (ent_value * 1.63871) / (10**5)
                    elif to_value == "Cubic Kilometer":
                        answer = (ent_value * 1.63871) / (10**14)
                    elif to_value == "Cubic Centimeter":
                        answer = ent_value * 16.3871
                    elif to_value == "Cubic Millimeter":
                        answer = ent_value * 16387.1
                    elif to_value == "Liter":
                        answer = ent_value * 0.0163871
                    elif to_value == "Milliliter":
                        answer = ent_value * 16.3871
                    elif to_value == "US Gallon":
                        answer = ent_value * 0.004329
                    elif to_value == "US Quart":
                        answer = ent_value * 0.017316
                    elif to_value == "US Pint":
                        answer = ent_value * 0.034632
                    elif to_value == "US Cup":
                        answer = ent_value * 0.0692641
                    elif to_value == "US Fluid Ounce":
                        answer = ent_value * 0.554113
                    elif to_value == "US Table Spoon":
                        answer = ent_value * 1.10823
                    elif to_value == "US Tea Spoon":
                        answer = ent_value * 3.32468
                    elif to_value == "Imperial Gallon":
                        answer = ent_value * 0.00360465
                    elif to_value == "Imperial Quart":
                        answer = ent_value * 0.0144186
                    elif to_value == "Imperial Pint":
                        answer = ent_value * 0.0288372
                    elif to_value == "Imperial Fluid Ounce":
                        answer = ent_value * 0.576744
                    elif to_value == "Imperial Table Spoon":
                        answer = ent_value * 0.92279
                    elif to_value == "Imperial Tea Spoon":
                        answer = ent_value * 2.76837
                    elif to_value == "Cubic Mile":
                        answer = (ent_value * 3.93147) / (10**15)
                    elif to_value == "Cubic Yard":
                        answer = (ent_value * 2.14335) / (10**5)
                    elif to_value == "Cubic Foot":
                        answer = ent_value * 0.000578704
                    elif to_value == "Cubic Inch":
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
    ninja = NinjaTurtle()
    sys.exit(app.exec_())