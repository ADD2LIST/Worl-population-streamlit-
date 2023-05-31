import streamlit as st

import requests

# Set the page title

st.set_page_config(page_title="Real-time Population")

# Get the current population from the Worldometers API

url = "https://api.worldometers.info/population/"

response = requests.get(url)

data = response.json()

# Display the current population

st.write("The current population of the world is:", data["population"])

# Update the population every second

while True:

    response = requests.get(url)

    data = response.json()

    st.write("The current population of the world is:", data["population"])

