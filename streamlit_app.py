import streamlit as st
from PIL import Image
import os
import torch
import logging
from diffusers import StableDiffusionPipeline


def generate_image_from_text(text):
    model_id = "vinesmsuic/bg-visualnovel-v03"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    prompt = text
    image = pipe(prompt, height=512, width=512).images[0]
    image.save(r'C:\Users\Patel\OneDrive\Desktop\web\nightstreet.png')
# Streamlit app title
st.title("Image generator (made by students)")
search_query = st.text_input("Enter a search query:")
generate_image_from_text(search_query)

# Text input for the user to enter a file name (assuming the images are in the same directory as your script)

#st.text_input("Enter the image file name (e.g., image.jpg):")

# Check if the user has entered a file name\
if search_query:
  
    # Construct the full file path
    image_path = r'C:\Users\Patel\OneDrive\Desktop\web\nightstreet.png'

    # Check if the file exists
    if os.path.exists(image_path):
        # Display the image
        st.image(Image.open(image_path), use_column_width=True)
    else:
        st.write("Image not found. Make sure the image file is in the same directory as this script.")

# Add some additional content below the image
    st.write("Additional content goes here.")
