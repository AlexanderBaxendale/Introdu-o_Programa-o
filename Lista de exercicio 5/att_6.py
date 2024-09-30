dist_a = float(input('Distancia do dragão(km) A:'))
temp_a = float(input('Tempo do dragão A(horas):'))
dist_b = float(input('Distancia do dragão b(km):'))
temp_b = float(input('Tempo do dragão b(horas):'))

vel_a = dist_a / temp_a
vel_b = dist_b / temp_b

if vel_a > vel_b:
    print('O dragão A foi mais rápido')
else:
    print('O Dragão B foi mais rápido')