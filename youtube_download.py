import streamlit as st
from pytube import YouTube

st.title('YouTube Video Downloader')
st.write('----by Yulei')

youtube_url = st.text_input('Please paste the URL for your YouTube Video')


def get_itag_by_res(yt):
    mp4 = yt.streams.filter(progressive=True, file_extension='mp4')
    available_streams = mp4.order_by('resolution').desc().first()
    st.write(available_streams.filesize)
    st.write(available_streams[0].fps)
    stream_list = [stream.res for stream in available_streams]
    stream_itag_list = [stream.itag for stream in available_streams]
    return stream_list, stream_itag_list
def extract_video(yt,itag):
    downloaded_video = yt.streams.get_by_itag(itag).download()
    caption_language= yt.captions
    return downloaded_video,caption_language

if youtube_url:
    yt = YouTube(youtube_url)
    stream_list,stream_itag_list = get_itag_by_res(yt)
    st.write(stream_list)
    with st.spinner('Processing....please wait'):
        downloaded_video,caption_language=extract_video(yt)
    st.success("Done! Click the 'Download video' button to download your video!")
    st.header(yt.title)
    with open(downloaded_video, "rb") as video:
         d_btn = st.download_button(
                 label="Download video",
                 data=video,
                 file_name="{}.mp4".format(yt.title),
                 mime="video/mp4"
               )
    if caption_language:
        language_list =[language.name for language in caption_language]
        lang_code_list = [language.code for language in caption_language]
        caption_selected = st.selectbox(
                                         'Choose the language of the caption/subtitle you want to download',
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
