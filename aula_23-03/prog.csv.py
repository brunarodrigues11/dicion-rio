import csv


with open('notas.csv.txt', 'r',
          encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha['nota1'], linha['nota2'], linha['nota3'])
        nota1 = float(linha['nota1'])
        nota2 = float(linha['nota2'])
        nota3 = float(linha['nota3'])

        media = (nota1+nota2+nota3) / 3

        print("A média é: ", (media))

    if media >6:
        print(linha['nome'], "- Média: ", (media), "- APROVADA")

    if media <6:
        print(linha['nome'], "- Média: ", (media), "- REPROVADO")