# Realtime Object Detection - with Video Upload
This repository contains configuration files to setup a demonstration environment to showcase the generic object detection application on ECS.
For demonstration purpose, this version is also configured to accept video upload to detect specific objects. This version also allows you to specify RTSP stream URL so that you can show the live demo using your webcam.
This application uses GPU/CUDA if available, and will use only CPU if not.

## Repository Contents

- **backend.yaml**: container configuration of object detection, using YOLOv8n model
- **frontend.yaml**: Object detection frontend application to provide GUI interaction for the users
- **workernode-config.yaml**: Since Object detection model requires decent amount of RAM, the worker node needs to be updated - 16-24GB should work fine as well

## What Object detection means in manufacturing?

ToBeUpdated

## Getting Started

1. Clone this repository
2. Depending on the timing, the host restart might be required to reflect the changes made on ec-worker
3. Access the frontend via `http://<worker-node>:30850`
4. enjoy!

https://github.com/user-attachments/assets/7ecfafb2-37ff-47d8-bea0-068dcdba9d39

![Screen Recording 2024-10-21 at 16 31 55 (1)](https://github.com/user-attachments/assets/e3cee224-ad19-4f18-b105-e2937bbf3bdc)

## Parameters
There are a few parameters you can select to make the experience better for your demo depending of your edge device, especially if the device doesn't have GPU it is recommended to tweek these parameters to show "moving" live demo.
- Image Size: default to 640 x 640, this is the size of the image that is sent to the backend. For CPU only deployment, 320 is recommended.
- Frame Skipping Interval: This determines how many frames are processed on the frontend so that it sends the data(image) to the backend. If you choose "1", every frame is sent to the backend, if you choose "3", a frame is sent every 3 frames it digests. For CPU only deployment, "10" is recommended.

<img width="1638" alt="image" src="https://github.com/user-attachments/assets/f011cc60-67c7-4d35-af69-2e5d36f15dfc">

<img width="1391" alt="image" src="https://github.com/user-attachments/assets/898d22f5-ec5f-4b7b-90b2-3dd78a6d4964">
