# 🌤️ Python Weather App

A simple weather app built with [Streamlit](https://streamlit.io/). Enter any city name and it shows the current temperature and conditions using the [OpenWeatherMap API](https://openweathermap.org/api).

## Features

- Search the current weather for any city in the world
- Shows temperature in °C with a short description of the conditions
- Displays the city and country that the API found
- Rejects blank input, number-only input, and cities that can't be found, with a clear message for each

## Requirements

- Python 3.9+
- A free OpenWeatherMap API key ([sign up here](https://openweathermap.org/api))

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/farhan-1798/python-weather-app.git
   cd python-weather-app
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit requests python-dotenv
   ```

4. **Add your API key**

   Copy the example environment file and add your key:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env`:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Run the app

```bash
streamlit run main.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## Project structure

```
.
├── main.py          # Streamlit app
├── concept.md       # Design notes and ideas for future features
├── .env.example     # Template for environment variables
└── .gitignore
```

## Ideas for future improvements

- Switch between Celsius and Fahrenheit
- Weather condition icons
- 5-day forecast chart
- Map showing where the city is
- Recent search history in the sidebar

See [concept.md](concept.md) for more details.
