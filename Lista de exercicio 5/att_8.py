missoes = int(input('Número de missões realizadas pelo cavaleiro: '))

if missoes > 10:
    print('Parabéns pelas suas conquistas, receba um bônus de 100 moedas de ouro')
elif missoes >= 5 and missoes < 11:
    print('Parabéns pelas suas conquistas, receba um bônus de 50 moedas de ouro')
else:
    print('Parabéns pelas suas conquistas, receba um bônus de 10 moedas de ouro')