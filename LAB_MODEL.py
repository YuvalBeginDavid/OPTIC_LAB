import streamlit as st
from PIL import Image

# Loading images
img_AAA = Image.open("AAA.jpg")
img_AAB = Image.open("AAB.jpg")
img_ABA = Image.open("ABA.jpg")
img_ABB = Image.open("ABB.jpg")
img_BAA = Image.open("BAA.jpg")
img_BAB = Image.open("BAB.jpg")
img_BBA = Image.open("BBA.jpg")
img_BBB = Image.open("BBB.jpg")

# Title
st.title('Electric Lab - Control Panel')

# Switches
filter_status = st.checkbox("FILTER ON/OFF", False)
gdd_status = st.checkbox("GDD ON/OFF", False)
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
