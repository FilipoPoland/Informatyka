# with open('Data.txt', 'a') as file:
#     file.write('Ejo\n')

# napisz dwa programy
# pierwszy generuje plik tekstowy zawierający 100 000 liczb los z zakresu -100 000 do 100 000
# drugi sprawdza czy w utworzonym pliku znajduje się podana liczba

def los(getiteam1, getiteam2, getiteam3):
    from random import randint
    list_los = []
    for i in range(getiteam1):
        list_los.append(randint(getiteam2, getiteam3))
    return list_los


# list_los = los(100000, -100000, 100000)
# list_los = str(list_los)
#
# list_los = list_los.replace('[', '')
# list_los = list_los.replace(']', '')
# list_los = list_los.replace(',', '\n')
# list_los = list_los.replace(' ', '')
#
# with open('Data.txt', 'w') as file:
#     file.write(list_los)

u_input = input('Podaj szukaną liczbę: ')

with open('Data.txt', 'r') as file:
    for line in range(100000):
        linijka = str(file.readline())
        linijka = linijka.replace('\n', '')
        if u_input == linijka:
            print(f'Podana wartość znajduje się w lini: {line + 1}')
