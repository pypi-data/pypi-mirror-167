# Import required modules.
import typer  # Turns mait_manager into a CLI tool.
import socket  # Networking.
from alive_progress import alive_bar  # Progress bar.
import os  # Executing commands.
import json  # For opening JSONs.
import shutil  # For zipping folders.
from time import sleep  # For waiting on action
import tempfile

app = typer.Typer(help="Package manager for text adventure games.", name="mait")

HOST = '54.159.187.169'
PORT = 6440  # TCP is 8081, no longer functional.

SERVER = (HOST, PORT)

print(r"""
     /\__\         /\  \          ___        /\  \    
    /::|  |       /::\  \        /\  \       \:\  \   
   /:|:|  |      /:/\:\  \       \:\  \       \:\  \  
  /:/|:|__|__   /::\~\:\  \      /::\__\      /::\  \ 
 /:/ |::::\__\ /:/\:\ \:\__\  __/:/\/__/     /:/\:\__\
 \/__/~~/:/  / \/__\:\/:/  / /\/:/  /       /:/  \/__/
       /:/  /       \::/  /  \::/__/       /:/  /     
      /:/  /        /:/  /    \:\__\       \/__/      
     /:/  /        /:/  /      \/__/                  
     \/__/         \/__/                              
-------------------------------------------------------------     """)



@app.command(help="Lists all packages in mait's registry.")
def list():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b'0', SERVER)  # Send message
        try:
            response = s.recvfrom(1024)  # Response from server.
            print(response[0].decode('utf-8').replace(r'\n', '\n').replace('./packages/', ''))
        except socket.timeout:
            pass


@app.command(help="Creates a temporary file from requested package and executes it.")
def play(game: str):
    temp_dir = tempfile.TemporaryDirectory()

    def execute(game):
        with open(f'{temp_dir.name}/{game}/mait.json', 'r') as r:
            data = json.load(r)

        try:
            short = data['short']
        except:
            short = "This package doesn't provide a short description."

        try:
            long = data['long']
        except:
            long = "This package doesn't provide a long description."

        try:
            creator = data['creator']
        except:
            creator = "Unknown!"

        try:
            name = data['name']
        except:
            name = game
        print(f"""
Name: {name}
Short: {short}
Creator: {creator}

Description:
{long}
        """)

        while True:
            prompt = input("(Want to execute?) >>> ")
            if prompt.startswith('y'):
                break
            else:
                print("cancelled.")
                exit()

        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        os.chdir(f'{temp_dir.name}/{game}')
        os.system(data['exec'])

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(60)
        with alive_bar(3) as bar:
            command = bytes("1".encode('UTF-8') + game.encode('UTF-8'))
            s.sendto(command, SERVER)

            l = s.recvfrom(1024)
            size = l[0]
            size = len(size) * 2
            bar()
            print(size)
            f = open(f'{temp_dir.name}/{game}.zip', 'wb')

            l = s.recvfrom(size)
            f.write(l[0])
            f.close()
            bar()
            # https://stackoverflow.com/questions/3083235/unzipping-file-results-in-badzipfile-file-is-not-a-zip-file
            # God bless their souls.
            f = open(f'{temp_dir.name}/{game}.zip', 'r+b')
            data = f.read()
            pos = data.find(b'\x50\x4b\x05\x06')  # End of central directory signature
            if (pos > 0):
                f.seek(pos + 22)  # size of 'ZIP end of central directory record'
                f.truncate()
                f.close()
            else:
                return

            bar()

        try:
            os.mkdir(f'{temp_dir.name}/{game}')
        except FileExistsError:
            s.close()
            execute(game)

        shutil.unpack_archive(f'{temp_dir.name}/{game}.zip', f'{temp_dir.name}/{game}')
        os.remove(f'{temp_dir.name}/{game}.zip')
        bar()

        s.close()
        execute(game)

@app.command(help="Permanently stores game files.")
def install(game, path : str=f''):
    if path == '':
        path = os.path.expanduser('~') + '/.mait'

    does_exist = os.path.exists(path)
    if does_exist == False:
        os.makedirs(path)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(60)
        with alive_bar(4) as bar:
            command = bytes("1".encode('UTF-8') + game.encode('UTF-8'))
            s.sendto(command, SERVER)

            l = s.recvfrom(1024)
            size = l[0]
            size = len(size) * 2
            bar()
            print(size)
            f = open(f'{path}/{game}.zip', 'wb')
            l = s.recvfrom(size)
            f.write(l[0])
            f.close()
            bar()
            # https://stackoverflow.com/questions/3083235/unzipping-file-results-in-badzipfile-file-is-not-a-zip-file
            # God bless their souls.
            f = open(f'{path}/{game}.zip', 'r+b')
            data = f.read()
            pos = data.find(b'\x50\x4b\x05\x06')  # End of central directory signature
            if (pos > 0):
                f.seek(pos + 22)  # size of 'ZIP end of central directory record'
                f.truncate()
                f.close()
            else:
                return

            bar()

            shutil.unpack_archive(f'{path}/{game}.zip', f'{path}/{game}')
            os.remove(f'{path}/{game}.zip')
            bar()

        print(f"Game is stored at: {path}/{game}")

        try:
            os.mkdir(f'{path}/{game}')
        except FileExistsError:
            s.close()

@app.command(help="Uploads folder to mait's registry.")
def upload(path: str):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # TODO: Create way to transport folders. (Success!)
        with alive_bar(5) as bar:

            does_exist = os.path.exists(path)
            if does_exist is False:
                print("Path doesn't exist!")
                exit()
            shutil.make_archive('./output', 'zip', path)
            size = os.path.getsize('./output.zip')
            name = path.rfind("/")
            name = path[name:]
            name = name[1:]
            bar()
            s.sendto(b'2', SERVER)
            s.sendto(bytes(size), SERVER)
            bar()
            s.sendto(bytes(name.encode('UTF-8')), SERVER)
            response = s.recvfrom(1024)
            if response[0] == b'100':
                pass
            elif response[0] == b'400':
                print("Package already exists!")
                exit()

            bar()
            shutil.make_archive('./output', 'zip', path)
            f = open('./output.zip', 'rb')
            s.sendto(f.read(), SERVER)
            f.close()
            bar()
            os.remove('./output.zip')
            bar()
        
        print("Congrats! Successful upload!\nYou should see your package in `mait list`.\n\nOpen an issue on the repository if problems arise.")


if __name__ == "__main__":
    app()