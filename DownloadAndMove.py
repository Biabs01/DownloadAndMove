import sys
import random
import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\biabs\Downloads" #Adicione o caminho da sua pasta de Download
to_dir = "C:\Users\biabs\Downloads\Arquivos_Documentos" #Crie uma pasta "Arquivos_Documentos"

dir_tree = {
    "Arquivos_Imagem": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Arquivos_Video": ['.mpg','.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Arquivos_Documentos": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Arquivos_Setup": ['.exe', '.bin', '.cmd', '.msi', '.dmg']

}

# Classe Gerenciadora de Eventos
class FileMovementHandler():

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)

        for key, value in dir_tree.items():

            if extension in value:
                file_name = os.path.basename(event.src_path)

                print("Baixado " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/'
                path3 = to_dir + '/' + file_name

                if os.path.exists(path2):

                    print("Diretório Existe...")
                    print("Movendo " + file_name + "...")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    
                    print("Criando Diretório...")
                    os.makedirs(path2)
                    print("Movendo " + file_name + "...")
                    shutil.move(path1, path3)
                    time.sleep(1)

        print(event)

# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

#Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
        print("interrompido")
        observer.stop()