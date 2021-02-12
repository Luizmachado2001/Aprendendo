linguas = {
    'br':'portugues',
    'eua':'ingles'
}


#Procura dentro de linguas o br
print(linguas.get('br'))

#Procura dentro de linguas o es, se não tiver vai falar lingua não definida
print(linguas.get('es', 'lingua não definida!'))

#se 'br' está em lingua, se estiver é true o contrario é false.
if 'br' in linguas:
    print('Está')
else:
    print('Não está')


linguas['es'] = 'spanhol'

