# Cmd-em-html-e-python-so-para-se-divestir
somente dirveção

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Imagem de Fundo</title>

    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            width: 100vw;
            height: 100vh;
            background-image: url("carro.jpeg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;

            display: flex;
            justify-content: center;
            align-items: center;
        }

        .texto {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 100px;
            letter-spacing: 8px;
            font-weight: bold;
            color: #fff;

            text-transform: uppercase;
            text-align: center;

            background: rgba(0, 0, 0, 0.7);
            padding: 25px 50px;
            border-radius: 25px;

            border: 4px solid white;

            text-shadow:
                0 0 10px #fff,
                0 0 20px #ff0000,
                0 0 40px #ff0000;

            box-shadow:
                0 0 20px red,
                inset 0 0 20px black;

            animation: brilho 1.5s infinite alternate;
        }

        @keyframes brilho {
            from {
                transform: scale(1);
                filter: brightness(1);
            }

            to {
                transform: scale(1.08);
                filter: brightness(1.4);
            }
        }
    </style>
</head>

<body>
    <div class="texto">
        SINTA O SOM DESCRAAAAAAAAAAAAÇA
        
        CINTURA DE MOLA 
    </div>
</body>
</html>


em python:

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
