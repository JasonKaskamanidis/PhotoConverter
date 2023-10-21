import streamlit as st
from PIL import Image


st.subheader("Color to Grayscale Converter")
uploaded_image = st.file_uploader("Upload Image")
with st.expander("Start Camera"):
	#start the camera
	camera_image = st.camera_input("Camera")

if camera_image:
	#create pillow omage instance
	img = Image.open(camera_image)
	#convert image to grayscale
	gray_img = img.convert('L')
	#show image
	st.image(gray_img)
if uploaded_image:
	upimg = Image.open(uploaded_image)
	gray_upimg = upimg.convert('L')
	st.image(gray_upimg)

