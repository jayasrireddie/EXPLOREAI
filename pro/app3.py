import streamlit as st
import requests
import base64
from io import BytesIO
from PIL import Image

# Hugging Face API Details
API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Function to Generate Logo
def generate_logo(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))  # Convert response to image
        return img
    else:
        return None

# Streamlit UI
st.title("AI Logo Generator")
st.write("Enter a prompt below to generate a custom logo.")

# Input field for user prompt
prompt = st.text_input("Enter your logo description:")

# Generate button
if st.button("Generate Logo"):
    if prompt:
        image = generate_logo(prompt)
        if image:
            st.image(image, caption="Generated Logo", use_column_width=True)
        else:
            st.error("Failed to generate image. Check API key and try again.")
    else:
        st.warning("Please enter a prompt before generating.")
