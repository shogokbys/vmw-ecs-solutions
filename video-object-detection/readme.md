# Realtime Object Detection - with Video Upload
This repository contains configuration files to setup a demonstration environment to showcase the generic object detection application on ECS.
For demonstration purpose, this version is configured to accept video upload rather than digesting the data from streaming media e.g. RTSP.

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
