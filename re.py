

import streamlit as st
import pandas as pd
import subprocess
import os
import matplotlib.pyplot as plt


st.title("Intelligent monitoring of the number of entrants and exits")
st.header("")
pwd = "/People-Counting-in-Real-Time-master/People-Counting-in-Real-Time-master/Log.csv"

df = pd.read_csv(pwd)
        
# "with" notation
with st.sidebar:
    st.sidebar.title("Data of People Counting")
    st.sidebar.markdown("This application is a Streamlit dashboard to analyze the data of people in live video")
    st.sidebar.write("End Time")
    time = df.iloc[0,0]
    st.sidebar.write(time)
    st.sidebar.write("Count the Enter people and Out people")
    people = df.iloc[df.shape[0] - 1,1]
    people2 = df.iloc[df.shape[1] - 1,2]
    y = [people,people2]
    x = ['In','Out']
    fig, ax = plt.subplots()
    ax.set_xlabel("People behavior", fontsize=16)
    ax.set_ylabel("Count", fontsize=16)
    ax.bar(x,y)
    st.pyplot(fig)

file_path = "/People-Counting-in-Real-Time-master/People-Counting-in-Real-Time-master/output1.h264"

converted_file_path = os.path.splitext(file_path)[0] + ".mp4"
command = ["ffmpeg", "-y", "-i", file_path, "-c:v", "libx264", "-preset", "ultrafast", "-crf", "23", "-c:a", "aac", "-b:a", "128k", converted_file_path]
subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if os.path.exists(converted_file_path):
    video_bytes = open(converted_file_path, 'rb').read()
    st.video(video_bytes)