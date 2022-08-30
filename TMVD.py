import PySimpleGUI as sg
from yt_dlp import YoutubeDL
from pathlib import Path


def download_music(url):
    out = str(Path.home()/"Documents"/"Trash downloader"/"Musics (trash)"/"%(title)s.%(ext)s")
    with YoutubeDL({"ffmpeg_location":"ffmpeg.exe", "outtmpl": out, "format":"140"}) as ydl:
        ydl.download(url)

def download_video(url):
    out = str(Path.home()/"Documents"/"Trash downloader"/"Videos (trash)"/"%(title)s.%(ext)s")
    with YoutubeDL({"ffmpeg_location":"ffmpeg.exe", "outtmpl": out, "format":"bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b"}) as ydl:
        ydl.download(url)


layout = [[sg.Output(size = (50,10))]]


window = sg.Window("nada aqui", layout)

while True:
    event, values = window.read()

window.close()

#new code looks sexy!
