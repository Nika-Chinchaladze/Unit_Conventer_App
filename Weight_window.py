from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QLineEdit
from PyQt5 import uic

class Ironman(QMainWindow):
    def __init__(self):
        super(Ironman, self).__init__()

        uic.loadUi("weight.ui", self)

        # define content:
        self.weight_label = self.findChild(QLabel, "weight_label")
        self.from_label = self.findChild(QLabel, "from_label")
        self.to_label = self.findChild(QLabel, "to_label")
        self.answer_label = self.findChild(QLabel, "answer_label")
        # --------------------------------------------------------------- #
        self.kg_button = self.findChild(QPushButton, "kg_button")
        self.gram_button = self.findChild(QPushButton, "gram_button")
        self.milli_button = self.findChild(QPushButton, "milli_button")
        self.metric_button = self.findChild(QPushButton, "metric_button")
        self.long_button = self.findChild(QPushButton, "long_button")
        self.short_button = self.findChild(QPushButton, "short_button")
        self.pound_button = self.findChild(QPushButton, "pound_button")
        self.ounce_button = self.findChild(QPushButton, "ounce_button")
        self.car_button = self.findChild(QPushButton, "car_button")
        self.atom_button = self.findChild(QPushButton, "atom_button")
        # --------------------------------------------------------------- #
        self.kg_button_2 = self.findChild(QPushButton, "kg_button_2")
        self.gram_button_2 = self.findChild(QPushButton, "gram_button_2")
        self.milli_button_2 = self.findChild(QPushButton, "milli_button_2")
        self.metric_button_2 = self.findChild(QPushButton, "metric_button_2")
        self.long_button_2 = self.findChild(QPushButton, "long_button_2")
        self.short_button_2 = self.findChild(QPushButton, "short_button_2")
        self.pound_button_2 = self.findChild(QPushButton, "pound_button_2")
        self.ounce_button_2 = self.findChild(QPushButton, "ounce_button_2")
        self.car_button_2 = self.findChild(QPushButton, "car_button_2")
        self.atom_button_2 = self.findChild(QPushButton, "atom_button_2")
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
        self.kg_button.clicked.connect(self.Kg_1)
        self.kg_button_2.clicked.connect(self.Kg_2)
        self.gram_button.clicked.connect(self.Gram_1)
        self.gram_button_2.clicked.connect(self.Gram_2)
        self.milli_button.clicked.connect(self.Milligram_1)
        self.milli_button_2.clicked.connect(self.Milligram_2)
        self.metric_button.clicked.connect(self.MetricTon_1)
        self.metric_button_2.clicked.connect(self.MetricTon_2)
        self.long_button.clicked.connect(self.LongTon_1)
        self.long_button_2.clicked.connect(self.LongTon_2)
        self.short_button.clicked.connect(self.ShortTon_1)
        self.short_button_2.clicked.connect(self.ShortTon_2)
        self.pound_button.clicked.connect(self.Pound_1)
        self.pound_button_2.clicked.connect(self.Pound_2)
        self.ounce_button.clicked.connect(self.Ounce_1)
        self.ounce_button_2.clicked.connect(self.Ounce_2)
        self.car_button.clicked.connect(self.Carrat_1)
        self.car_button_2.clicked.connect(self.Carrat_2)
        self.atom_button.clicked.connect(self.Atomic_1)
        self.atom_button_2.clicked.connect(self.Atomic_2)
        self.back_button.clicked.connect(self.BackToSourcepage)
        self.convert_button.clicked.connect(self.Convert_Into)

        self.show()
# ------------------------------------------ start -------------------------------------- #
    # define some colors:
    def Green_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(176, 255, 208);")
    
    def Red_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(255, 178, 216);")

    # define method for back button:
    def BackToSourcepage(self):
        from Source_window import Maryland
        self.window_land = QMainWindow()
        self.randy = Maryland()
        self.close()
    
    # define methods for temperature button:
    def Kg_1(self):
        self.from_label.setText("Kilogram")
    def Gram_1(self):
        self.from_label.setText("Gram")
    def Milligram_1(self):
        self.from_label.setText("Milligram")
    def MetricTon_1(self):
        self.from_label.setText("Metric Ton")
    def LongTon_1(self):
        self.from_label.setText("Long Ton")
    def ShortTon_1(self):
        self.from_label.setText("Short Ton")
    def Pound_1(self):
        self.from_label.setText("Pound")
    def Ounce_1(self):
        self.from_label.setText("Ounce")
    def Carrat_1(self):
        self.from_label.setText("Carrat")
    def Atomic_1(self):
        self.from_label.setText("Atomic Mass Unit")
    
    def Kg_2(self):
        self.to_label.setText("Kilogram")
    def Gram_2(self):
        self.to_label.setText("Gram")
    def Milligram_2(self):
        self.to_label.setText("Milligram")
    def MetricTon_2(self):
        self.to_label.setText("Metric Ton")
    def LongTon_2(self):
        self.to_label.setText("Long Ton")
    def ShortTon_2(self):
        self.to_label.setText("Short Ton")
    def Pound_2(self):
        self.to_label.setText("Pound")
    def Ounce_2(self):
        self.to_label.setText("Ounce")
    def Carrat_2(self):
        self.to_label.setText("Carrat")
    def Atomic_2(self):
        self.to_label.setText("Atomic Mass Unit")
    

    # define method for convert button:
    def Convert_Into(self):
        ent_value = self.value_line.text()
        from_value = self.from_label.text()
        to_value = self.to_label.text()
        answer = 0
        if len(ent_value) > 0:
            try:
                ent_value = float(ent_value)
                if from_value == "Kilogram":
                    if to_value == "Kilogram":
                        answer = ent_value
                    elif to_value == "Gram":
                        answer = ent_value * 1000
                    elif to_value == "Milligram":
                        answer = ent_value * (10**6)
                    elif to_value == "Metric Ton":
                        answer = ent_value * 0.001
                    elif to_value == "Long Ton":
                        answer = ent_value * 0.000984206528
                    elif to_value == "Short Ton":
                        answer = ent_value * 0.00110231131
                    elif to_value == "Pound":
                        answer = ent_value * 2.20462262
                    elif to_value == "Ounce":
                        answer = ent_value * 35.2739619
                    elif to_value == "Carrat":
                        answer = ent_value * 5000
                    elif to_value == "Atomic Mass Unit":
                        answer = ent_value * 6.02214076 * (10**26)
                
                elif from_value == "Gram":
                    if to_value == "Kilogram":
                        answer = ent_value * 0.001
                    elif to_value == "Gram":
                        answer = ent_value
                    elif to_value == "Milligram":
                        answer = ent_value * 1000
                    elif to_value == "Metric Ton":
                        answer = ent_value / (10**6)
                    elif to_value == "Long Ton":
                        answer = (ent_value * 9.8421) / (10**7)
                    elif to_value == "Short Ton":
                        answer = (ent_value * 1.1023) / (10**6)
                    elif to_value == "Pound":
                        answer = (ent_value * 2.20462262) / (10**4)
                    elif to_value == "Ounce":
                        answer = ent_value * 0.0352739619
                    elif to_value == "Carrat":
                        answer = ent_value * 5
                    elif to_value == "Atomic Mass Unit":
                        answer = ent_value * 6.02214076 * (10**23)

                elif from_value == "Milligram":
                    if to_value == "Kilogram":
                        answer = ent_value / (10**6)
                    elif to_value == "Gram":
                        answer = ent_value * 0.001
                    elif to_value == "Milligram":
                        answer = ent_value
                    elif to_value == "Metric Ton":
                        answer = ent_value / (10**9)
                    elif to_value == "Long Ton":
                        answer = (ent_value * 9.8421) / (10**10)
                    elif to_value == "Short Ton":
                        answer = (ent_value * 1.1023) / (10**9)
                    elif to_value == "Pound":
                        answer = (ent_value * 2.20462262) / (10**6)
                    elif to_value == "Ounce":
                        answer = (ent_value * 3.52739619) / (10**5)
                    elif to_value == "Carrat":
                        answer = ent_value * 0.005
                    elif to_value == "Atomic Mass Unit":
                        answer = ent_value * 6.02214076 * (10**20)

                elif from_value == "Metric Ton":
                    if to_value == "Kilogram":
                        answer = ent_value * 1000
                    elif to_value == "Gram":
                        answer = ent_value * (10**6)
                    elif to_value == "Milligram":
                        answer = ent_value * (10**9)
                    elif to_value == "Metric Ton":
                        answer = ent_value
                    elif to_value == "Long Ton":
                        answer = ent_value * 0.98421
                    elif to_value == "Short Ton":
                        answer = ent_value * 1.1023
                    elif to_value == "Pound":
                        answer = ent_value * 2204.62262
                    elif to_value == "Ounce":
                        answer = ent_value * 35273.9619
                    elif to_value == "Carrat":
                        answer = ent_value * 5 * (10**6)
                    elif to_value == "Atomic Mass Unit":
                        answer = ent_value * 6.02214076 * (10**29)

                elif from_value == "Long Ton":
                    if to_value == "Kilogram":
                        answer = ent_value * 1016.04691
                    elif to_value == "Gram":
                        answer = ent_value * 1016046.91
                    elif to_value == "Milligram":
                        answer = ent_value * 1.01604691 * (10**9)
                    elif to_value == "Metric Ton":
                        answer = ent_value * 1.01604691
                    elif to_value == "Long Ton":
                        answer = ent_value
                    elif to_value == "Short Ton":
                        answer = ent_value * 1.12
                    elif to_value == "Pound":
                        answer = ent_value * 2240
                    elif to_value == "Ounce":
                        answer = ent_value * 35840
                    elif to_value == "Carrat":
                        answer = ent_value * 5080234.54
                    elif to_value == "Atomic Mass Unit":
                        answer = ent_value * 6.1187775 * (10**29)

                elif from_value == "Short Ton":
                    if to_value == "Kilogram":
                        answer = ent_value * 907.18474
                    elif to_value == "Gram":
                        answer = ent_value * 907184.74
                    elif to_value == "Milligram":
                        answer = ent_value * 907184740
                    elif to_value == "Metric Ton":
                        answer = ent_value * 0.90718474
                    elif to_value == "Long Ton":
                        answer = ent_value * 0.892857143
                    elif to_value == "Short Ton":
                        answer = ent_value
                    elif to_value == "Pound":
                        answer = ent_value * 2000
                    elif to_value == "Ounce":
                        answer = ent_value * 32000
                    elif to_value == "Carrat":
                        answer = ent_value * 4535923.7
                    elif to_value == "Atomic Mass Unit":
                        answer = ent_value * 5.4631942 * (10**29)

                elif from_value == "Pound":
                    if to_value == "Kilogram":
                        answer = ent_value * 0.45359237
                    elif to_value == "Gram":
                        answer = ent_value * 453.59237
                    elif to_value == "Milligram":
                        answer = ent_value * 453592.37
                    elif to_value == "Metric Ton":
                        answer = ent_value * 0.00045359237
                    elif to_value == "Long Ton":
                        answer = ent_value * 0.000446428571
                    elif to_value == "Short Ton":
                        answer = ent_value * 0.0005
                    elif to_value == "Pound":
                        answer = ent_value
                    elif to_value == "Ounce":
                        answer = ent_value * 16
                    elif to_value == "Carrat":
                        answer = ent_value * 2267.96185
                    elif to_value == "Atomic Mass Unit":
                        answer = ent_value * 2.7315971 * (10**26)

                elif from_value == "Ounce":
                    if to_value == "Kilogram":
                        answer = ent_value * 0.0283495231
                    elif to_value == "Gram":
                        answer = ent_value * 28.3495231
                    elif to_value == "Milligram":
                        answer = ent_value * 28349.5231
                    elif to_value == "Metric Ton":
                        answer = (ent_value * 2.83495231) / (10**5)
                    elif to_value == "Long Ton":
                        answer = (ent_value * 2.79017857) / (10**5)
                    elif to_value == "Short Ton":
                        answer = (ent_value * 3.125) / (10**5)
                    elif to_value == "Pound":
                        answer = ent_value * 0.0625
                    elif to_value == "Ounce":
                        answer = ent_value
                    elif to_value == "Carrat":
                        answer = ent_value * 141.747616
                    elif to_value == "Atomic Mass Unit":
                        answer = ent_value * 1.70724819 * (10**25)

                elif from_value == "Carrat":
                    if to_value == "Kilogram":
                        answer = ent_value * 0.0002
                    elif to_value == "Gram":
                        answer = ent_value * 0.2
                    elif to_value == "Milligram":
                        answer = ent_value * 200
                    elif to_value == "Metric Ton":
                        answer = (ent_value * 2) / (10**7)
                    elif to_value == "Long Ton":
                        answer = (ent_value * 1.96841306) / (10**7)
                    elif to_value == "Short Ton":
                        answer = (ent_value * 2.20462262) / (10**7)
                    elif to_value == "Pound":
                        answer = ent_value * 0.000440924524
                    elif to_value == "Ounce":
                        answer = ent_value * 0.00705479239
                    elif to_value == "Carrat":
                        answer = ent_value
                    elif to_value == "Atomic Mass Unit":
                        answer = ent_value * 1.20442815 * (10**23)

                elif from_value == "Atomic Mass Unit":
                    if to_value == "Kilogram":
                        answer = (ent_value * 1.66053907) / (10**27)
                    elif to_value == "Gram":
                        answer = (ent_value * 1.66053907) / (10**24)
                    elif to_value == "Milligram":
                        answer = (ent_value * 1.66053907) / (10**21)
                    elif to_value == "Metric Ton":
                        answer = (ent_value * 1.66053907) / (10**30)
                    elif to_value == "Long Ton":
                        answer = (ent_value * 1.63431339) / (10**30)
                    elif to_value == "Short Ton":
                        answer = (ent_value * 1.830431) / (10**30)
                    elif to_value == "Pound":
                        answer = (ent_value * 3.66086199) / (10**27)
                    elif to_value == "Ounce":
                        answer = (ent_value * 5.85737919) / (10**26)
                    elif to_value == "Carrat":
                        answer = (ent_value * 8.30269534) / (10**24)
                    elif to_value == "Atomic Mass Unit":
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
    iron = Ironman()
    sys.exit(app.exec_())