# for i in range(10):
#     print(i)
#
list1 = []

# for j in list1:
#     print(j)

# for element in list1:
#    print(type(element))

# for i in range(10):
#     list1.append(i+1)
#
# print(list1)
#
# for j in list1:
#     if j % 2 == 0:
#         print(j)

# list2 = [[2, 4, 6, 8], [2, 5, 7], [5, 7, 9, 10, 202]]
#
# for i in list2:
#     for j in i:
#         if j % 2 == 0:
#             print(f'{j} jest parzysta.')
#         else:
#             print(f'{j} jest nieparzysta.')


# from random import randint
#
# listRandom = []
# for i in range(10):
#     listRandom.append(randint(0, 100))
#
# maximum = None
# minimum = None
#
# for j in listRandom:
#     if maximum is None and minimum is None:
#         minimum = maximum = j
#     else:
#         if j > maximum:
#             maximum = j
#         elif j < minimum:
#             minimum = j
#
# countmax = 0
# countmin = 0
#
# for k in listRandom:
#     if k == maximum:
#         countmax += 1
#     elif k == minimum:
#         countmin += 1
#
# print(listRandom)
# print(f'{maximum} wystąpiło: {countmax}')
# print(f'{minimum} wystąpiło: {countmin}')


def sumowanie(getiteam1, getiteam2):
    return getiteam1 + getiteam2


# funkcja tworzaca w zaleznosci


def nlist(getiteam1, getiteam2, getiteam3):
    from random import randint
    list_nlist = []
    for i in range(getiteam1):
        list_nlist.append(randint(getiteam2, getiteam3))
    return list_nlist


print(nlist(100, -100, 100))
