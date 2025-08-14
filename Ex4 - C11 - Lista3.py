pessoas = []
for i in range(3):
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    pessoas.append((nome, peso))

mais_pesada = max(pessoas, key=lambda x: x[1])
mais_leve = min(pessoas, key=lambda x: x[1])

print("Mais pesada:", mais_pesada[0])
print("Mais leve:", mais_leve[0])
