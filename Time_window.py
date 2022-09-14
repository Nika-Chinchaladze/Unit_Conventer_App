from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QLineEdit
from PyQt5 import uic

class Blackpanter(QMainWindow):
    def __init__(self):
        super(Blackpanter, self).__init__()

        uic.loadUi("time.ui", self)

        # define content:
        self.time_label = self.findChild(QLabel, "time_label")
        self.from_label = self.findChild(QLabel, "from_label")
        self.to_label = self.findChild(QLabel, "to_label")
        self.answer_label = self.findChild(QLabel, "answer_label")
        # --------------------------------------------------------------- #
        self.second_button = self.findChild(QPushButton, "second_button")
        self.mili_button = self.findChild(QPushButton, "mili_button")
        self.micro_button = self.findChild(QPushButton, "micro_button")
        self.nano_button = self.findChild(QPushButton, "nano_button")
        self.pico_button = self.findChild(QPushButton, "pico_button")
        self.minute_button = self.findChild(QPushButton, "minute_button")
        self.hour_button = self.findChild(QPushButton, "hour_button")
        self.day_button = self.findChild(QPushButton, "day_button")
        self.week_button = self.findChild(QPushButton, "week_button")
        self.month_button = self.findChild(QPushButton, "month_button")
        self.year_button = self.findChild(QPushButton, "year_button")
        # --------------------------------------------------------------- #
        self.second_button_2 = self.findChild(QPushButton, "second_button_2")
        self.mili_button_2 = self.findChild(QPushButton, "mili_button_2")
        self.micro_button_2 = self.findChild(QPushButton, "micro_button_2")
        self.nano_button_2 = self.findChild(QPushButton, "nano_button_2")
        self.pico_button_2 = self.findChild(QPushButton, "pico_button_2")
        self.minute_button_2 = self.findChild(QPushButton, "minute_button_2")
        self.hour_button_2 = self.findChild(QPushButton, "hour_button_2")
        self.day_button_2 = self.findChild(QPushButton, "day_button_2")
        self.week_button_2 = self.findChild(QPushButton, "week_button_2")
        self.month_button_2 = self.findChild(QPushButton, "month_button_2")
        self.year_button_2 = self.findChild(QPushButton, "year_button_2")
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
        self.back_button.clicked.connect(self.BackToSourceWindow)
        self.convert_button.clicked.connect(self.Convert_Into)
        self.second_button.clicked.connect(self.Second_1)
        self.second_button_2.clicked.connect(self.Second_2)
        self.mili_button.clicked.connect(self.Millisecond_1)
        self.mili_button_2.clicked.connect(self.Millisecond_2)
        self.micro_button.clicked.connect(self.Microsecond_1)
        self.micro_button_2.clicked.connect(self.Microsecond_2)
        self.nano_button.clicked.connect(self.Nanosecond_1)
        self.nano_button_2.clicked.connect(self.Nanosecond_2)
        self.pico_button.clicked.connect(self.Picosecond_1)
        self.pico_button_2.clicked.connect(self.Picosecond_2)
        self.minute_button.clicked.connect(self.Minute_1)
        self.minute_button_2.clicked.connect(self.Minute_2)
        self.hour_button.clicked.connect(self.Hour_1)
        self.hour_button_2.clicked.connect(self.Hour_2)
        self.day_button.clicked.connect(self.Day_1)
        self.day_button_2.clicked.connect(self.Day_2)
        self.week_button.clicked.connect(self.Week_1)
        self.week_button_2.clicked.connect(self.Week_2)
        self.month_button.clicked.connect(self.Month_1)
        self.month_button_2.clicked.connect(self.Month_2)
        self.year_button.clicked.connect(self.Year_1)
        self.year_button_2.clicked.connect(self.Year_2)

        self.show()
# ------------------------------------------ start -------------------------------------- #
    # define some colors:
    def Green_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(176, 255, 208);")
    
    def Red_color(self):
        self.answer_label.setStyleSheet("background-color: rgb(255, 178, 216);")

    # define method for back button:
    def BackToSourceWindow(self):
        from Source_window import Maryland
        self.window_land = QMainWindow()
        self.randy = Maryland()
        self.close()
    
    # define methods for temperature button:
    def Second_1(self):
        self.from_label.setText("Second")
    def Millisecond_1(self):
        self.from_label.setText("Millisecond")
    def Microsecond_1(self):
        self.from_label.setText("Microsecond")
    def Nanosecond_1(self):
        self.from_label.setText("Nanosecond")
    def Picosecond_1(self):
        self.from_label.setText("Picosecond")
    def Minute_1(self):
        self.from_label.setText("Minute")
    def Hour_1(self):
        self.from_label.setText("Hour")
    def Day_1(self):
        self.from_label.setText("Day")
    def Week_1(self):
        self.from_label.setText("Week")
    def Month_1(self):
        self.from_label.setText("Month")
    def Year_1(self):
        self.from_label.setText("Year")
    
    def Second_2(self):
        self.to_label.setText("Second")
    def Millisecond_2(self):
        self.to_label.setText("Millisecond")
    def Microsecond_2(self):
        self.to_label.setText("Microsecond")
    def Nanosecond_2(self):
        self.to_label.setText("Nanosecond")
    def Picosecond_2(self):
        self.to_label.setText("Picosecond")
    def Minute_2(self):
        self.to_label.setText("Minute")
    def Hour_2(self):
        self.to_label.setText("Hour")
    def Day_2(self):
        self.to_label.setText("Day")
    def Week_2(self):
        self.to_label.setText("Week")
    def Month_2(self):
        self.to_label.setText("Month")
    def Year_2(self):
        self.to_label.setText("Year")
    
    
    # define method for convert button:
    def Convert_Into(self):
        ent_value = self.value_line.text()
        from_value = self.from_label.text()
        to_value = self.to_label.text()
        answer = 0
        if len(ent_value) > 0:
            try:
                ent_value = float(ent_value)
                if from_value == "Second":
                    if to_value == "Second":
                        answer = ent_value
                    elif to_value == "Millisecond":
                        answer = ent_value * 1000
                    elif to_value == "Microsecond":
                        answer = ent_value * (10**6)
                    elif to_value == "Nanosecond":
                        answer = ent_value * (10**9)
                    elif to_value == "Picosecond":
                        answer = ent_value * (10**12)
                    elif to_value == "Minute":
                        answer = ent_value * 0.0166666667
                    elif to_value == "Hour":
                        answer = ent_value * 0.000277777778
                    elif to_value == "Day":
                        answer = (ent_value * 1.15740741) / (10**5)
                    elif to_value == "Week":
                        answer = (ent_value * 1.65343915) / (10**6)
                    elif to_value == "Month":
                        answer = (ent_value * 3.80265176) / (10**7)
                    elif to_value == "Year":
                        answer = (ent_value * 3.16887646) / (10**8)
                
                elif from_value == "Millisecond":
                    if to_value == "Second":
                        answer = ent_value * 0.001
                    elif to_value == "Millisecond":
                        answer = ent_value
                    elif to_value == "Microsecond":
                        answer = ent_value * (10**3)
                    elif to_value == "Nanosecond":
                        answer = ent_value * (10**6)
                    elif to_value == "Picosecond":
                        answer = ent_value * (10**9)
                    elif to_value == "Minute":
                        answer = (ent_value * 1.66666667) / (10**5)
                    elif to_value == "Hour":
                        answer = (ent_value * 2.77777778) / (10**7)
                    elif to_value == "Day":
                        answer = (ent_value * 1.15740741) / (10**8)
                    elif to_value == "Week":
                        answer = (ent_value * 1.65343915) / (10**9)
                    elif to_value == "Month":
                        answer = (ent_value * 3.80265176) / (10**10)
                    elif to_value == "Year":
                        answer = (ent_value * 3.16887646) / (10**11)

                elif from_value == "Microsecond":
                    if to_value == "Second":
                        answer = ent_value / (10**6)
                    elif to_value == "Millisecond":
                        answer = ent_value * 0.001
                    elif to_value == "Microsecond":
                        answer = ent_value
                    elif to_value == "Nanosecond":
                        answer = ent_value * 1000
                    elif to_value == "Picosecond":
                        answer = ent_value * (10**6)
                    elif to_value == "Minute":
                        answer = (ent_value * 1.66666667) / (10**8)
                    elif to_value == "Hour":
                        answer = (ent_value * 2.77777778) / (10**10)
                    elif to_value == "Day":
                        answer = (ent_value * 1.15740741) / (10**11)
                    elif to_value == "Week":
                        answer = (ent_value * 1.65343915) / (10**12)
                    elif to_value == "Month":
                        answer = (ent_value * 3.80265176) / (10**13)
                    elif to_value == "Year":
                        answer = (ent_value * 3.16887646) / (10**14)

                elif from_value == "Nanosecond":
                    if to_value == "Second":
                        answer = ent_value / (10**9)
                    elif to_value == "Millisecond":
                        answer = ent_value / (10**6)
                    elif to_value == "Microsecond":
                        answer = ent_value * 0.001
                    elif to_value == "Nanosecond":
                        answer = ent_value
                    elif to_value == "Picosecond":
                        answer = ent_value * 1000
                    elif to_value == "Minute":
                        answer = (ent_value * 1.66666667) / (10**11)
                    elif to_value == "Hour":
                        answer = (ent_value * 2.77777778) / (10**13)
                    elif to_value == "Day":
                        answer = (ent_value * 1.15740741) / (10**14)
                    elif to_value == "Week":
                        answer = (ent_value * 1.65343915) / (10**15)
                    elif to_value == "Month":
                        answer = (ent_value * 3.80265176) / (10**16)
                    elif to_value == "Year":
                        answer = (ent_value * 3.16887646) / (10**17)


                elif from_value == "Picosecond":
                    if to_value == "Second":
                        answer = ent_value / (10**12)
                    elif to_value == "Millisecond":
                        answer = ent_value / (10**9)
                    elif to_value == "Microsecond":
                        answer = ent_value / (10**6)
                    elif to_value == "Nanosecond":
                        answer = ent_value / 1000
                    elif to_value == "Picosecond":
                        answer = ent_value
                    elif to_value == "Minute":
                        answer = (ent_value * 1.66666667) / (10**14)
                    elif to_value == "Hour":
                        answer = (ent_value * 2.77777778) / (10**16)
                    elif to_value == "Day":
                        answer = (ent_value * 1.15740741) / (10**17)
                    elif to_value == "Week":
                        answer = (ent_value * 1.65343915) / (10**18)
                    elif to_value == "Month":
                        answer = (ent_value * 3.80265176) / (10**19)
                    elif to_value == "Year":
                        answer = (ent_value * 3.16887646) / (10**20)


                elif from_value == "Minute":
                    if to_value == "Second":
                        answer = ent_value * 60
                    elif to_value == "Millisecond":
                        answer = ent_value * 6 * (10**4)
                    elif to_value == "Microsecond":
                        answer = ent_value * 6 * (10**7)
                    elif to_value == "Nanosecond":
                        answer = ent_value * 6 * (10**10)
                    elif to_value == "Picosecond":
                        answer = ent_value * 6 * (10**13)
                    elif to_value == "Minute":
                        answer = ent_value
                    elif to_value == "Hour":
                        answer = ent_value * 0.0166666667
                    elif to_value == "Day":
                        answer = ent_value * 0.000694444444
                    elif to_value == "Week":
                        answer = (ent_value * 9.92063492) / (10**5)
                    elif to_value == "Month":
                        answer = (ent_value * 2.28159105) / (10**5)
                    elif to_value == "Year":
                        answer = (ent_value * 1.90132588) / (10**6)

                elif from_value == "Hour":
                    if to_value == "Second":
                        answer = ent_value * 3600
                    elif to_value == "Millisecond":
                        answer = ent_value * 36 * (10**5)
                    elif to_value == "Microsecond":
                        answer = ent_value * 36 * (10**8)
                    elif to_value == "Nanosecond":
                        answer = ent_value * 36 * (10**11)
                    elif to_value == "Picosecond":
                        answer = ent_value * 36 * (10**14)
                    elif to_value == "Minute":
                        answer = ent_value * 60
                    elif to_value == "Hour":
                        answer = ent_value
                    elif to_value == "Day":
                        answer = ent_value / 24
                    elif to_value == "Week":
                        answer = ent_value / (24 * 7)
                    elif to_value == "Month":
                        answer = ent_value * 0.00136895463
                    elif to_value == "Year":
                        answer = ent_value * 0.000114079553

                elif from_value == "Day":
                    if to_value == "Second":
                        answer = ent_value * 86400
                    elif to_value == "Millisecond":
                        answer = ent_value * 86400 * (10**3)
                    elif to_value == "Microsecond":
                        answer = ent_value * 86400 * (10**6)
                    elif to_value == "Nanosecond":
                        answer = ent_value * 86400 * (10**9)
                    elif to_value == "Picosecond":
                        answer = ent_value * 86400 * (10**12)
                    elif to_value == "Minute":
                        answer = ent_value * 1440
                    elif to_value == "Hour":
                        answer = ent_value * 24
                    elif to_value == "Day":
                        answer = ent_value
                    elif to_value == "Week":
                        answer = ent_value / 7
                    elif to_value == "Month":
                        answer = ent_value * 0.0328549112
                    elif to_value == "Year":
                        answer = ent_value * 0.00273790926

                elif from_value == "Week":
                    if to_value == "Second":
                        answer = ent_value * 604800
                    elif to_value == "Millisecond":
                        answer = ent_value * 604800 * (10**3)
                    elif to_value == "Microsecond":
                        answer = ent_value * 604800 * (10**6)
                    elif to_value == "Nanosecond":
                        answer = ent_value * 604800 * (10**9)
                    elif to_value == "Picosecond":
                        answer = ent_value * 604800 * (10**12)
                    elif to_value == "Minute":
                        answer = ent_value * 10080
                    elif to_value == "Hour":
                        answer = ent_value * 168
                    elif to_value == "Day":
                        answer = ent_value * 7
                    elif to_value == "Week":
                        answer = ent_value
                    elif to_value == "Month":
                        answer = ent_value * 0.229984378
                    elif to_value == "Year":
                        answer = ent_value * 0.0191653649

                elif from_value == "Month":
                    if to_value == "Second":
                        answer = ent_value * 2629743.83
                    elif to_value == "Millisecond":
                        answer = ent_value * 2629743.83 * (10**3)
                    elif to_value == "Microsecond":
                        answer = ent_value * 2629743.83 * (10**6)
                    elif to_value == "Nanosecond":
                        answer = ent_value * 2629743.83 * (10**9)
                    elif to_value == "Picosecond":
                        answer = ent_value * 2629743.83 * (10**12)
                    elif to_value == "Minute":
                        answer = ent_value * 43829.0639
                    elif to_value == "Hour":
                        answer = ent_value * 730.484398
                    elif to_value == "Day":
                        answer = ent_value * 30.4368499
                    elif to_value == "Week":
                        answer = ent_value * 4.34812141
                    elif to_value == "Month":
                        answer = ent_value
                    elif to_value == "Year":
                        answer = ent_value / 12

                elif from_value == "Year":
                    if to_value == "Second":
                        answer = ent_value * 365.25 * 24 * 3600
                    elif to_value == "Millisecond":
                        answer = ent_value * 365.25 * 24 * 3600 * (10**3)
                    elif to_value == "Microsecond":
                        answer = ent_value * 365.25 * 24 * 3600 * (10**6)
                    elif to_value == "Nanosecond":
                        answer = ent_value * 365.25 * 24 * 3600 * (10**9)
                    elif to_value == "Picosecond":
                        answer = ent_value * 365.25 * 24 * 3600 * (10**12)
                    elif to_value == "Minute":
                        answer = ent_value * 365.25 * 24 * 60
                    elif to_value == "Hour":
                        answer = ent_value * 365.25 * 24
                    elif to_value == "Day":
                        answer = ent_value * 365.25
                    elif to_value == "Week":
                        answer = ent_value * 12 * 4.34812141
                    elif to_value == "Month":
                        answer = ent_value * 12
                    elif to_value == "Year":
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
    panter = Blackpanter()
    sys.exit(app.exec_())