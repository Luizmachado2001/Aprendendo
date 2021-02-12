nome = 'Renzo'
#1 modo maior de fazer
for i in range(len(nome)):
    print(i, nome[i])

#2 modo mais limpo
for x,v in enumerate(nome):
    print(x, v)