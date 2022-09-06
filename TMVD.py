import PySimpleGUI as sg
from yt_dlp import YoutubeDL
from pathlib import Path
from threading import Thread


class DownloadMusic(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        try:
            print("Baixando[]\n")
            out = str(
                Path.home()
                / "Documents"
                / "Trash downloader"
                / "Musics (trash)"
                / "%(title)s.%(ext)s"
            )
            with YoutubeDL(
                {
                    "ffmpeg_location": "ffmpeg.exe",
                    "outtmpl": out,
                    "quiet": True,
                    "no_warnings": True,
                    "format": "140",
                    "postprocessors": [
                        {"key": "FFmpegMetadata"},
                        {
                            "key": "EmbedThumbnail",
                            "already_have_thumbnail": True,
                        },
                    ],
                }
            ) as ydl:
                ydl.download(self.url)
                print("\nDonwload concluído[]")
        except:
            print("\nDownload mal sucedido, verifique a Url.")


class DownloadVideo(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        try:
            print("Baixando[]\n")
            out = str(
                Path.home()
                / "Documents"
                / "Trash downloader"
                / "Videos (trash)"
                / "%(title)s.%(ext)s"
            )
            with YoutubeDL(
                {
                    "ffmpeg_location": "ffmpeg.exe",
                    "outtmpl": out,
                    "quiet": True,
                    "no_warnings": True,
                    "format": "137+140/136+140/135+140/134+140/133+140/160+140/22/18",
                    "postprocessors": [
                        {"key": "FFmpegMetadata"},
                        {"key": "EmbedThumbnail"},
                    ],
                }
            ) as ydl:
                ydl.download(self.url)
                print("\nDonwload concluído[]")
        except:
            print("\nDownload mal sucedido, verifique a Url.")


layout = [
    [sg.Output(key="out", size=(50, 10),)],
    [
        sg.Button("Download Music", key="dm"),
        sg.Button("Download Video", key="dv"),
    ],
    [sg.Input(key="IN"), sg.Button("Exit", key="Close")],
]

window = sg.Window("Trash Downloader", layout)

while True:
    event, values = window.read()

    v = DownloadVideo(values["IN"])
    m = DownloadMusic(values["IN"])
    
    if event == "dv":
        if len(values["IN"]) > 0:
            v.start()
        else:
            print("Por favor digite algo.")

    if event == "dm":
        if len(values["IN"]) > 0:
            m.start()

        else:
            print("Por favor digite algo.")

    if event in (None, "Close"):
        break


window.close()

# new code looks sexy!
