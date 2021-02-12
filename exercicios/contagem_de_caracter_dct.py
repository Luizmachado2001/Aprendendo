

def contar_caracteres(s):
    """Função que conta os caracteres de uma string
    :param s: string a ser contada
    :return:
    """
    caracteres_cordenados = sorted(s)
    cararter_anterior = caracteres_cordenados[0]
    contagem = 1

    for caracter in caracteres_cordenados[1:]:
        if caracter == cararter_anterior:
            contagem+=1
        else:
            print(f'{cararter_anterior} : {contagem}')
            cararter_anterior = caracter
            contagem = 1

    print(f'{cararter_anterior} : {contagem}')


if __name__ == '__main__':
    contar_caracteres('Banana')