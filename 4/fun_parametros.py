def soma(*parcelas):
    aux = 0 
    for valor in parcelas:
        aux += valor
    return aux

print(soma(10,20))


def f(**kwargs):
    print(kwargs)
    print(type(kwargs))

f(nome = 'Renzo')