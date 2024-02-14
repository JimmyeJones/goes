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

    folders_with_images = [root for root, _, files in os.walk(folder_path) if any(file.endswith(('.jpg', '.jpeg', '.png', '.gif')) and "FC" in file for file in files)]
    
    if len(folders_with_images) == 0:
        st.warning("No folders with images found in the directory!")
        return

    image_types = [["Full Color", "Red", "Near Infrared", "Cirrus", "Snow/Ice", "Cloud Particle Size", "Thermal", "Mid-level water vapor", "Lower-level water vapor", "Cloud-top", "Ozone-level", "Infrared-less sensitive", "Infrared", "Infrared-sensitive", "Carbon Dioxide"],["G16_FC", "G16_2", "G16_3", "G16_4", "G16_5", "G16_6", "G16_7", "G16_8", "G16_9", "G16_10", "G16_11", "G16_12", "G16_13", "G16_14", "G16_15", "G16_16"]]
  
    folder_selected = st.sidebar.selectbox("Select a folder", folders_with_images)
    image_type = st.sidebar.selectbox("Select image type", image_types[0])
    file_image_type = image_types[1][len(image_type)]
    st.sidebar.text(file_image_type)
    image_files = [os.path.join(folder_selected, file) for file in os.listdir(folder_selected) if file.endswith(('.jpg', '.jpeg', '.png', '.gif')) and "FC" in file]
    
    if len(image_files) == 0:
        st.warning("No images found in the selected folder!")
        return
    
    st.write(f"Selected folder: {folder_selected}")

    st.subheader("Timelapse GIF")
    create_timelapse(folder_selected, )

    st.subheader("Images")
    for img_file in image_files:
        st.image(img_file, use_column_width=True)

def create_timelapse(folder_path, image_type):
    image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png', '.gif')) and image_type in file]
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
