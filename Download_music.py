from pytube import YouTube
import customtkinter
import os

def Download():
    
    path_directory = os.getcwd() + "/Download_from_python"
    url = lineEdit.get()
    yt = YouTube(url)

    audio_only = yt.streams.get_audio_only()

    audio_only.download(path_directory)

    label_file_name = customtkinter.CTkLabel(janela, text=f"Música baixada: {audio_only.default_filename}", text_color="blue")
    label_file_name.place(x= 25, y= 450)

    path = path_directory

    arquivos = os.listdir(path)
    for file in arquivos:
        if file.endswith(".mp4"):
            caminho_original = os.path.join(path, file)
            novo_nome = file.replace(".mp4", ".mp3")
            novo_caminho = os.path.join(path, novo_nome) 
            os.rename(caminho_original, novo_caminho)
            print(f"Música convertida de .mp4 para .mp3: {file}")
        



janela = customtkinter.CTk()
customtkinter.set_appearance_mode("dark-blue")
customtkinter.set_default_color_theme("blue")


janela.title("Download musics from YouTube")

janela.geometry("800x500")


l_show = customtkinter.CTkLabel(janela, text_color="black", font=("Georgia", 35), text="Baixe aqui suas músicas")
l_show.place(x=215, y=35)


explain = customtkinter.CTkLabel(janela, text_color="black",font=("Georgia", 15), text="Coloque a url da música que deseja baixar\n e clique no botão abaixo para obter\n na melhor qualidade de áudio")
explain.place(x=255, y=135)





lineEdit = customtkinter.CTkEntry(janela, width=300, height=50, corner_radius=25, placeholder_text="Url Of Music")

lineEdit.place(x=250, y=230)


button_download = customtkinter.CTkButton(janela,width=200, height=50 ,corner_radius=25, hover_color="white", text_color="black", text="Download", fg_color="grey", command=Download)

button_download.place(x=295, y=350)






janela.mainloop()


