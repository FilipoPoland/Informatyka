from random import shuffle


def plansza(stan):
    a = 0
    for i1 in range(3):
        for i2 in range(3):
            print('+', 3*'-', sep='', end='')
        print('+')
        for i2 in range(3):
            print('|', ' ', stan[a], ' ', sep='', end='')
            a += 1
        print('|')

    for i3 in range(3):
        print('+', 3*'-', sep='', end='')
    print('+')


def sprawdz(getiteam, getiteam2):
    if getiteam[0] == getiteam[1] == getiteam[2]:
        return False
    elif getiteam[3] == getiteam[4] == getiteam[5]:
        return False
    elif getiteam[6] == getiteam[7] == getiteam[8]:
        return False
    elif getiteam[0] == getiteam[4] == getiteam[8]:
        return False
    elif getiteam[2] == getiteam[4] == getiteam[6]:
        return False
    elif not getiteam2:
        return False
    else:
        return True


lista = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print(lista)

lista2 = []
for i in range(9):
    lista2.append(i)
print(lista2)

x = True

while x:
    shuffle(lista2)
    los = lista2[0]
    del(lista2[0])
    print(los)
    lista[los] = 'O'
    plansza(lista)
    x = sprawdz(lista, lista2)

    user = int(input('Podaj pole: '))
    lista[user] = 'X'
    lista2.remove(user)
    plansza(lista)

    x = sprawdz(lista, lista2)
