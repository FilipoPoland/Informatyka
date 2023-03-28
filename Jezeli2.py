# instrukcje warunkowe

# # od uzytkownika
# a = float(input('Podaj liczbę: '))

# warunek
# if a > 5:
#     print('Liczba jest większa od 5')
# elif a == 5:
#     print('Podana liczba jest równa 5')
# else:
#     print('Podana liczba jest mniejsza od 5')

# napisz program sprawdzajacy czy podana liczba jest parzysta

# a = float(input('Podaj liczbę: '))
#
# if a % 2 == 0:
#     print('Liczba jest parzysta.')
# else:
#     print('Liczba jest nieparzysta.')

# na podstwie wieku uzytkownika powiedz czy jest gotowy glosowac/byc prezydentem

# a = int(input('Podaj swój wiek: '))
#
# if a >= 35:
#     print('Możesz głosować i zostać prezydentem.')
# elif a >= 18:
#     print('Możesz głosować.')
# else:
#     print('Niestety nie możesz być prezydentem.')

# pobranie tekstu od urzytkownika i podanie roznych wynikow w zaleznosci od dlugosci bez spacji
# przedzialy 1-10 11-20 21-30

a = input('Podaj tekst')
b = len(a.replace(' ', ''))

if b == 0:
    print('Nie podano frazy')
elif b < 11:
    print('Tekst mieści się w przedziale 1-10.')
elif b < 21:
    print('Tekst mieści się w przedziale 11-20.')
elif b < 31:
    print('Tekst mieści się w przedziale 21-30.')
else:
    print('Tekst ma więcej niż 30 znaków.')