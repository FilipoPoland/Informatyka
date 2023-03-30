from random import randint

los = randint(0, 100)

zm = True

while zm:
    a = int(input('Podaj liczbę:'))

    if a > los:
        print('Za dużo')
    elif a < los:
        print('Za dużo')
    else:
        print('Bingo')
        zm = False
