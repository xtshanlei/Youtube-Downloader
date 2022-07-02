import streamlit as st
from pytube import YouTube

st.title('YouTube Video Downloader')

youtube_url = st.text_input('Please paste the URL for your YouTube Video')
yt = YouTube(youtube_url)
downloaded_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

st.write(yt.title)
with open(downloaded_video, "rb") as video:
     btn = st.download_button(
             label="Download video",
             data=video,
             file_name="{}.mp4".format(yt.title),
             mime="video/mp4"
           )
st.image(yt.thumbnail_url)
