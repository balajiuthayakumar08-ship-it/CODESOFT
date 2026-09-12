import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Load face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

st.title("😊 Face Detection App")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Convert RGB to BGR
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # Draw rectangle around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            img_array,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

    st.image(
        img_array,
        caption=f"Detected Faces: {len(faces)}",
        use_container_width=True
    )
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            img,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

    st.image(
        img,
        caption=f"Faces Detected: {len(faces)}",
        use_container_width=True
    )
