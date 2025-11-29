from cryptography.fernet import Fernet

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as arquivo:
        arquivo.write(chave)
        
if __name__ == "__main__":
    gerar_chave()
