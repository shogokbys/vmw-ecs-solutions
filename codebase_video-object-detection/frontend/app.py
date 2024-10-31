import os
import streamlit as st
import requests
from PIL import Image
import base64
import io
import cv2
import tempfile
import time

# Get the backend URL from an environment variable
backend_url = os.getenv("BACKEND_URL", "http://localhost:8000")

# Streamlit UI
st.title("Real-time Object Detection with Alarm Feature")
st.write("Upload a video file, choose objects to detect, and select objects for which you want an alarm.")

# COCO class names for the objects to detect
coco_class_names = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
    'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
    'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
    'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
    'potted plant', 'bed', 'dining table', 'toilet', 'TV', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
    'hair drier', 'toothbrush'
]

# Let the user select objects to detect
selected_objects = st.multiselect("Select objects to detect:", coco_class_names, default=coco_class_names[:5])

# Let the user select objects to be alarmed
alarmed_objects = st.multiselect("Objects to be alarmed:", selected_objects)

# Upload video file
uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mov", "avi"])

# If the user uploads a video and selects objects to detect
if uploaded_file and selected_objects:
    # Open the uploaded video file
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())
    video = cv2.VideoCapture(tfile.name)

    stframe = st.empty()  # Placeholder for displaying frames
    alarm_frame = st.empty()  # Placeholder for the alarm message
    snapshot_frame = st.empty()  # Placeholder for displaying the snapshot when an alarm is triggered

    alarm_triggered_time = None  # To track when the alarm was triggered

    # Process the video frame by frame
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        # Convert frame to bytes and send it to the FastAPI server
        _, img_encoded = cv2.imencode('.jpg', frame)
        files = {'file': img_encoded.tobytes()}
        data = {'selected_objects': selected_objects}

        # Use the backend URL from the environment variable to make the request
        response = requests.post(f"{backend_url}/detect_frame/", files=files, data=data)

        if response.status_code == 200:
            frame_data = response.json()["frame"]
            detected_objects = response.json().get("detected_objects", [])
            device_used = response.json().get("device", "CPU")  # Get the device used from the backend

            img_bytes = base64.b64decode(frame_data)
            img = Image.open(io.BytesIO(img_bytes))

            # Display the detected frame with bounding boxes (as a video)
            stframe.image(img, caption=f"Processed on: {device_used}", use_column_width=True)

            # Check if any alarmed objects are detected
            alarmed_detected = [obj for obj in detected_objects if obj in alarmed_objects]

            if alarmed_detected and alarm_triggered_time is None:
                # Alarm triggered: show the message and snapshot
                alarm_triggered_time = time.time()  # Track when the alarm was triggered

                # Display the alarm message in bold, big font
                alarm_message = ", ".join(alarmed_detected) + " detected!"
                alarm_frame.markdown(f"<h1 style='color:red; font-size:40px;'>{alarm_message}</h1>", unsafe_allow_html=True)

                # Display the detected frame separately as a snapshot
                snapshot_frame.image(img, caption="Snapshot of Detected Frame", use_column_width=True)
            # Clear the alarm after 5 seconds
            if alarm_triggered_time and time.time() - alarm_triggered_time > 5:
                alarm_frame.empty()
                snapshot_frame.empty()
                alarm_triggered_time = None  # Reset the alarm trigger
    video.release()
else:
    st.write("Please upload a video and select objects to detect.")