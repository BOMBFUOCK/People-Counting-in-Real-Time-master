
st.title("播放H264视频示例")

# 获取本地H264文件的路径
file_path = "/Users/yaokaidi/Desktop/output.h264"

# 将H264文件转换为MP4格式
converted_file_path = os.path.splitext(file_path)[0] + ".mp4"
command = ["ffmpeg", "-y", "-i", file_path, "-c:v", "libx264", "-preset", "ultrafast", "-crf", "23", "-c:a", "aac", "-b:a", "128k", converted_file_path]
subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 检查转换后的文件是否存在
if os.path.exists(converted_file_path):
    # 在Streamlit应用程序中呈现视频
    video_bytes = open(converted_file_path, 'rb').read()
    st.video(video_bytes)
