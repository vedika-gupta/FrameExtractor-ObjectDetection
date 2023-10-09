import cv2

video = cv2.VideoCapture("video1.mp4")

nr_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.CAP_PROP_FPS)

timestamp = input('Enter timestamp in hh:mm:ss format')


# timestamp = '00:00:02.75'
timestamp_list = timestamp.split(':')
hh, mm, ss = map(float, timestamp_list)

frame_nr = int(hh * 3600 * fps + mm * 60 * fps + ss * fps)

# Print some information for debugging
print(f"Total frames in the video: {nr_frames}")
print(f"Frames per second (fps): {fps}")
print(f"Target frame number: {frame_nr}")

# Set the frame position and check if successful
video.set(1, frame_nr)
success, frame = video.read()

if success:
    print("Frame successfully retrieved.")
    cv2.imwrite(f'Frame_at_{int(hh)}_{int(mm)}_{int(ss)}.jpg', frame)
else:
    print("Error retrieving frame.")

# Release the video capture object
video.release()