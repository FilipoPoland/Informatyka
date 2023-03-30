from random import randint, shuffle


def plansza(stan):
    a = 0
    for j in range(3):
        for i in range(3):
            print('+', 3*'-', sep='', end='')
        print('+')
        for i in range(3):
            print('|',' ', stan[a], ' ', sep='', end='')
        print('|')
        a += 1
    for i in range(3):
        print('+', 3*'-', sep='', end='')
    print('+')


def sprawdz(lista):
    if list[0] == lista[1] == lista[2]:
        return True
    if list[3] == lista[4] == lista[5]:
        return True
    if list[6] == lista[7] == lista[8]:
        return True
    return False


lista = [' '] * 9
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
    lista[los] = 'o'
    plansza(lista)

    user = int(input('Podaj pole: '))
    lista[user] = 'X'
    lista2.remove(user)
    plansza(lista)
