def los(getiteam1, getiteam2, getiteam3):
    from random import randint
    list_los = []
    for i in range(getiteam1):
        list_los.append(randint(getiteam2, getiteam3))
    return list_los


l_los = los(1000, -100, 100)

# swap = True
#
# while swap:
#     swap = False
#     for i in range(len(l_los)-1):
#         if l_los[i] > l_los[i+1]:
#             l_los[i], l_los[i+1] = l_los[i+1], l_los[i]
#             swap = True
#
# print(l_los)


def sortBuble(getlist):
    swap = False
    for i in range(len(getlist)-1):
        for j in range(len(getlist)-i-1):
            if getlist[j] > getlist[j+1]:
                getlist[j], getlist[j+1] = getlist[j+1], getlist[j]
                swap = True
        if not swap:
            return


sortBuble(l_los)
print(l_los)

def binary_search(u_in, getlist):
    left = 0
    right = len(getlist)
    idx = None
    while left < right:
        idx = (left + right) // 2
        if getlist[idx] == u_in:
            print(f'Szukana liczba jest na indeksie {idx}')
            return True
        else:
            if getlist[idx] < u_in:
                left = idx + 1
            elif getlist[idx] > u_in:
                right = idx - 1
    return False


u_input = int(input('Podaj liczbę.'))
binary_search(u_input, l_los)
