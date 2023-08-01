import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fancy Calculator")
        self.setGeometry(200, 200, 400, 400)

        self.layout = QVBoxLayout()
        self.create_display()
        self.create_buttons()

        self.setLayout(self.layout)
        self.current_expression = ""

        # Dark Mode
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #FFFFFF;
                font-size: 20px;
                font-family: Arial;
            }
            
            QLineEdit {
                background-color: #1E1E1E;
                color: #FFFFFF;
                border: 2px solid #777777;
                border-radius: 10px;
                padding: 8px;
            }
            
            QPushButton {
                background-color: #333333;
                color: #FFFFFF;
                border: 2px solid #555555;
                border-radius: 10px;
                padding: 8px;
            }
            
            QPushButton:hover {
                background-color: #444444;
            }
            
            QPushButton:pressed {
                background-color: #555555;
            }
        """)

    def create_display(self):
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

    def create_buttons(self):
        buttons = [
            ('7', 0, 0),
            ('8', 0, 1),
            ('9', 0, 2),
            ('/', 0, 3),
            ('4', 1, 0),
            ('5', 1, 1),
            ('6', 1, 2),
            ('*', 1, 3),
            ('1', 2, 0),
            ('2', 2, 1),
            ('3', 2, 2),
            ('-', 2, 3),
            ('0', 3, 0),
            ('.', 3, 1),
            ('=', 3, 2),
            ('+', 3, 3),
            ('C', 4, 0),
            ('<-', 4, 1),
            ('sqrt', 4, 2),
            ('^', 4, 3),
            ('sin', 5, 0),
            ('cos', 5, 1),
            ('tan', 5, 2),
            ('pi', 5, 3),
        ]

        grid_layout = QGridLayout()
        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(lambda checked, text=text: self.on_button_click(text))
            button.setStyleSheet("QPushButton:hover { background-color: #555555; }")
            grid_layout.addWidget(button, row, col)

        self.layout.addLayout(grid_layout)

    def animate_button_press(self, button):
        button.setGeometry(button.geometry().adjusted(5, 5, -5, -5))
        anim = QPropertyAnimation(button, b"geometry")
        anim.setDuration(50)
        anim.setEndValue(button.geometry())
        anim.start(QPropertyAnimation.DeleteWhenStopped)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.current_expression)
                self.current_expression = str(result)
                self.display.setText(self.current_expression)
            except Exception as e:
                self.current_expression = ""
                self.display.setText("Error")
        elif text == 'C':
            self.current_expression = ""
            self.display.setText("")
        elif text == '<-':
            self.current_expression = self.current_expression[:-1]
            self.display.setText(self.current_expression)
        elif text == 'sqrt':
            try:
                result = math.sqrt(eval(self.current_expression))
                self.current_expression = str(result)
                self.display.setText(self.current_expression)
            except Exception as e:
                self.current_expression = ""
                self.display.setText("Error")
        elif text == '^':
            self.current_expression += '**'
            self.display.setText(self.current_expression)
        elif text in ('sin', 'cos', 'tan'):
            try:
                result = math.degrees(eval(f"math.{text}(math.radians({self.current_expression}))"))
                self.current_expression = str(result)
                self.display.setText(self.current_expression)
            except Exception as e:
                self.current_expression = ""
                self.display.setText("Error")
        elif text == 'pi':
            self.current_expression += str(math.pi)
            self.display.setText(self.current_expression)
        else:
            self.current_expression += text
            self.display.setText(self.current_expression)
        sender = self.sender()
        if isinstance(sender, QPushButton):
            self.animate_button_press(sender)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())
