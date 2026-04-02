def simularCrescimento(pop, taxa, limite):
    anos = 0
    while pop <= limite: 
        pop = pop * (1+taxa/100)
        anos +=1
    return anos 

#main
p = float(input('população: '))
t = float(input('taxa (%):  '))
1 = float(input('limite: '))
print (f'anos = {simularCrescimento(p,t,1)}')
