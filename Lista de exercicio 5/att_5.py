agua = float(input('Quantidade de águal atual em (l):'))
dist = float(input('Distância até o oásis em (km):'))

quantidade = 2 * dist

if agua >= quantidade:
    print('Água suficiente para chegar ao óasis')
else:
    print('Água insuficiente')