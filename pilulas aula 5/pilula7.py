def menu():
    while True:
        print('1 - soma')
        print('2 - média')
        print('3 - sair ')
        opc = int(input('opção '))
        if opc == 3:
            break 
        n1 = float(input('n1  '))
        n2 = float(input('n2  '))
        if opc == 1: 
            print(f'soma é {n1+n2}')
        elif opc == 2: 
            print(f'média é {(n1+n2)/2}')
        else: 
            print('opção invalida')