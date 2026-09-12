import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
import urllib.request

st.set_page_config(page_title="Face Detection App", layout="centered")
st.title("Face Detection App")

# ---- Load Haar Cascade safely ----
CASCADE_PATH = "haarcascade_frontalface_default.xml"

@st.cache_resource
def load_cascade():
    # If the xml file is not already in the project folder, download it once
    if not os.path.exists(CASCADE_PATH):
        url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
        urllib.request.urlretrieve(url, CASCADE_PATH)

    cascade = cv2.CascadeClassifier(CASCADE_PATH)

    if cascade.empty():
        st.error("Failed to load Haar Cascade classifier.")
        st.stop()

    return cascade

face_cascade = load_cascade()

# ---- Upload Image ----
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV image
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img_bgr, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Convert back to RGB for display
    result_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    st.image(result_img, caption=f"Detected {len(faces)} face(s)", use_container_width=True)

    if len(faces) == 0:
        st.warning("No faces detected in this image.")
    else:
        st.success(f"{len(faces)} face(s) detected!")
