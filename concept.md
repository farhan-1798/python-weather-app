# 🌤️ Streamlit Weather App — Concept & Inspiration Guide

A reference guide to help you design and build your interactive weather application from scratch.

---

## 1. Streamlit Mental Model

Unlike traditional web frameworks (like Flask or React) that require separate routes, request handlers, or complex state management, Streamlit treats your Python script as a **reactive script**:

> **How it works:** Whenever a user interacts with a widget (types in a text box, clicks a button, toggles a radio), Streamlit **re-runs your entire script from top to bottom**.

Keep this in mind when structuring your code:
- Inputs come first.
- Conditionals decide what to fetch and display.
- State that needs to survive across re-runs can be stored in `st.session_state`.

---

## 2. Essential Streamlit Building Blocks

Here are the key Streamlit components you can use to build your UI:

### Page & Layout
```python
import streamlit as st

# Configure browser tab title and favicon
st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

# Layout columns for side-by-side components
col1, col2 = st.columns(2)
# or specify ratios: col1, col2 = st.columns([3, 1])
```

### Inputs & Triggers
```python
# Text input for the city
city = st.text_input("Enter city name:", placeholder="e.g. Tokyo, London")

# Action button
search_btn = st.button("Get Weather")

# Radio toggle for units
unit = st.radio("Units", options=["Celsius (°C)", "Fahrenheit (°F)"])
```

### Displaying Weather Information
```python
# Headings & Text
st.title("Weather App")
st.subheader("Current Conditions")

# Metric cards (great for temperature, humidity, wind)
st.metric(label="Temperature", value="24°C", delta="Feels like 26°C")

# Weather condition icon
st.image("https://openweathermap.org/img/wn/10d@2x.png", width=120)

# User feedback & alerts
st.spinner("Fetching data...")
st.success("Data loaded!")
st.warning("Please enter a valid city name.")
st.error("City not found (404).")
```

---

## 3. OpenWeatherMap API Reference

### Current Weather Endpoint
```text
https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}
```

* **Parameters:**
  * `q`: City name (e.g. `London`, `Tokyo`).
  * `units`: `metric` for Celsius, `imperial` for Fahrenheit, or omit for Kelvin.
  * `appid`: Your OpenWeatherMap API key.

### Key Fields in the JSON Response
```json
{
  "name": "London",
  "sys": { "country": "GB", "sunrise": 1710000000, "sunset": 1710040000 },
  "weather": [
    { "main": "Clouds", "description": "scattered clouds", "icon": "03d" }
  ],
  "main": {
    "temp": 15.2,
    "feels_like": 14.8,
    "temp_min": 13.0,
    "temp_max": 17.1,
    "humidity": 72,
    "pressure": 1015
  },
  "wind": { "speed": 4.1 },
  "coord": { "lat": 51.5074, "lon": -0.1278 }
}
```

### Displaying the Condition Icon
OpenWeatherMap provides icons matching the `icon` field (`01d`, `02d`, `10d`, etc.):
```text
https://openweathermap.org/img/wn/{icon_code}@2x.png
```

---

## 4. Edge Cases to Handle

1. **Empty / Blank Input**: Prevent making an API call if the search box is empty.
2. **Numeric-only Input**: Strings like `"656"` might match postal codes or numeric identifiers instead of cities. You can validate using `.isalpha()` or checking `not user_input.isnumeric()`.
3. **HTTP 404 (Not Found)**: Show a friendly message suggesting the user check their spelling.
4. **Network & General Errors**: Check `response.status_code == 200` before accessing JSON keys to avoid `KeyError` crashes.

---

## 5. Creative Feature Ideas to Explore

* **Quick-Select Chips**: Row of buttons for popular cities (`London`, `Tokyo`, `New York`) that automatically populate the search.
* **Interactive Map**: Use `st.map()` with `coord.lat` and `coord.lon` to show where the city is located.
* **Unit Conversion**: Allow switching between Celsius and Fahrenheit.
* **5-Day Forecast Chart**: Use the `/data/2.5/forecast` endpoint with `st.line_chart()` to show upcoming temperature trends.
* **Search History**: Use `st.session_state` to store recent searches and display them in a sidebar (`with st.sidebar:`).

---

## 6. How to Run Your App

When you create your script (e.g. `main.py` or `streamlit_app.py`):

```bash
streamlit run <your_script_name>.py
```
Open **`http://localhost:8501`** in your browser. Streamlit automatically refreshes when you save changes in your code!
