import streamlit as st
from PIL import Image

# Loading images
img_AAA = Image.open("AAA.png")
img_AAB = Image.open("AAB.png")
img_ABA = Image.open("ABA.png")
img_ABB = Image.open("ABB.png")
img_BAA = Image.open("BAA.png")
img_BAB = Image.open("BAB.png")
img_BBA = Image.open("BBA.png")
img_BBB = Image.open("BBB.png")

# Title and subtitle
st.title('MMW LAB EXPILLUSTRATION')
st.write('Yuval & Adi For Prof. Yosef Pinhasi')

# Creating a horizontal layout for switches
col1, col2, col3 = st.columns(3)
with col1:
    filter_status = st.checkbox("FILTER ON/OFF", False)
with col2:
    gdd_status = st.checkbox("GDD ON/OFF", False)
with col3:
    lab_light_status = st.checkbox("LAB LIGHT ON/OFF", False)

# Determining the image based on the switches' status
def get_image(filter, gdd, lab_light):
    if not filter and not gdd and not lab_light:
        return img_AAA
    elif not filter and not gdd and lab_light:
        return img_AAB
    elif not filter and gdd and not lab_light:
        return img_ABA
    elif not filter and gdd and lab_light:
        return img_ABB
    elif filter and not gdd and not lab_light:
        return img_BAA
    elif filter and not gdd and lab_light:
        return img_BAB
    elif filter and gdd and not lab_light:
        return img_BBA
    elif filter and gdd and lab_light:
        return img_BBB

# Displaying the image
current_image = get_image(filter_status, gdd_status, lab_light_status)
st.image(current_image, use_container_width=True)
