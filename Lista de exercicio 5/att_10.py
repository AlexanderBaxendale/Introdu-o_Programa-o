porta = int(input('Número da porta escolhida: '))

match porta:
    case 1:
        print('Para aqueles que entrarem pela porta 1, você lutara contra um ogro')
    case 2:
        print('Para aqueles que entrarem pela porta 2, você lutara contra um enxame de goblins')
    case 3:
        print('Para aqueles que entrarem pela porta 3, você lutara contra um dragão')
    case 4:
        print('Para aqueles que entrarem pela porta 4, você resolverá um quebra-cabeças')
    case 5:
        print('Para aqueles que entrarem pela porta 5, você lutara contra o Hulk1')
    case _:
        print('porta invalida')