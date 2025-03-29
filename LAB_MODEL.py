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

# Loading graph images
graph_AAA = Image.open("GAAA.png")
graph_AAB = Image.open("GAAB.png")
graph_ABA = Image.open("GABA.png")
graph_ABB = Image.open("GABB.png")
graph_BAA = Image.open("GBAA.png")
graph_BAB = Image.open("GBAB.png")
graph_BBA = Image.open("GBBA.png")
graph_BBB = Image.open("GBBB.png")

# Title and subtitle with smaller font size using markdown
st.markdown("""
# MMW LAB EXPERIMENT ILLUSTRATION
### Yuval & Adi For Prof. Yosef Pinhasi
""", unsafe_allow_html=True)

# Creating a horizontal layout for switches and setting initial states
col1, col2, col3 = st.columns(3)
with col1:
    filter_status = st.checkbox("FILTER ON/OFF", False)
with col2:
    gdd_status = st.checkbox("GDD ON/OFF", False)
with col3:
    lab_light_status = st.checkbox("LAB LIGHT ON/OFF", True)  # Set to True for initial state AAB

# Determining the image and graph based on the switches' status
def get_image_and_graph(filter, gdd, lab_light):
    if not filter and not gdd and not lab_light:
        return img_AAA, graph_AAA
    elif not filter and not gdd and lab_light:
        return img_AAB, graph_AAB
    elif not filter and gdd and not lab_light:
        return img_ABA, graph_ABA
    elif not filter and gdd and lab_light:
        return img_ABB, graph_ABB
    elif filter and not gdd and not lab_light:
        return img_BAA, graph_BAA
    elif filter and not gdd and lab_light:
        return img_BAB, graph_BAB
    elif filter and gdd and not lab_light:
        return img_BBA, graph_BBA
    elif filter and gdd and lab_light:
        return img_BBB, graph_BBB

# Displaying the image and graph
current_image, current_graph = get_image_and_graph(filter_status, gdd_status, lab_light_status)
st.image(current_image, use_container_width=True)
st.image(current_graph, use_container_width=True)
