import streamlit as st
import subprocess
import os

st.title("play")


file_path = "/Users/yaokaidi/Desktop/output.h264"


converted_file_path = os.path.splitext(file_path)[0] + ".mp4"
command = ["ffmpeg", "-y", "-i", file_path, "-c:v", "libx264", "-preset", "ultrafast", "-crf", "23", "-c:a", "aac", "-b:a", "128k", converted_file_path]
subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if os.path.exists(converted_file_path):
    video_bytes = open(converted_file_path, 'rb').read()
    st.video(video_bytes)
