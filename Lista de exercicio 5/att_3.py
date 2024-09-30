animal = int(input('Seu animal favorito é um 1(mamífero) ou 2(réptil)?: '))

match animal:
    case 1:
        print('Seu annimal favorito é um cachorro')
    case 2:
        print('Seu animal favorito é uma tartaruga')
    case _:
        print('Resposta inválida')