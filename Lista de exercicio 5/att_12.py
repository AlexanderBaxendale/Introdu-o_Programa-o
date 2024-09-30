atk_espada = int(input('poder de ataque da espada:'))
dura_espada = int(input('Durabilidade da espada:'))

atk_arco = int(input('poder de ataque da arco:'))
dura_arco = int(input('Durabilidade da arco:'))

atk_lanca = int(input('poder de ataque da lança:'))
dura_lanca = int(input('Durabilidade da lança:'))

if ((atk_espada > 50) and (dura_espada > 70)):
    print('A arma escolhida foi a espada')
elif ((atk_arco > 50) and (dura_arco > 70)):
    print('A arma escolhida foi a arco')
elif ((atk_lanca > 50) and (dura_lanca > 70)):
    print('A arma escolhida foi a lança')
else:
    print('é melhor escolher outra arma')

