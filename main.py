import flet as ft
from pytube import YouTube
import os


def download(URL = f"https://www.youtube.com/watch?v=dQw4w9WgXcQ", video_format="MP4", folder_dir= os.path.dirname(__file__)):
    video = YouTube(URL)
    print(folder_dir)
    if video_format == "MP4":
        st = video.streams.get_by_itag(22)
        print("downloading video")
    else:
        st = video.streams.get_by_itag(249)
        print("downloading audio")

    st.download(output_path=folder_dir)

def main(page):
    text = ft.Text()
    title = ft.Text(value="Meovv", size=60, weight=ft.FontWeight.BOLD, text_align="CENTER")
    sub_title = ft.Text(value="Youtube Downloader", size=30, text_align="CENTER")
    progress = ft.Text()
    file_picker = ft.FilePicker()

    page.window_width = 400  
    page.window_height = 600      
    page.window_resizable = False

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Enter the URL"
            page.update()
        else:
            url = txt_name.value
            progress.value = "Video is downloading...\n"
            text.value = f"Choose download option: {cg.value}"
            video_format = cg.value
            directory = curr_Dir.value
            print(url, video_format, directory)
            page.update()
            download(url, video_format, directory)

            progress.value += "Video has been downloaded\n"
            page.update()

    def on_dialog_result(e: ft.FilePickerResultEvent):
        curr_Dir.value = str(file_picker.result.path)
        page.update()

    def selectDir():
        file_picker.get_directory_path()
         

    file_picker = ft.FilePicker(on_result=on_dialog_result)
    txt_name = ft.TextField(label="Enter the URL")
    page.add(title, sub_title, txt_name)

    cg = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="MP3", label="MP3"),
        ft.Radio(value="MP4", label="MP4"),
        ]))
    
    page.overlay.append(file_picker)
    getDir_button = ft.ElevatedButton("Choose directory", on_click=lambda _: selectDir())
    curr_Dir = ft.Text()
    submit_button = ft.ElevatedButton("Download", on_click=btn_click)

    page.add(ft.Text("Choose download option:"), cg, getDir_button, submit_button, curr_Dir, text, progress)
ft.app(target=main)