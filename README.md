# FrameExtractor-ObjectDetection

This project is a simple Python script that allows you to perform object detection on a specific frame of a video using OpenCV and a pre-trained object detection model. It's a useful tool for quickly analyzing the content of a video at a specific timestamp.

## Features

<ul>
<li><strong>Object Detection</strong>: Detects objects in a specified frame of a video using a pre-trained model.</li>
<li><strong>User-Friendly</strong>: You can specify the timestamp (hh:mm:ss) for the frame you want to analyze.</li>
<li><strong>Frame Saving</strong>: The detected objects are annotated, and you can save the frame as an image for later reference.</li>
</ul>

## Usage

#### 1. Requirements:
Python
OpenCV (cv2)
Matplotlib (for displaying images)

##### 2. Setup:
Clone or download this repository to your local machine.

##### 3. Usage:
<ul>
<li>Run the "main.py" script.</li>
<li>You'll be prompted to enter a timestamp in the format hh:mm:ss.</li>
<li>The script will extract the frame at that timestamp from the video and perform object detection.</li>
<li>The annotated frame is displayed using Matplotlib, and it's also saved as an image in the project directory.</li>
</ul>
