distancia_1 = float(input('Distancia que o primeio dragão vermelho pecorreu:'))
tempo_1 = float(input('tempo que o dragão vermelho pecorreu:'))
distancia_2 = float(input('Distancia que o primeio dragão azul pecorreu:'))
tempo_2 = float(input('tempo que  o primeio dragão azul pecorreu:'))

if tempo_1 > tempo_2:
    print('O dragão vermelho é mais rápido')
elif tempo_1 == tempo_2:
    print('Ambos tem a mesma Velocidade')
else:
    print('o dragão azul é mais rápido')