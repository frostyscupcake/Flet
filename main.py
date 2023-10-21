import flet as ft

def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Enter the URL"
            page.update()
        else:
            url = txt_name.value
            page.clean()
            page.add(ft.Text(f"{url}"))

    txt_name = ft.TextField(label="Enter the URL")

    page.add(txt_name, ft.ElevatedButton("Submit", on_click=btn_click))

ft.app(target=main)