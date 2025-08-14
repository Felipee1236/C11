tupla = ("Goku", "Vegeta", "Trunks", "Gohan")
print(tupla)
print(tupla[1:3])
print(tupla[2:])
print(len(tupla))
print(max(tupla))
print(min(tupla))
#aaaaaaaaaaaaaaaaaaaaa
print("")
print("")
print("")
print("")
lista = ["Goku", "Vegeta", "Trunks", "Gohan"]
print(lista)
lista.append("Piccolo")
lista.insert(1, "Freeza")
print(lista)
lista[0] = "Goten"
print(lista)
del lista[0]
lista.remove("Trunks")
print("")
print("")
print("")
print("")
print("")
print("")
#conjuentos
conjunto = {"Goku", "Vegeta", "Trunks", "Gohan"}
print(conjunto)
conjunto.add("Piccolo")
print(conjunto)
conjunto.discard("Gohan")
print(conjunto)
conjunto.remove("Trunks")
print(conjunto)
print(type(conjunto))
print("")
print("")
print("")
print("")
# Dicionários
pessoa = {
    "nome": "Goku",
    "idade": 30,
    "sexo": "masculino"
}
print(pessoa)
pessoa ["raca"] = "sayajin"
pessoa ["familia"] = ["Gohan", "Goten", "Chichi", "Pan"]
print(pessoa)
pessoa["idade"] = 31
print(pessoa)
del pessoa["sexo"]
print(pessoa)
print(pessoa.keys())
print(pessoa.values())
print(pessoa["familia"][2])


