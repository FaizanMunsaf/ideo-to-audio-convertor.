# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 04:28:17 2023

@author: SA
"""

from moviepy.editor import *

# Load the video file
video = VideoFileClip(r"C:\Users\SA\Desktop\Geeflow Musab-Hasbi Rabbi (Mexnes Trap).mp4")

# Extract the audio and save as an mp3 file
audio = video.audio
audio.write_audiofile(r"C:\Users\SA\Desktop\audio.mp3")
