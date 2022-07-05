import streamlit as st
from pytube import YouTube

st.title('YouTube Video Downloader')
st.write('----by Yulei')

youtube_url = st.text_input('Please paste the URL for your YouTube Video')

@st.cache
def extract_video():
    yt = YouTube(youtube_url)
    downloaded_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    caption_language= yt.captions

if youtube_url:
    with st.spinner('Processing....please wait'):
        extract_video()
    st.success("Done! Click the 'Download video' button to download your video!")
    st.header(yt.title)
    with open(downloaded_video, "rb") as video:
         d_btn = st.download_button(
                 label="Download video",
                 data=video,
                 file_name="{}.mp4".format(yt.title),
                 mime="video/mp4"
               )

    language_list =[language.name for language in caption_language]
    lang_code_list = [language.code for language in caption_language]
    caption_selected = st.selectbox(
                                     'Choose the language you want to download for your video',
                                     language_list,
                                    )
    language_index = language_list.index(caption_selected)

    downloaded_caption = yt.captions.get_by_language_code(lang_code_list[language_index]).xml_captions
    caption_button = st.download_button(
                                        label="Download caption/subtitle",
                                        data=downloaded_caption,
                                        file_name="{}.xml".format(yt.title),
                                        mime="text/xml"
                                      )

    st.image(yt.thumbnail_url)
