import streamlit as st
from pytube import YouTube

st.title('YouTube Video Downloader')
st.write('----by Yulei')

youtube_url = st.text_input('Please paste the URL for your YouTube Video')

if youtube_url:
    yt = YouTube(youtube_url)
    with st.spinner('Processing....please wait'):
        downloaded_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        caption_language= yt.captions
        downloaded_caption = yt.captions.get_by_language_code('zh-TW').xml_captions
    st.success("Done! Click the 'Download video' button to download your video!")
    st.write(type(downloaded_caption))

    st.header(yt.title)
    with open(downloaded_video, "rb") as video:
         btn = st.download_button(
                 label="Download video",
                 data=video,
                 file_name="{}.mp4".format(yt.title),
                 mime="video/mp4"
               )
    with open("caption.xml", "w") as cap:
        cap.write("test")

    st.image(yt.thumbnail_url)
    with open("caption.xml") as t:
        st.write(t)
