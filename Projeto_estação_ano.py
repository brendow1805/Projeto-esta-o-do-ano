#Estação do ano
#Entradas

Dia = int(input('Digite o dia: '))
Mes = int(input('Digite o mês: '))
listmes = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]


if Mes in listmes[0]:
    print('Verão')
elif Mes in listmes[1]:
    print('Outono')
elif Mes in listmes[2]:
    print('Inverno')
elif Mes in listmes[3]:
    print('Primavera')
else:
    print('Estação inválida')

