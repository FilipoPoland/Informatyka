a = float(input('Podaj liczbę przy x^2:'))
b = float(input('Podaj liczbę przy x:'))
c = float(input('Podaj liczbę na końcu równania:'))

delta = (b ** 2) - 4 * (a * c)
print(delta)

if delta > 0:
    x1 = (-b - delta)/2 * a
    x2 = (-b + delta)/2 * a
    print('Miejsca zerowe:', x1, x2)
elif delta == 0:
    x = -b / 2 * a
    print('Miejsce zerowe', x)
else:
    print('Brak miejsc zerowych')

input('Naciśnij enter, aby zakończyć program.')
