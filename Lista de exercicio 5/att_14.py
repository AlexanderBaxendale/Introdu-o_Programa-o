atk_a = int(input('Poder de ataque do guerreiro A:'))
def_a = int(input('Poder de defesa do guerreiro A:'))
atk_b = int(input('Poder de ataque do guerreiro B:'))
def_b = int(input('Poder de defesa do guerreiro B:'))

soma_a = atk_a + def_a
soma_b = atk_b + def_b

if soma_a > soma_b:
    print('O vencedor do luta foi o guerreiro A')
elif soma_b > soma_a:
    print('O vencedor da luta foi o guerreiro B')
elif soma_a == soma_b > def_a > def_b :
    print('Em casa de empate, aquele que tiver a maior defesa será o vencendor. Portanto o vencedor e o guerreiro A')
else:
    print('Em casa de empate, aquele que tiver a maior defesa será o vencendor. Portanto o vencedor e o guerreiro B')