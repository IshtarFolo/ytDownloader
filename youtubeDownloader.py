import os
from pytube import YouTube
import moviepy.editor as mpe
import PySimpleGUI as sg
from pathlib import Path

#***GUI***
#le layout avec texte, barre d'input et bouton
layout=[[sg.Text("Entrez un URL ici")],
        [sg.InputText('', key='url')], 
        [sg.Button("Envoyer")]]

#le titre de la fenetre et passation du layout dans la fenetre
window = sg.Window("Youtube Downloader", layout)

#Si la fenetre est ouverte:
while True:
    event, values = window.read()

#Si l'utilisateur appuie sur OK
    if event == "Envoyer":

        #**Debut du programme**
        #Le liens a telecharger
        link = str(values['url']) #lien test:'https://www.youtube.com/watch?v=GL9vi4hTQQU&t=9s&ab_channel=RedLetterMedia'
        yt = YouTube(link)

        #print nom du video
       # print(yt.title)
        #print nbr de vues
       # print(yt.views)

        def get_resolution(s):
            return int (s.resolution[:-1])

    stream = max(
        filter(lambda s: get_resolution(s) <= 1080, 
               filter(lambda s: s.type == 'video', yt.fmt_streams)), 
    key=get_resolution)
    # accelerate download birate
    stream.bitrate *= 2

            
    stream.download(Path.home(), 'yt.mp4')
    #**Fin du programme**#

    #Si l'utilisateur ferme la fenetre:
    if event == sg.WIN_CLOSED:
        exit()
    break
