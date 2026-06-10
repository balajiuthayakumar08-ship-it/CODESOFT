import streamlit as st
from PIL import Image
from transformers import pipeline

st.set_page_config(page_title="Image Captioning AI")

st.title("🖼️ Image Captioning AI")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Generating Caption..."):
        from transformers import BlipProcessor, BlipForConditionalGeneration

        result = captioner(image)

    st.success("Caption Generated!")
    st.write("### Caption:")
    st.write(result[0]["generated_text"])
