import cv2
from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os
import numpy as np
from PIL import Image, ImageDraw
import io
import base64
from typing import List
from ultralytics import YOLO
import torch

# Check if CUDA is available and set the device accordingly
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load the YOLOv8 model onto the GPU if available
model = YOLO('yolov8n.pt').to(device)  # You can use yolov8s.pt, yolov8m.pt, yolov8l.pt, or yolov8x.pt for larger models

# Draw bounding boxes on the image
def draw_bounding_boxes(image, boxes, labels):
    image_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(image_pil)

    for i, box in enumerate(boxes):
        xmin, ymin, xmax, ymax = box

        # Convert box coordinates to the actual image size
        xmin, xmax = int(xmin), int(xmax)
        ymin, ymax = int(ymin), int(ymax)

        # Draw the bounding box
        draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=3)

        # Draw the label
        label = labels[i]
        draw.text((xmin, ymin), label, fill="white")

    return image_pil

app = FastAPI()

@app.post("/detect_frame/")
async def detect_frame(file: UploadFile = File(...), selected_objects: List[str] = Form(...)):
    # Save the uploaded frame temporarily
    file_location = f"./temp_frame.jpg"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Open the saved image file using OpenCV
    frame = cv2.imread(file_location)

    # Convert the frame to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert the frame to a PIL image
    img_pil = Image.fromarray(frame_rgb)

    # Perform object detection using YOLOv8 on the GPU
    results = model.predict(img_pil, imgsz=640, iou=0.4, device=device)  # Ensure the device is set to GPU if available

    # Extracting outputs: boxes, scores, and class names
    boxes = results[0].boxes.xyxy.cpu().numpy()  # Get bounding boxes (xmin, ymin, xmax, ymax)
    scores = results[0].boxes.conf.cpu().numpy()  # Get confidence scores
    class_ids = results[0].boxes.cls.cpu().numpy().astype(int)  # Get class indices

    current_frame_labels = []
    current_frame_boxes = []
    detected_objects = []  # Store the detected object labels

    # Filter detections based on the user-selected objects and confidence threshold
    for i, class_id in enumerate(class_ids):
        label = model.names[class_id]  # Get the class name from YOLOv8
        if label in selected_objects and scores[i] > 0.5:  # Only consider relevant classes and high-confidence detections
            current_frame_labels.append(label)
            current_frame_boxes.append(boxes[i])
            detected_objects.append(label)  # Add detected object label

    # Draw bounding boxes on the frame
    image_with_boxes = draw_bounding_boxes(frame_rgb, current_frame_boxes, current_frame_labels)

    # Convert image to bytes
    buffered = io.BytesIO()
    image_with_boxes.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    # Delete the temporary image file
    os.remove(file_location)

    # Return the processed frame as a base64 string, the list of detected objects, and the processing device
    return {"frame": img_str, "detected_objects": detected_objects, "device": device}