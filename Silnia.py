silnia = int(input('Podaj z jakiej liczby obliczyc silnie: '))
tmp = 1

for i in range(2, silnia + 1):
    tmp = tmp * i

print(f'Silnia wynosi {tmp}')
