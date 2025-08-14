aluno = {}
aluno['nome'] = input("Nome do aluno: ")
aluno['media'] = float(input("Média do aluno: "))
aluno['situacao'] = 'AP' if aluno['media'] >= 50 else 'RP'
print("Dados do aluno:", aluno)
