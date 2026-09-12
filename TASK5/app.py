
import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("😊 Face Detection App")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    # Convert image to numpy array
    img_array = np.array(image)

    # Convert RGB to Gray
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Load face detection model
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(
            img_array,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

    # Display result
    st.image(
        img_array,
        caption=f"Faces Detected: {len(faces)}",
        use_container_width=True
    )
