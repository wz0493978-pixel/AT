import os
import shutil

movidos = 0
pasta = r"C:\P_Frell\arquivos"

pastas = ["documentos", "pdfs", "imagens", "videos", "textos"]

tipos = { 
    ".docx": "documentos",
     ".pdf": "pdfs",
     ".jpg": "imagens",
     ".mp4": "videos",
     ".txt": "textos"
      }

print("  ")




confirmacao = input(
    "Deseja organizar todos os arquivos ?(s/n)\n"
    )

print(" ")

if confirmacao.lower() != "s":
    print("Operação cancelada")
    exit()

arquivos = os.listdir(pasta)


for nome_pasta in pastas:
    caminho_pasta = os.path.join(pasta, nome_pasta)

    if not os.path.exists(caminho_pasta):
        os.mkdir(caminho_pasta)
        print(nome_pasta, "criada")


    


for arquivo in arquivos:

    nome, extensao = os.path.splitext(arquivo)
    print()

    if extensao in tipos:
        nome_da_pasta = tipos[extensao]

        pasta_destino = os.path.join(pasta, nome_da_pasta)

        origem = os.path.join(pasta, arquivo)

        destino = os.path.join(
        pasta_destino, arquivo
        )

        shutil.move(origem, destino)
        movidos += 1


print(" ")
print(f"Foram movidos {movidos} arquivos")
