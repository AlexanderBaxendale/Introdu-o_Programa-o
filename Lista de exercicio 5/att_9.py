magia = int(input('Escolha um 1(fogo), 2(água) e 3(terra) para solta o feitiço: '))

match magia:
    case 1:
        print('feitiço de Fogo')
    case 2:
        print('feitiço de Água')
    case 3:
        print('feitiço de Terra')
    case _:
        print('feitiço incorreto')