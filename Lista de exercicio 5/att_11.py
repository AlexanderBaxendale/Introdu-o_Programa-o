can_a = float(input('A Média do candidato A foi:')) 
can_b = float(input('A Média do candidato B foi:')) 
can_c = float(input('A Média do candidato C foi:')) 


if can_a > can_b > can_c:
    print('O vencedor é o candidato A')
elif can_b > can_a and can_c:
    print('O vencedor é o candidato B')
elif can_c > can_b and can_a:
    print('O vencedor é o candidato C')
elif can_a == can_b and can_c:
    print('Empate entre os cadidatos')
else:
    print('empate')