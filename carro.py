import os
import subprocess
import platform
import webbrowser

print ("SINTA O SOM PORRA")

arquivo = "ASAS LIVRES - RELÍQUIA PRA PAREDÃO (COM GRAVE).mp3"

sistema = platform.system()

if sistema == "Windows":
    os.startfile(arquivo)
elif sistema == "Linux":
    subprocess.run(["xdg-open", arquivo])
else:
    print("No Android ou outro sistema, use uma biblioteca específica do ambiente.")

webbrowser.open("carro.html")
