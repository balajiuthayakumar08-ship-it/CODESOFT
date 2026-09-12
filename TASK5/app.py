import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Face Detection App",
    page_icon="😊"
)

# Title
st.title("😊 Face Detection App")
st.write("Upload an image to detect faces.")

# Upload image
uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open uploaded image
    image = Image.open(uploaded_file).convert("RGB")

    # Convert PIL image to NumPy array
    img_array = np.array(image)

    # Convert RGB image to grayscale
    gray = cv2.cvtColor(
        img_array,
        cv2.COLOR_RGB2GRAY
    )

    # Load OpenCV Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    # Check whether cascade loaded correctly
    if face_cascade.empty():
        st.error("Face detection model could not be loaded.")
    else:

        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Create copy for output
        output_image = img_array.copy()

        # Draw rectangle around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(
                output_image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                3
            )

        # Display result
        st.image(
            output_image,
            caption=f"Faces Detected: {len(faces)}",
            use_container_width=True
        )

        st.success(
            f"Successfully detected {len(faces)} face(s)!"
        )
