import flet as ft
from pytube import YouTube
from pytube import Playlist
from pytube import Search
import os

folder_dir = os.path.dirname(__file__)

def download(page, URL = f"https://www.youtube.com/watch?v=dQw4w9WgXcQ", video_format="MP3"):
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
    text = ft.Text()
    process = ft.Text()
    file_picker = ft.FilePicker()

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Enter the URL"
            page.update()
        else:
            url = txt_name.value
            process.value = "File is been downloaded...\n"
            text.value = f"Choose download option: {cg.value}"
            video_format = cg.value
            
            #download(page, url, video_format, page)
            page.update()

    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)
        curr_Dir.value = str(file_picker.result.path)
        page.update()

    file_picker = ft.FilePicker(on_result=on_dialog_result)

    txt_name = ft.TextField(label="Enter the URL")
    page.add(txt_name)

    cg = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="mp3", label="mp3"),
        ft.Radio(value="mp4", label="mp4"),
        ]))
    
    page.overlay.append(file_picker)
    getDir_button = ft.ElevatedButton("Choose directory", on_click=lambda _: selectDir())
    curr_Dir = ft.Text()
    submit_button = ft.ElevatedButton("Submit", on_click=btn_click)

    page.add(ft.Text("Choose download option:"), cg, getDir_button, curr_Dir, submit_button, text, process)

ft.app(target=main)