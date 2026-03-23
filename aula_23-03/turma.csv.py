import csv


dados = [
    ['nome', 'nota1', 'nota2']
]


dadosAluno = []


for i in dados(3):
    nome = input("Qual o nome do aluno? ")
    nota1 = input("Qual a nota1 do aluno? ")
    nota2 = input("Qual a nota2 do aluno? ")


    dadosAluno.append(nome)
    dadosAluno.append(nota1)
    dadosAluno.append(nota2)


    dados.append(dadosAluno)


print(dados)

with open('turma.csv', 'r',
          encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
        