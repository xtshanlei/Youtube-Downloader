import streamlit as st
from pytube import YouTube

st.title('YouTube Video Downloader')
st.write('----by Yulei')

youtube_url = st.text_input('Please paste the URL for your YouTube Video')

if youtube_url:
    yt = YouTube(youtube_url)
    with st.spinner('Processing....please wait'):
        downloaded_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        downloaded_caption = yt.Caption.download(filename_prefix=yt.title)
    st.success("Done! Click the 'Download video' button to download your video!")


    st.header(yt.title)
    with open(downloaded_video, "rb") as video:
         btn = st.download_button(
                 label="Download video",
                 data=video,
                 file_name="{}.mp4".format(yt.title),
                 mime="video/mp4"
               )
    st.image(yt.thumbnail_url)
    st.write(downloaded_caption)
