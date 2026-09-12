import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Face Detection App")

st.title("😊 Face Detection App")
st.write("Upload an image to detect faces.")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    image_array = np.array(image)

    gray = cv2.cvtColor(
        image_array,
        cv2.COLOR_RGB2GRAY
    )

    cascade_file = (
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    face_cascade = cv2.CascadeClassifier(cascade_file)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    result = image_array.copy()

    for (x, y, w, h) in faces:
        cv2.rectangle(
            result,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

    st.image(
        result,
        caption=f"Faces Detected: {len(faces)}"
    )
