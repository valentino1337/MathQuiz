import random
from operator import add, sub, mul
howlong = int(input('Koľko otázkov má mať kvíz?: '))

nespravneodpovede = 0
spravneodpovede = 0
while spravneodpovede < howlong:
    operacia = random.choice([add, sub, mul])
    num1 = int(random.uniform(-100, 100))
    num2 = int(random.uniform(-100, 100))
    vysledok = operacia(num1, num2)
    operacia = str(operacia)
    operacia = operacia.replace('<built-in function sub>', ' - ')
    operacia = operacia.replace('<built-in function add>', ' + ')
    operacia = operacia.replace('<built-in function mul>', ' * ')
    vypocitany = int(input(str(num1) + operacia + str(num2) + ' = '))
    if vypocitany == vysledok:
        spravneodpovede = spravneodpovede + 1
        print('Správna odpoveď. Už len ' + str(10 - spravneodpovede) + ' do konca!')
    else:
        nespravneodpovede = nespravneodpovede + 1
        print('Nesprávna odpoveď')
        pass

while spravneodpovede >= howlong:
    print('Vyhral si a mal si ' + str(nespravneodpovede) + ' nesprávnych odpovedí')