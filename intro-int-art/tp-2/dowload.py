import yt_dlp

def descargar_audio(url, formato='mp3'):
    opciones = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': formato,
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

#Cancion1
Cancion1 = 'https://www.youtube.com/watch?v=e7n1wiuVlD0'
descargar_audio(Cancion1)


#Cancion2
Cancion2 = 'https://www.youtube.com/watch?v=vWVa-u8K0IE'
descargar_audio(Cancion2)

#Cancion3
Cancion3 = 'https://www.youtube.com/watch?v=jSjiwmseHAc'
descargar_audio(Cancion3)

#Cancion4
Cancion4 = 'https://www.youtube.com/watch?v=rhtJKnQ6jI0'
descargar_audio(Cancion4)

#Cancion5
Cancion5 = 'https://www.youtube.com/watch?v=Q0qq63iMbsA'
descargar_audio(Cancion5)

#Cancion6
Cancion6 = 'https://www.youtube.com/watch?v=OzOsTHyHlDY'
descargar_audio(Cancion6)

#Cancion7
Cancion7 = 'https://www.youtube.com/watch?v=YXM3YArwtVc'
descargar_audio(Cancion7)

#Cancion8
Cancion8 = 'https://www.youtube.com/watch?v=cYOdk3SSslQ'
descargar_audio(Cancion8)
