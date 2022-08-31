import PySimpleGUI as sg
from yt_dlp import YoutubeDL
from pathlib import Path


def download_music(url):
    try:
        window["out"].update("Baixando")
        out = str(Path.home()/"Documents"/"Trash downloader"/"Musics (trash)"/"%(title)s.%(ext)s")
        with YoutubeDL({"ffmpeg_location":"ffmpeg.exe", "outtmpl": out, "format":"140"}) as ydl:
            ydl.download(url)
    except:
        window["out"].update("download mal sucedido, verifique a Url.")

def download_video(url):
    try:
        window["out"].update("Baixando")
        out = str(Path.home()/"Documents"/"Trash downloader"/"Videos (trash)"/"%(title)s.%(ext)s")
        with YoutubeDL({"ffmpeg_location":"ffmpeg.exe", "outtmpl": out, "format":"bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b"}) as ydl:
            ydl.download(url)
    except:
        window["out"].update("download mal sucedido, verifique a Url.")

def get_quality(url):
    pass

layout = [[sg.Output(key = "out",size = (50,10))],

[sg.ButtonMenu("Video", [["Video", "Music"], ["Video", "Music"]], key = "slctf") ],

[sg.Input(key = "IN"), sg.Button("download"), sg.Button("Exit", key="Close")]
]


window = sg.Window("nada aqui", layout)

while True:
    event, values = window.read()


    if event == "slctf":
        if values["slctf"] == "Music":
            values["slctf"] = "Music"
        else:
            values["slctf"] ="Video"
        

    if event == "download":
        if values["slctf"] == "Video":
            if len(values["IN"]) > 0:              
                download_video(values["IN"])
            else:
                window["out"].add("Por favor digite algo.")
        else:
            if len(values["IN"]) > 0:              
                download_music(values["IN"])
            else:
                window["out"].add("Por favor digite algo.")
            


    if event in (None, "Close"):
        break
    
    


window.close()

#new code looks sexy!
