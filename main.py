import cv2
import matplotlib.pyplot as plt

# Function to perform object detection on a given frame
def perform_object_detection(frame):
    config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    frozen_model = 'frozen_inference_graph.pb'

    model = cv2.dnn_DetectionModel(frozen_model, config_file)

    classLabels = []
    file_name = 'labels.txt'
    with open(file_name, 'rt') as fpt:
        classLabels = fpt.read().rstrip('\n').split('\n')

    print(classLabels)

    model.setInputSize(320, 320)
    model.setInputScale(1.0 / 127.5)
    model.setInputMean((127.5, 127.5, 127.5))
    model.setInputSwapRB(True)

    # Perform object detection on the frame
    Classindex, confidence, bbox = model.detect(frame, confThreshold=0.5)

    font_scale = 3
    font = cv2.FONT_HERSHEY_PLAIN

    for ClassInd, conf, boxes in zip(Classindex.flatten(), confidence.flatten(), bbox):
        cv2.rectangle(frame, boxes, (255, 0, 0), 2)
        cv2.putText(frame, classLabels[ClassInd - 1], (boxes[0] + 10, boxes[1] + 40), font, fontScale=font_scale,
                    color=(0, 255, 0), thickness=3)

    return frame

# Load the video
video = cv2.VideoCapture("video1.mp4")

# Get video information
nr_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.CAP_PROP_FPS)

# Get user input for timestamp
timestamp = input('Enter timestamp in hh:mm:ss format: ')

# Parse the timestamp
timestamp_list = timestamp.split(':')
hh, mm, ss = map(float, timestamp_list)

# Calculate the target frame number
frame_nr = int(hh * 3600 * fps + mm * 60 * fps + ss * fps)

# Set the frame position
video.set(1, frame_nr)

# Read the frame
success, frame = video.read()

if success:
    print("Frame successfully retrieved.")
    # Perform object detection on the frame
    frame_with_detection = perform_object_detection(frame)
    
    # Display the frame with detection
    plt.imshow(cv2.cvtColor(frame_with_detection, cv2.COLOR_BGR2RGB))
    plt.show()

    # Save the frame with detection
    cv2.imwrite(f'Frame_at_{int(hh)}_{int(mm)}_{int(ss)}_with_detection.jpg', frame_with_detection)
else:
    print("Error retrieving frame.")

# Release the video capture object
video.release()