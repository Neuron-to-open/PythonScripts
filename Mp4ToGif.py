# /****************************************************************************
# * Author: Neuron-to-open
# * Date: 2024/7/20
# * Python : 3.11
# * 系统版本： Windows 11 家庭版 20H2
# * IDE: Pycharm
# * 编程语言: Python
# * =========== ====== ===== ==============================================
# * @Copyright (C) Yijiayi All Rights reserved
# *****************************************************************************/

import moviepy.editor as mpy
from PIL import Image

# Ensure compatibility with PIL version
if hasattr(Image, 'Resampling'):
    resampling_method = Image.Resampling.LANCZOS
else:
    resampling_method = Image.LANCZOS

# Load the video file
clip = mpy.VideoFileClip(r"C:\Users\24887\Desktop\408\mp4\顺序表的创建.mp4")

# Speed up the video
clip = clip.speedx(2)

# # Resize the video to reduce the file size (adjust width and height as needed)
# clip_resized = clip.resize(height=400)  # Adjust the height as needed

# Write the GIF with a reduced frame rate to help keep it under 20MB
clip.write_gif(r"C:\Users\24887\Desktop\408\gif\顺序表的创建.gif")

print("GIF created successfully!")

