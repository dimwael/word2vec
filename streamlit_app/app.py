import streamlit as st
from PIL import Image

st.title("Image Gallery")

images = ["image1.jpg", "image2.png", "image3.jpeg"]

for img in images:
    image = Image.open(img)
    st.image(image, caption=img)