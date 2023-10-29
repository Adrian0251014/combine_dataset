import cv2 as cv
import os

# Set the mp4-related variables
selected_word = "ABHOR"  # Choose a default video name
mp4_folder_path = '/Users/adrian/TIPS/t2s/high_quality_videos'  # Set your video folder path
mp4_path = os.path.join(mp4_folder_path, selected_word + '.mp4')

# Check if the mp4 file exists
if not os.path.isfile(mp4_path):
    print("mp4 file not found:", mp4_path)
    exit()

# Open the mp4 file
cap = cv.VideoCapture(mp4_path)

# Get the dimensions of the mp4
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Set the window size and position
cv.namedWindow('mp4', cv.WINDOW_NORMAL)
cv.resizeWindow('mp4', width, height)
cv.moveWindow('mp4', 100, 100)

# Play the video
while cap.isOpened():
    ret, frame = cap.read()
    # if not ret:
    #     print("Can't receive frame")
    #     break

    # Show the current frame
    cv.imshow('mp4', frame)

    # Wait for a while
    key = cv.waitKey(30)  # Adjust the delay as per your video's frame rate
    if key & 0xFF == ord(' '):
        break

# Close the window
cv.destroyAllWindows()