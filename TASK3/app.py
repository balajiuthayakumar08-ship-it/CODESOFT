import streamlit as st
from PIL import Image

st.set_page_config(page_title="Image Captioning AI")

st.title("🖼️ Image Captioning AI")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")

    width, height = image.size

    if width > height:
        caption = "A landscape image."
    elif height > width:
        caption = "A portrait image."
    else:
        caption = "A square image."

    st.success("Caption:")
    st.write(caption)
