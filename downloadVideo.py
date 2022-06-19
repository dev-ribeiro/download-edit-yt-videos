from pytube import YouTube,streams

url = input(str("Digite a url do vídeo aqui: "))
yt = YouTube(url)
print("Iniciando...")
print(yt.title + "foi iniciado o download...")
video = yt.streams.get_highest_resolution()
video.download()
print("Download do vídeo concluído com sucesso")