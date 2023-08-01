import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import requests
import json
from config import API_KEY

class WeatherApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        
        # Modern and elegant font with improved style
        font = QFont("Segoe UI", 14, weight=QFont.Bold)
        label_font = QFont("Segoe UI", 12)

        self.cityLabel = QLabel('City:')
        self.cityLabel.setFont(label_font)

        self.cityInput = QLineEdit()
        self.cityInput.setFont(font)

        self.tempLabel = QLabel('Temperature:')
        self.tempLabel.setFont(label_font)

        self.tempValueF = QLabel('')
        self.tempValueF.setFont(font)
        self.tempValueC = QLabel('')
        self.tempValueC.setFont(font)

        self.humidityLabel = QLabel('Humidity:')
        self.humidityLabel.setFont(label_font)

        self.humidityValue = QLabel('')
        self.humidityValue.setFont(font)

        self.pressureLabel = QLabel('Pressure:')
        self.pressureLabel.setFont(label_font)

        self.pressureValue = QLabel('')
        self.pressureValue.setFont(font)

        self.windLabel = QLabel('Wind Speed:')
        self.windLabel.setFont(label_font)

        self.windValue = QLabel('')
        self.windValue.setFont(font)

        self.descLabel = QLabel('Description:')
        self.descLabel.setFont(label_font)

        self.descValue = QLabel('')
        self.descValue.setFont(font)

        self.weatherIconLabel = QLabel()
        self.weatherIconLabel.setMaximumSize(100, 100)

        self.errorLabel = QLabel('')  # Error label to display error messages
        self.errorLabel.setFont(label_font)
        self.errorLabel.setStyleSheet("color: red;")

        self.getWeatherBtn = QPushButton('Get Weather')
        self.getWeatherBtn.setFont(label_font)
        self.getWeatherBtn.setStyleSheet(
            """
            background-color: #3498db;
            color: white;
            border: 2px solid #3498db;
            padding: 10px;
            border-radius: 5px;
            text-transform: uppercase;
            """
        )
        self.getWeatherBtn.clicked.connect(self.getWeather)


        grid.addWidget(self.cityLabel, 0, 0)
        grid.addWidget(self.cityInput, 0, 1)

        grid.addWidget(self.tempLabel, 1, 0)
        grid.addWidget(self.tempValueF, 1, 1)
        grid.addWidget(self.tempValueC, 1, 2)

        grid.addWidget(self.humidityLabel, 2, 0)
        grid.addWidget(self.humidityValue, 2, 1)

        grid.addWidget(self.pressureLabel, 3, 0)
        grid.addWidget(self.pressureValue, 3, 1)

        grid.addWidget(self.windLabel, 4, 0)
        grid.addWidget(self.windValue, 4, 1)

        grid.addWidget(self.descLabel, 5, 0)
        grid.addWidget(self.descValue, 5, 1)
        grid.addWidget(self.weatherIconLabel, 5, 2)

        grid.addWidget(self.errorLabel, 6, 0, 1, 3)  # Error label

        grid.addWidget(self.getWeatherBtn, 7, 0, 1, 3)  # Move the button down

        self.setWindowTitle('Weather App')
        self.setGeometry(300, 300, 400, 250)
        self.setStyleSheet("""
            background-color: #2c3e50;
            color: #ffffff;
            selection-color: #000000;
            selection-background-color: #f39c12;
            """
        )
        self.show()

        self.unit = 'F'

    def getWeather(self):
        city = self.cityInput.text()

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

        self.showLoading()  # Display the loading animation

        response = requests.get(url)
        data = json.loads(response.text)

        if response.status_code == 200:
            # Data fetched successfully, proceed with displaying the weather information
            temp_f = data['main']['temp']
            temp_c = (temp_f - 32) * 5 / 9
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind_speed = data['wind']['speed']
            desc = data['weather'][0]['description']
            weather_icon = data['weather'][0]['icon']

            self.hideLoading()  # Hide the loading animation

            self.tempValueF.setText(f'{temp_f:.1f}°F')
            self.tempValueF.setToolTip('Temperature (Fahrenheit)')
            self.tempValueC.setText(f'{temp_c:.1f}°C')
            self.tempValueC.setToolTip('Temperature (Celsius)')

            self.humidityValue.setText(f'{humidity}%')
            self.pressureValue.setText(f'{pressure} hPa')
            self.windValue.setText(f'{wind_speed} mph')
            self.descValue.setText(desc)

            # Fetch the weather icon and set it to the label
            icon_url = f"http://openweathermap.org/img/w/{weather_icon}.png"
            icon_data = requests.get(icon_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(icon_data)
            self.weatherIconLabel.setPixmap(pixmap)

            # Clear the error label in case there was a previous error
            self.errorLabel.setText('')
        else:
            # Error occurred, display the error message in the error label
            self.errorLabel.setText('City not found in the API Database')

    def showLoading(self):
        self.tempValueF.setText('Loading...')
        self.tempValueF.setToolTip('')
        self.tempValueC.setText('')
        self.tempValueC.setToolTip('')
        self.humidityValue.setText('')
        self.pressureValue.setText('')
        self.windValue.setText('')
        self.descValue.setText('')
        self.weatherIconLabel.clear()

    def hideLoading(self):
        pass

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Use the modern Fusion style
    weatherApp = WeatherApp()
    sys.exit(app.exec_())
