def count_De_Letras(palavra=""): #By Luizmachado!
    if palavra == "":
        print('Você não colocou nenhuma palavra! \n')
    else:
        for k,v in enumerate(palavra):
            print(k, ":", v)


count_De_Letras('')
count_De_Letras('Charizard')