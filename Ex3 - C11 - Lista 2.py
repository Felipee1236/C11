sexo = input("Digite seu sexo (M/F): ").strip().upper()
while sexo not in ("M", "F"):
    sexo = input("Entrada inválida. Digite seu sexo (M/F): ").strip().upper()

if sexo == "M":
    print("Sexo Masculino")
elif sexo == "F":
    print("Sexo Feminino")
