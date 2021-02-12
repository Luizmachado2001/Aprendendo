linguas = {
    'br':'portugues',
    'eua':'ingles'
}

for chave in linguas:
    print(chave)

# retorna interar
for chave in linguas.keys():
    print(chave)


#retorna o valor
for valor in linguas.values():
    print(valor)


for chave, valor in linguas.items():
    print(chave, valor)