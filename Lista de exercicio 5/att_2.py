ferro = float(input('Quantidade de Ferro(kg): '))
ouro = float(input('Quantidade de Ouro(kg): '))

liga_m = ferro + ouro 

porcentagem = (ferro / liga_m) * 100

print(liga_m)
print(porcentagem)

if liga_m >= porcentagem:
    print('ferro suficiente para fazer a liga metálica')
else:
    print('ferro insuficiente para fazer a liga metálica')
