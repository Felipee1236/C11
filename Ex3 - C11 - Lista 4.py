import numpy as np

campo = np.zeros((2,2), dtype=int)

linha = np.random.randint(0, 2)
coluna = np.random.randint(0, 2)
campo[linha, coluna] = 1

print("Campo gerado (escondido do jogador)")
print(campo)

tentativas = 3
encontrou = False

for i in range(tentativas):
    print(f"Tentativa {i+1} de {tentativas}")
    l = int(input("Digite a linha (0 ou 1): "))
    c = int(input("Digite a coluna (0 ou 1): "))

    if campo[l, c] == 1:
        print("💥 Game Over! :( Try Again!")
        encontrou = True
        break
    else:
        print("Posição segura! ✅")

if not encontrou:
    print("🎉 Congratulations! You beat the game! :)")
