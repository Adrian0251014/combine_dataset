import cv2 as cv
import numpy as np
import os
from PIL import Image

# Set the GIF-related variables
selected_word = "about"
gif_folder_path = '/Users/adrian/TIPS/t2s/videos/ASLVideos'
gif_path = os.path.join(gif_folder_path, selected_word + '.gif')

# Check if the GIF file exists
if not os.path.isfile(gif_path):
    print("GIF file not found:", gif_path)
    exit()

# Read the GIF file
gif = Image.open(gif_path)

# Get the dimensions of the GIF
width, height = gif.size

# Set the window size and position
cv.namedWindow('GIF', cv.WINDOW_NORMAL)
cv.resizeWindow('GIF', width, height)
cv.moveWindow('GIF', 100, 100)

# Play the GIF
while True:
    # Get each frame of the GIF
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)

        # Convert the PIL image to OpenCV format
        frame_cv = cv.cvtColor(np.array(gif), cv.COLOR_RGBA2BGRA)

        # Display the current frame
        cv.imshow('GIF', frame_cv)

        # Wait for a while
        if 'duration' in gif.info:
            delay = gif.info['duration']
        else:
            delay = 100
        cv.waitKey(delay)

    # Press 'space' to exit the loop
    if cv.waitKey(1) & 0xFF == ord(' '):
        break

# Close the window
cv.destroyAllWindows()
