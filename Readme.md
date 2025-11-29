#  Ransomware Simulado – Projeto Educacional em Python

Este projeto representa um **ransomware simulado**, criado para fins de estudo e demonstração prática de como malwares desse tipo operam.  
O script **criptografa e descriptografa arquivos reais**, permitindo visualizar o impacto de um ataque e como a recuperação depende da chave de criptografia.

> Uso EXCLUSIVAMENTE EDUCACIONAL  
---

## Estrutura do Projeto

desafio/
│
├── arquivos_alvo/ # Documentos-alvo da simulação
│ └── senhas.txt # Exemplo de arquivo sensível (antes e depois criptografado)
│
└── ransomware/
├── criar_chave.py # Gera a chave de criptografia
├── criptografar.py # Realiza o ataque (criptografa os arquivos)
├── descriptografar.py # Restaura os arquivos encriptados
├── chave.key # (gerado após criar_chave.py)
└── mensagem_resgate.txt # (gerado após criptografia)

##  Requisitos

Ter Python 3 instalado.  
Instalar a biblioteca necessária:

```bash
pip install cryptography
 ```

## Como rodar o projeto

#### 1 - Dentro da pasta desafio/ransomware, execute:

```bash
 python criar_chave.py
 ```

Gera um arquivo chamado chave.key.
Sem essa chave, os arquivos não podem ser recuperados.

#### 2 - Criptografar os arquivos da vítima (ataque simulado)

```bash
python criptografar.py
 ```

Após executar:
senhas.txt será criptografado
será criado mensagem_resgate.txt simulando o pedido de resgate


#### 3 - Descriptografar e restaurar tudo

```bash
python descriptografar.py
 ```

Usa chave.key para recuperar os dados:
os arquivos retornam ao estado original.