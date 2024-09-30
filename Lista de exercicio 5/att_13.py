exercito = int(input('O exercito estar fora(1) ou dentro(2) do castelo:'))


match exercito:
    case 1:
        print('Desativar defesas mágicas')
    case 2:
        print('Ativar defesas mágicas')
    case _:
        print('inválido')