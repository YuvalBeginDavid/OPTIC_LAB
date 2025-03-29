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

# Loading and resizing graph images
def load_and_resize_graph(filename):
    img = Image.open(filename)
    width, height = img.size
    # Cropping the bottom part of the graph (small portion)
    cropped_graph = img.crop((0, int(height*0.75), width, height))
    # Resizing the cropped part to make it smaller
    resized_graph = cropped_graph.resize((int(width*0.5), int(height*0.25)), Image.ANTIALIAS)
    return resized_graph

graph_AAA = load_and_resize_graph("GAAA.png")
graph_AAB = load_and_resize_graph("GAAB.png")
graph_ABA = load_and_resize_graph("GABA.png")
graph_ABB = load_and_resize_graph("GABB.png")
graph_BAA = load_and_resize_graph("GBAA.png")
graph_BAB = load_and_resize_graph("GBAB.png")
graph_BBA = load_and_resize_graph("GBBA.png")
graph_BBB = load_and_resize_graph("GBBB.png")

# Title and subtitle with smaller font size using markdown
st.markdown("""
# MMW LAB EXPERIMENT ILLUSTRATION
### Yuval & Adi For Prof. Yosef Pinhasi
""", unsafe_allow_html=True)

# Creating a horizontal layout for switches
col1, col2, col3 = st.columns(3)
with col1:
    filter_status = st.checkbox("FILTER ON/OFF", False)
with col2:
    gdd_status = st.checkbox("GDD ON/OFF", False)
with col3:
    lab_light_status = st.checkbox("LAB LIGHT ON/OFF", False)

# Determining the image and placing the resized graph at the bottom center part of the image
def get_combined_image(filter, gdd, lab_light):
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

    # Combine the images
    base_width, base_height = base_img.size
    graph_width, graph_height = graph_img.size
    # Positioning the graph at the bottom center
    position = ((base_width - graph_width) // 2, base_height - graph_height)
    base_img.paste(graph_img, position, graph_img)
    return base_img

# Displaying the combined image
current_image = get_combined_image(filter_status, gdd_status, lab_light_status)
st.image(current_image, use_container_width=True)
