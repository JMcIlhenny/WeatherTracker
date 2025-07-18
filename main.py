import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__() #super class
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.temp_feels_like_label = QLabel(self)
        self.temp_min_max_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.temp_feels_like_label)
        vbox.addWidget(self.temp_min_max_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.temp_feels_like_label.setAlignment(Qt.AlignCenter)
        self.temp_min_max_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.temp_feels_like_label.setObjectName("temp_feel_like_label")
        self.temp_min_max_label.setObjectName("temp_min_max_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;       
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;  
            }
            QLabel#description_label{
                font-size: 50px;
            }
            QLabel#temp_feels_like_label{
                font-size: 70px;
            }
            QLabel#temp_min_max_label{
                font-size: 70px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        # get the weather data
        api_key = "887a14cee881cdba2ea1ca4aabaa1d85"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # if theres no error, use the data from get_weather and display it
            if data["cod"] == 200:
                self.display_weather(data)
                
        except requests.exceptions.HTTPError as http_error:
        # HTTPError is an exception raised by the requests module 
        # when an http request returns a status code of 400 or 500
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input.")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key.")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied.")
                case 404:
                    self.display_error("Not Found:\nCity not found.")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later.")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server.")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down.")
                case 504:
                    self.display_error("Gateway Timeout:\nNo reponse from the server.")
                case _:
                    self.display_error(f"HTTP error occured:\n{http_error}")

        except requests.exceptions.ConnectionError:
        # internet gets disconnected 
            self.display_error("Connection Error:\nCheck your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out.")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:\nCheck the URL.")
        except requests.exceptions.RequestException as req_error:
        # network problems, invalid urls
            self.display_errornt(f"Request Error:\n{req_error}.")


    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.city_input.clear()
        self.emoji_label.clear()
        self.description_label.clear()
        self.temp_feels_like_label.clear()
        self.temp_min_max_label.clear()

    def display_weather(self, data):
        # in the data, we are looking for a key of 'main'
        # 'main' contains a dictionary with key value pairs
        self.temperature_label.setStyleSheet("font-size: 75px;")
        self.temp_feels_like_label.setStyleSheet("font-size: 50px;")
        self.temp_min_max_label.setStyleSheet("font-size: 50px;")
        self.emoji_label.setStyleSheet("font-size: 100px;")
        temperature_f = ((data['main']['temp']) * 9/5) - 459.67
        # converting from kelvin to fahrenheit
        temp_feels_like = ((data['main']['feels_like']) * 9/5) - 459.67
        temp_min = ((data['main']['temp_min']) * 9/5) - 459.67
        temp_max = ((data['main']['temp_max']) * 9/5) - 459.67
        weather_id = data['weather'][0]['id']
        weather_description = data['weather'][0]['description']

        self.temperature_label.setText(f"{temperature_f:.0f}°F")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)
        self.temp_feels_like_label.setText(f"Feels like: {temp_feels_like:.0f}°F")
        self.temp_min_max_label.setText(f"Min: {temp_min:.0f}°F     Max: {temp_max:.0f}°F")

    @staticmethod
    # static methods belong to a class but don't require any specific instance data or methods
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return '⛈️'
        elif 300 <= weather_id <= 321:
            return '🌤️'
        elif 500 <= weather_id <= 531:
            return '🌧️'
        elif 600 <= weather_id <= 632:
            return '🌨️'
        elif 701 <= weather_id <= 781:
            return '🌫️'
        elif weather_id == 762:
            return '🌋'
        elif weather_id == 771:
            return '💨'
        elif weather_id == 781:
            return '🌪️'
        elif weather_id == 800:
            return '☀️'
        elif 801 <= weather_id <= 804:
            return '🌥️'
        else:
            return ''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_()) # handles closing the window