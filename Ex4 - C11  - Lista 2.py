km = float(input("Quantos Km foram percorridos? "))
preco = float(0.0)
if km <= 200:
    preco = km * 0.50
else:
    preco = km*0.45

print(f"Total: R$ {preco:.2f}")