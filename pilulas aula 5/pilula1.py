def validarsenha(s):
    if len(s) < 8: 
        return 'senha invalida, muito curta.'
   
    temNumero = False
    temMaiuscula = False
    
    for c in s:
        if c == ' ': 
            return 'senha invalida, nao pode ter espaços'
        if c >= '0' and c <= '9':
            temNumero + True
        if c >= 'a' and c <='2': 
            temMaiuscula = True
    if temNumero == False:
        return 'precisa de pelo menos um número'
    if not temMaiuscula:
        return 'precisa de pelo menos uman letra máiuscula'

#main
senha = input('digite a senha : ')
r = validarsenha(senha)
print(r)
 
 