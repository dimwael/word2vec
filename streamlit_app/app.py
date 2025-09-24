import streamlit as st
from PIL import Image

st.set_page_config(page_title="Image Gallery", page_icon=":smiley:", layout="wide")
st.markdown("""
    <style>
    .stApp {
        background-color: #F5F5F5;
        color: #333333;
    }
    </style>
    """, unsafe_allow_html=True)
st.title("🖼️ Image Gallery")

images = ["image1.jpg", "image2.png", "image3.jpeg"]

for img in images:
    image = Image.open(img)
    st.image(image, caption=img)