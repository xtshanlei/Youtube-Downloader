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

    st.success("Done! Click the 'Download video' button to download your video!")

    st.header(yt.title)
    with open(downloaded_video, "rb") as video:
         d_btn = st.download_button(
                 label="Download video",
                 data=video,
                 file_name="{}.mp4".format(yt.title),
                 mime="video/mp4"
               )

    language_list =[language.lang for language in caption_language]
    lang_code_list = [language.code for language in caption_language]
    caption_selected = st.multiselect(
                                     'Choose the caption you want to download',
                                     language_list,
                                     [language_list[0]])

    downloaded_caption = yt.captions.get_by_language_code('zh-TW').xml_captions
    caption_button = st.download_button(
                                        label="Download caption/subtitle",
                                        data=downloaded_caption,
                                        file_name="{}.xml".format(yt.title),
                                        mime="text/xml"
                                      )

    st.image(yt.thumbnail_url)
