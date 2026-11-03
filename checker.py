import hashlib

def calcular_hash_arquivo(caminho_arquivo):
    sha256 = hashlib.sha256()

    with open(caminho_arquivo, 'rb') as arquivo:
        while bloco := arquivo.read(4096) :
            sha256.update(bloco)

    return sha256.hexdigest()

# TESTE PRÁTICO
nome_arquivo = 'teste.txt'
hash_resultado = calcular_hash_arquivo(nome_arquivo)
print(f"Hash SHA-256 de '{nome_arquivo}' :\n{hash_resultado}")