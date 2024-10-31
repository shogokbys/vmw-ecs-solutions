# This repository is for code reference only and not ECS ready 

# Video Object Detection Web Application

This repository contains reference code for a web-based application that digests a video file and displays detected objects to the end user. The application is powered by the YOLOv8n object detection model, capable of detecting objects in video frames and presenting the results directly in the web browser.

## Overview

The application consists of two main components:

- **Frontend**: A Python-based web interface for end-user interaction, allowing users to upload video files.
- **Backend**: A YOLOv8-powered detection service that processes uploaded videos, detects objects frame-by-frame, and returns the results to the frontend for display.

The backend automatically detects if CUDA is available and utilises GPU acceleration if possible. If CUDA is not available, it defaults to CPU processing.

