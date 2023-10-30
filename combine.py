import cv2 as cv
import numpy as np
import os
from PIL import Image


def play_gif(gif_path):
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


# def play_mp4(mp4_path):
#     # Open the mp4 file
#     cap = cv.VideoCapture(mp4_path)

#     # Get the dimensions of the mp4
#     width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

#     # Set the window size and position
#     cv.namedWindow('mp4', cv.WINDOW_NORMAL)
#     cv.resizeWindow('mp4', width, height)
#     cv.moveWindow('mp4', 100, 100)

#     # Play the video
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             print("Can't receive frame")
#             break

#         # Show the current frame
#         cv.imshow('mp4', frame)

#         # Wait for a while
#         key = cv.waitKey(30)  # Adjust the delay as per your video's frame rate
#         if key & 0xFF == ord(' '):
#             break

#     # Close the window
#     cv.destroyAllWindows()


def search_and_play(file_name):
    # Set the folder paths
    gif_folder_path = '/Users/adrian/TIPS/t2s/videos/ASLVideos'
    mp4_folder_path = '/Users/adrian/TIPS/t2s/high_quality_videos'

    # Build the file paths
    gif_path = os.path.join(gif_folder_path, file_name + '.gif')
    mp4_path = os.path.join(mp4_folder_path, file_name + '.gif')

    # Search for GIF
    if os.path.isfile(gif_path):
        play_gif(gif_path)
    # If GIF not found, search for mp4
    elif os.path.isfile(mp4_path):
        play_gif(mp4_path)
    else:
        print("File not found")


if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    search_and_play(file_name)
