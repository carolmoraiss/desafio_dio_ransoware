import os
from cryptography.fernet import Fernet

CAMINHO_PASTA = "../arquivos_alvo"

def carregar_chave():
    with open("chave.key", "rb") as arquivo:
        return Fernet(arquivo.read())

def descriptografar():
    fernet = carregar_chave()

    for nome_arquivo in os.listdir(CAMINHO_PASTA):
        caminho_completo = os.path.join(CAMINHO_PASTA, nome_arquivo)

        if os.path.isfile(caminho_completo):
            with open(caminho_completo, "rb") as arquivo:
                dados_criptografados = arquivo.read()

            try:
                dados = fernet.decrypt(dados_criptografados)
            except:
                print(f"ERRO Não foi possível descriptografar {nome_arquivo}")
                continue

            with open(caminho_completo, "wb") as arquivo:
                arquivo.write(dados)

            print(f"RESTAURADO {nome_arquivo}")

if __name__ == "__main__":
    descriptografar()
    print("\nArquivos restaurados com sucesso.")
