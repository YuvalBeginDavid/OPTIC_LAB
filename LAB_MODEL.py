import streamlit as st
from PIL import Image, ImageDraw, ImageFont

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

# Font settings
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

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
        base_img = img_AAA
        graph_img = graph_AAA
    elif not filter and not gdd and lab_light:
        base_img = img_AAB
        graph_img = graph_AAB
    elif not filter and gdd and not lab_light:
        base_img = img_ABA
        graph_img = graph_ABA
    elif not filter and gdd and lab_light:
        base_img = img_ABB
        graph_img = graph_ABB
    elif filter and not gdd and not lab_light:
        base_img = img_BAA
        graph_img = graph_BAA
    elif filter and not gdd and lab_light:
        base_img = img_BAB
        graph_img = graph_BAB
    elif filter and gdd and not lab_light:
        base_img = img_BBA
        graph_img = graph_BBA
    elif filter and gdd and lab_light:
        base_img = img_BBB
        graph_img = graph_BBB

    # Draw text on the image
    draw = ImageDraw.Draw(base_img)
    texts = ["Photoreceiver", "GDD Holder", "Lens", "Hyperbolic Mirror", "Radiation Source"]
    x_positions = [100, 180, 350, 550, 700]  # Example positions, adjust as necessary
    y_position = base_img.height - 220  # Adjust vertical position as necessary
    for text, x in zip(texts, x_positions):
        draw.text((x, y_position), text, font=font, fill="white")

    return base_img, graph_img

# Displaying the image and graph
current_image, current_graph = get_image_and_graph(filter_status, gdd_status, lab_light_status)
st.image(current_image, use_container_width=True)
st.image(current_graph, use_container_width=True)
