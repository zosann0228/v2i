
import os
import cv2

def main(video_path, output_dir, frame_skip):
  video = cv2.VideoCapture(video_path)
  if not video.isOpened():
    print("Could not open the video file:", video_path)
    return
  
  frame_number = 0
  image_name_base = os.path.join(output_dir, os.path.basename(video_path)) + "_frame"
  while True:
    ret, frame = video.read()
    if not ret:
      break
    if frame_number % frame_skip == 0:
      cv2.imwrite(image_name_base + str(frame_number) + ".png", frame)
    frame_number = frame_number + 1
  print("Frame written:", frame_number)

if __name__ == "__main__":
  video_path = input("Enter the video file:")
  output_dir = input("Enter the directory to save video frames:")
  frame_skip = input("How many frames do you want to skip?[default=0]:")
  
  if len(frame_skip) > 0:
    frame_skip = int(frame_skip)
  else:
    frame_skip = 0

  main(video_path, output_dir, frame_skip)
