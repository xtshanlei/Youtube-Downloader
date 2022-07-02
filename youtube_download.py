import streamlit as st
from pytube import YouTube

st.title('YouTube Video Downloader')

youtube_url = st.text_input('Please paste the URL for your YouTube Video')
yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
yt.streams.filter(progressive=True, file_extension='mp4')
        .order_by('resolution')
        .desc()
        .first()
        .download()
