energia = float(input('Nível de energia em (%):'))
coor = float(input('As coordenadas:'))
tempo = float(input('O tempo:'))

if energia > 80:
    print('Energia suficiente para viajar no tempo!')
elif energia < 80:
    print('Energia insuficiente para viajar no tempo')
elif coor != coor:
    print(' Coordenadas incertas')
else:
    print('o tempo não está ideal')