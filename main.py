import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

st.title("Naser's Weather Application")
st.write("Enter any city name in the world to check the weather and temperature")

# Safety guard: ensure the key was loaded properly
if not API_KEY:
    st.error("API key is missing! Please make sure OPENWEATHER_API_KEY is defined in your .env file.")
    st.stop()

# 1. Search Bar Layout (Weighted Columns)
search_col, btn_col = st.columns([4, 1])

with search_col:
    city_input = st.text_input(
        "Enter city",
        placeholder="e.g. Tokyo, London",
        label_visibility="collapsed",
    )

with btn_col:
    search_clicked = st.button("Search", use_container_width=True)

# 2. Validation & API Fetch
if search_clicked or city_input:
    clean_city = city_input.strip()

    if not clean_city:
        st.warning("City name can't be blank. Please enter a city name to check the weather.")
    elif clean_city.isnumeric():
        st.error("Please enter a valid city name containing letters.")
    else:
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={clean_city}&appid={API_KEY}&units=metric"
        )

        if weather_data.status_code != 200:
            st.error("City was not found. Please check the city name properly and try again.")
        else:
            data = weather_data.json()
            weather = data["weather"][0]["main"]
            description = data["weather"][0]["description"].capitalize()
            temperature = round(data["main"]["temp"])
            resolved_city = data.get("name", clean_city)
            country = data.get("sys", {}).get("country", "")

            # Clean UI Output
            st.divider()
            st.success(f"Weather for **{resolved_city}, {country}**")
            st.metric(label="Temperature", value=f"{temperature}°C", delta=description)