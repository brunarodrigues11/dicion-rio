
contato = {
    'nome' : 'Bruna',
    'telefone' : '12345678',
    'email' : 'brf@gmail.com',
    'cidade' : 'Rio Pomba'
}


contato['instagram'] = "bruna_rdz_"
del contato['telefone']

for e, v in contato.items():
    print(e, v)

if 'email' in contato:
    print ("email existe!")

'''------------------------------------------'''

frase = 'a rata roeu a roupa do rei de roma'.split()

cont = {}
for e in frase :
    print(e)

    if e in cont:
       cont[e] += 1 
    else:
        cont[e]=1

print(cont)