# Weather App

## Overview

This is a simple desktop weather app built with Python and PyQt5. It allows the user to enter a city name and fetches the current weather data for that city using the OpenWeatherMap API.

The app displays the following weather information:

- Temperature (Fahrenheit and Celsius)
- Humidity
- Pressure
- Wind Speed
- Weather Description
- Weather Icon

The app has a simple and clean UI built with PyQt5.

## Dependencies

- PyQt5
- Requests
- Python 3

The following Python packages need to be installed:

```
pip install pyqt5 requests
```

## Usage

To use the app:

1. Clone the repository

```
git clone https://github.com/takshakmudgal/CodSoft_Projects/weather-app.git
```

2. Navigate to the project directory

```
cd weather-app
```

3. Install the required packages mentioned above.

4. Get your API key from [OpenWeatherMap](https://openweathermap.org/)

5. Add your API key to `config.py` (RIGHT NOW IT HAS MINE)

```python
API_KEY = "YOUR_API_KEY"
```

6. Run the app

```
python main.py
```

7. Enter a city name and click "Get Weather" to fetch weather data

## Code Overview

- `main.py` - Creates the main application window, layout, and events
- `config.py` - Contains the OpenWeatherMap API key

The code is structured into classes for each component and uses the Model-View-Controller pattern.

## License

This project is open source and available under the [MIT License](LICENSE).
