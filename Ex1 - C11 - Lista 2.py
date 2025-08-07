
nome_completo = input("Digite seu nome completo: ").strip()
print("Nome em maiúsculas:", nome_completo.upper())
print("Nome em minúsculas:", nome_completo.lower())

quantidade_letras = len(nome_completo.replace(" ", ""))
print("Total de letras no nome:", quantidade_letras)

quantidade_palavras = len(nome_completo.split())
print("Total de palavras no nome:", quantidade_palavras)
nome_dividido = nome_completo.split()
nome_dividido[-1] = "do Inatel"
novo_nome = " ".join(nome_dividido)
print("Nome modificado:", novo_nome)