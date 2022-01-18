lista_avatares = []
_ = {}
cont = 1
with open('avatares.txt', 'r') as files:
    linhas = files.readline()
    frase = ''
    for v in linhas:
        frase += v
        if v == ';':
            _['conta'] = cont
            _['img'] = frase.replace(';', '')
            lista_avatares.append(_.copy())
            _.clear()

print(lista_avatares)
