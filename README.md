# FrameExtractor-ObjectDetection

This project is a simple Python script that allows you to perform object detection on a specific frame of a video using OpenCV and a pre-trained object detection model. It's a useful tool for quickly analyzing the content of a video at a specific timestamp.

## Features

<ul>
<li><strong>Object Detection</strong>: Detects objects in a specified frame of a video using a pre-trained model.</li>
<li><strong>User-Friendly</strong>: You can specify the timestamp (hh:mm:ss) for the frame you want to analyze.</li>
<li><strong>Frame Saving</strong>: The detected objects are annotated, and you can save the frame as an image for later reference.</li>
</ul>

## Usage

### 1. Requirements:
<ul>
<li>Python</li>
<li>OpenCV (cv2)</li>
<li>Matplotlib (for displaying images)</li>
</ul>

#### 2. Setup:
Clone or download this repository to your local machine.

#### 3. Usage:
<ul>
<li>Run the "main.py" script.</li>
<li>You'll be prompted to enter a timestamp in the format hh:mm:ss.</li>
<li>The script will extract the frame at that timestamp from the video and perform object detection.</li>
<li>The annotated frame is displayed using Matplotlib, and it's also saved as an image in the project directory.</li>
</ul>

## Output
![Frame_at_0_2_1](https://github.com/vedika-gupta/FrameExtractor-ObjectDetection/assets/107416261/43c76aa1-f84e-4ef1-b4f9-faf4e8a15e33)

![Frame_at_0_2_1_with_detection](https://github.com/vedika-gupta/FrameExtractor-ObjectDetection/assets/107416261/9d8cd633-1077-4199-ac96-31ed7c15545f)
