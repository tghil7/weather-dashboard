import streamlit as st
import requests
from weather_dashboard import WeatherDashboard

st.title("Current Weather for 4 U.S Cities:")

# Fetch weather data when button is clicked
if st.button("Get Weather"):
    def main():
        dashboard = WeatherDashboard()

        # Create bucket if needed
        dashboard.create_bucket_if_not_exists()

        cities = ["Philadelphia", "Seattle", "New York", "Kansas City"]

        for city in cities:
            st.subheader(f"\nFetching weather for {city}...")
            weather_data = dashboard.fetch_weather(city)
            if weather_data:
                temp = weather_data['main']['temp']
                feels_like = weather_data['main']['feels_like']
                humidity = weather_data['main']['humidity']
                description = weather_data['weather'][0]['description']

                st.write(f"Temperature: {temp}°F")
                st.write(f"Feels like: {feels_like}°F")
                st.write(f"Humidity: {humidity}%")
                st.write(f"Conditions: {description}")

                # Save to S3


    #               success = dashboard.save_to_s3(weather_data, city)
    #                if success:
    #                    print(f"Weather data for {city} saved to S3!")
    #            else:
    #                print(f"Failed to fetch weather data for {city}")

    if __name__ == "__main__":
        main()
