planta = float(input('altura da planta(metros): '))

if planta < 1:
    print('essa planta mágica é classificada como pequena')
elif  planta >= 1 and planta < 4:
    print('essa planta mágica é classificada como Média')
else:
    print('essa planta mágica é classificada como Grande') 