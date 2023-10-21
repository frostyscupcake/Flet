import flet as ft
from pytube import YouTube
from pytube import Playlist
from pytube import Search
import os

folder_dir = os.path.dirname(__file__)

def download(URL = f"https://www.youtube.com/watch?v=dQw4w9WgXcQ", video_format="MP3"):
    video = YouTube(URL)
    available_itags = [stream.itag for stream in video.streams]
    print("Available itags:", available_itags)

    if video_format == "MP4":
        st = video.streams.get_by_itag(22)
        print("downloading video")
    else:
        st = video.streams.get_by_itag(249)
        print("downloading audio")

    st.download(output_path=folder_dir)



def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Enter the URL"
            page.update()
        else:

            url = txt_name.value
            page.add(ft.Text(f"video is been downloaded"))
            #download(URL=url)

    txt_name = ft.TextField(label="Enter the URL")
    

    page.add(txt_name, ft.ElevatedButton("Submit", on_click=btn_click))

ft.app(target=main)