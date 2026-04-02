def verificarValores():
    anterior = float(input('leitura 1: '))
    for i in range(4):
        atual = float(input(f'leitura {i+2}: '))
        if atual <= anterior:
            return  False
        anterior = atual
    return True

#main
if verificarValores():
    print('crescente')
else:
    print('instávels')
    