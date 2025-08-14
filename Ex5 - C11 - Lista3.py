n = int(input("Quantidade de pessoas: "))
idades = []
mulheres_menos_20 = 0

for i in range(n):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    idades.append(idade)
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idade = sum(idades) / len(idades)
print("Média de idade:", media_idade)
print("Mulheres com menos de 20 anos:", mulheres_menos_20)
