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


def sprawdz(getiteam, getiteam2):
    # for 0
    if getiteam[0] == getiteam[1] == getiteam[2] == '0':
        getiteam2.append('The computer won.')
        return False
    elif getiteam[3] == getiteam[4] == getiteam[5] == '0':
        getiteam2.append('The computer won.')
        return False
    elif getiteam[6] == getiteam[7] == getiteam[8] == '0':
        getiteam2.append('The computer won.')
        return False
    elif getiteam[0] == getiteam[4] == getiteam[8] == '0':
        getiteam2.append('The computer won.')
        return False
    elif getiteam[2] == getiteam[4] == getiteam[6] == '0':
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
    elif not getiteam:
        getiteam2.append('It is a tie')
        return False
    else:
        return True


list1 = [' '] * 9

list2 = []
for i in range(9):
    list2.append(i)
print(list2)
zwyciestwo = []

while sprawdz(list1, zwyciestwo):
    shuffle(list2)
    los = list2[0]
    del(list2[0])
    list1[los] = 0
    plansza(list1)

    user = int(input('Podaj pole(zakres 0 - 8): '))
    list1[user] = 'X'
    list2.remove(user)
    plansza(list1)

print(zwyciestwo[0])
