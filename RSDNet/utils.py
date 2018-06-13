import cv2
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


# ffmpeg_extract_subclip("/home/devendra/projects/my-DL-journey/RSDNet/data/video01.mp4", 00, 21, targetname="/home/devendra/projects/my-DL-journey/RSDNet/data/training_data/test.mp4")
# clip1 = VideoFileClip('').subclip(0,21)

vidcap = cv2.VideoCapture('/home/devendra/projects/my-DL-journey/RSDNet/data/video01.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1