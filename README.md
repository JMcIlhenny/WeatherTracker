# Weather Tracker ☀️🌧️❄️

A PyQt5 desktop app that fetches and displays real-time weather data using the OpenWeatherMap API.

---

## Images
<p align="center">
  <img width="392" height="227" alt="InitialHomeScreen" src="https://github.com/user-attachments/assets/2bb3d2f2-532f-44e0-9ff5-38676f55cee8" />
</p>
<p align="center">
  <img width="465" height="672" alt="WeatherDisplay" src="https://github.com/user-attachments/assets/b58a220f-b839-46c0-8c3b-c47ee1b10e22" />
</p>

---

## Features

- Search by city name
- Displays:
  - Current temperature
  - "Feels like" temperature
  - Min & Max temperature
  - Weather description
  - Weather emoji based on condition
- Toggle between **Fahrenheit** and **Celsius**
- Real-time weather data from OpenWeatherMap API
- Basic error handling

---

## Getting Started

### Prerequisites

- Python 3.x installed
- [OpenWeatherMap API key](https://home.openweathermap.org/users/sign_up)
- A virtual environment with PyQt5 installed

---

## API Key

**Note:** The API key is currently hardcoded into the "main.py" for simplicity.

To run the app yourself, open main.py and replace the placeholder with your actual API key from [OpenWeatherMap](https://openweathermap.org.api):
'''python
api_key = "your_api_key"

---

### Installation

```bash
# Clone the repo
git clone https://github.com/YOUR-USERNAME/WeatherTracker.git
cd WeatherTracker

# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
