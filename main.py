import streamlit as st
import os
from PIL import Image
import io
def main():
    st.title("GOES 16 Images")

    folder_path = "./GOES"


    if not os.path.exists(folder_path):
        st.error("Folder not found!")
        return
    folders_with_images = [root for root, _, files in os.walk(folder_path) if any(file.endswith(('.jpg', '.jpeg', '.png', '.gif')) and "" in file for file in files)]
    if len(folders_with_images) == 0:
        st.warning("No folders with images found in the directory!")
        return

    image_types = [["All Images", "Full Color", "Blue", "Red", "Near Infrared", "Cirrus", "Snow/Ice", "Cloud Particle Size", "Thermal", "Upper-level water vapor", "Mid-level water vapor", "Lower-level water vapor", "Cloud-top", "Ozone-level", "Infrared-less sensitive", "Infrared", "Infrared-sensitive", "Carbon Dioxide"],["", "_FC_", "_1_", "_2_", "_3_", "_4_", "_5_", "_6_", "_7_", "_8_", "_9_", "_10_", "_11_", "_12_", "_13_", "_14_", "_15_", "_16_"]]

    folder_selected = st.sidebar.selectbox("Select a folder", folders_with_images)
    image_type = st.sidebar.selectbox("Select image type", image_types[0])
    file_image_type = image_types[1][image_types[0].index(image_type)]
    st.sidebar.write("Timelapse feature is not recommended for all images")
    output_type = st.sidebar.selectbox("Select a display type", ["Timelape", "Images"])

    image_files = [os.path.join(folder_selected, file) for file in os.listdir(folder_selected) if file.endswith(('.jpg', '.jpeg', '.png', '.gif')) and file_image_type in file]

    if len(image_files) == 0:
        st.warning("No images found in the selected folder!")
        return
    
    st.write(folder_selected)
    if output_type == "Timelape":
        
        st.subheader("Timelapse GIF")
        create_timelapse(folder_selected, file_image_type)

    if output_type == "Images":
        
        st.subheader("Images")
        for img_file in image_files:
            st.image(img_file, use_column_width=True)
            st.download_button("Download file", img_file)
def create_timelapse(folder_path, file_image_type):
    image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png', '.gif')) and file_image_type in file]
    image_files.sort(key=os.path.getmtime)
    if len(image_files) == 0:
        st.warning("No image files found in the folder!")
        return
    
    images = [Image.open(img_file).resize((800, 600)) for img_file in image_files]
    gif_bytes = create_gif(images)
    st.image(gif_bytes)
def create_gif(images):
    gif_bytes = io.BytesIO()
    images[0].save(gif_bytes, format="GIF", save_all=True, append_images=images[1:], loop=0, duration=100)
    return gif_bytes.getvalue()
if __name__ == "__main__":
    main()
