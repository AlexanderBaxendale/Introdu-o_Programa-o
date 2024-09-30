real_1 = int(input('Quantidade de moedas de 1 real: '))
cen_50 = int(input('Quantidade de moedas de 50 centavos:'))
cen_25 = int(input('Quantidade de moedads de 25 centavos:'))

total = real_1 *1 + cen_50*0.05 + cen_25*0.025

print(f'O valor total em R$:{total}')