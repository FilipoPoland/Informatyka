from random import shuffle


def plansza(stan):
    a = 0
    for j in range(3):
        for i1 in range(3):
            print('+', 3 * '-', sep='', end='')
        print('+')
        for i1 in range(3):
            print('|', ' ', stan[a], ' ', sep='', end='')
            a += 1
        print('|')
    for i1 in range(3):
        print('+', 3 * '-', sep='', end='')
    print('+')


def sprawdz(getiteam, getiteam2, getiteam3):
    # for 0
    if getiteam[0] == getiteam[1] == getiteam[2] == 0:
        getiteam2.append('The computer won.')
        return False
    elif getiteam[3] == getiteam[4] == getiteam[5] == 0:
        getiteam2.append('The computer won.')
        return False
    elif getiteam[6] == getiteam[7] == getiteam[8] == 0:
        getiteam2.append('The computer won.')
        return False
    elif getiteam[0] == getiteam[4] == getiteam[8] == 0:
        getiteam2.append('The computer won.')
        return False
    elif getiteam[2] == getiteam[4] == getiteam[6] == 0:
        getiteam2.append('The computer won.')
        return False
    elif getiteam[0] == getiteam[3] == getiteam[6] == 0:
        getiteam2.append('The computer won.')
        return False
    elif getiteam[1] == getiteam[4] == getiteam[7] == 0:
        getiteam2.append('The computer won.')
        return False
    elif getiteam[2] == getiteam[5] == getiteam[8] == 0:
        getiteam2.append('The computer won.')
        return False
    # for X
    if getiteam[0] == getiteam[1] == getiteam[2] == 'X':
        getiteam2.append('You won.')
        return False
    elif getiteam[3] == getiteam[4] == getiteam[5] == 'X':
        getiteam2.append('You won.')
        return False
    elif getiteam[6] == getiteam[7] == getiteam[8] == 'X':
        getiteam2.append('You won.')
        return False
    elif getiteam[0] == getiteam[4] == getiteam[8] == 'X':
        getiteam2.append('You won.')
        return False
    elif getiteam[2] == getiteam[4] == getiteam[6] == 'X':
        getiteam2.append('You won.')
        return False
    elif getiteam[0] == getiteam[3] == getiteam[6] == 0:
        getiteam2.append('You won.')
        return False
    elif getiteam[1] == getiteam[4] == getiteam[7] == 0:
        getiteam2.append('You won.')
        return False
    elif getiteam[2] == getiteam[5] == getiteam[8] == 0:
        getiteam2.append('You won.')
        return False
    elif not getiteam3:
        getiteam2.append('It is a tie')
        return False
    else:
        return True


list1 = [' '] * 9

list2 = []
for i in range(9):
    list2.append(i)

zwyciestwo = []

x = sprawdz(list1, zwyciestwo, list2)

while x:
    shuffle(list2)
    los = list2[0]
    del(list2[0])
    list1[los] = 0
    y = 1
    plansza(list1)
    x = sprawdz(list1, zwyciestwo, list2)
    if x:
        user = int(input('Podaj pole(zakres 1-9): '))
        user -= 1
        list1[user] = 'X'
        list2.remove(user)
        x = sprawdz(list1, zwyciestwo, list2)


print(zwyciestwo[0])
