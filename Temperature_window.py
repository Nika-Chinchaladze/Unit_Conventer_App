from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QLineEdit
from PyQt5 import uic

class Spiderman(QMainWindow):
    def __init__(self):
        super(Spiderman, self).__init__()

        uic.loadUi("temperature.ui", self)

        # define content:
        self.temp_label = self.findChild(QLabel, "temp_label")
        self.from_label = self.findChild(QLabel, "from_label")
        self.to_label = self.findChild(QLabel, "to_label")
        self.answer_label = self.findChild(QLabel, "answer_label")

        self.cel_button = self.findChild(QPushButton, "cel_button")
        self.sius_button = self.findChild(QPushButton, "sius_button")
        self.kel_button = self.findChild(QPushButton, "kel_button")
        self.vin_button = self.findChild(QPushButton, "vin_button")
        self.far_button = self.findChild(QPushButton, "far_button")
        self.eit_button = self.findChild(QPushButton, "eit_button")
        self.convert_button = self.findChild(QPushButton, "convert_button")
        self.back_button = self.findChild(QPushButton, "back_button")

        self.line_1 = self.findChild(QFrame, "line_1")
        self.line_2 = self.findChild(QFrame, "line_2")
        self.frame_1 = self.findChild(QFrame, "frame_1")
        self.frame_2 = self.findChild(QFrame, "frame_2")

        self.value_line = self.findChild(QLineEdit, "value_line")
        self.value_line.setPlaceholderText("value")

        # call defined functions from here:
        self.cel_button.clicked.connect(self.Cel)
        self.kel_button.clicked.connect(self.Kel)
        self.far_button.clicked.connect(self.Far)
        self.sius_button.clicked.connect(self.Sius)
        self.vin_button.clicked.connect(self.Vin)
        self.eit_button.clicked.connect(self.Heit)
        self.convert_button.clicked.connect(self.Convert_Into)
        self.back_button.clicked.connect(self.GoToSource)

        self.show()
# ------------------------------------------ start -------------------------------------- #
    # define some colors:
    def Green_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(176, 255, 208);")
    
    def Red_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(255, 178, 216);")

    # define method for back button:
    def GoToSource(self):
        from Source_window import Maryland
        self.window_land = QMainWindow()
        self.randy = Maryland()
        self.close()
    
    # define methods for temperature button:
    def Cel(self):
        self.from_label.setText("Celsius")
    def Kel(self):
        self.from_label.setText("Kelvin")
    def Far(self):
        self.from_label.setText("Fahrenheit")
    
    def Sius(self):
        self.to_label.setText("Celsius")
    def Vin(self):
        self.to_label.setText("Kelvin")
    def Heit(self):
        self.to_label.setText("Fahrenheit")
    
    # define method for convert button:
    def Convert_Into(self):
        ent_value = self.value_line.text()
        from_value = self.from_label.text()
        to_value = self.to_label.text()
        answer = 0
        if len(ent_value) > 0:
            try:
                ent_value = float(ent_value)
                if from_value == "Celsius" and to_value == "Celsius":
                    answer = ent_value
                elif from_value == "Celsius" and to_value == "Kelvin":
                    answer = round(ent_value + 273.15, 2)
                elif from_value == "Celsius" and to_value == "Fahrenheit":
                    answer = round((ent_value * 1.8) + 32, 2)

                elif from_value == "Kelvin" and to_value == "Celsius":
                    answer = round(ent_value - 273.15, 2)
                elif from_value == "Kelvin" and to_value == "Kelvin":
                    answer = ent_value
                elif from_value == "Kelvin" and to_value == "Fahrenheit":
                    answer = round((ent_value * 1.8) - 459.67, 2)
                
                elif from_value == "Fahrenheit" and to_value == "Celsius":
                    answer = round((ent_value - 32) / 1.8, 2)
                elif from_value == "Fahrenheit" and to_value == "Kelvin":
                    answer = round((ent_value + 459.67) / 1.8, 2)
                elif from_value == "Fahrenheit" and to_value == "Fahrenheit":
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
    man = Spiderman()
    sys.exit(app.exec_())