# pobieranie danych od uzytkownika

# x = input('Jak Ci na imię?')
# print('Witaj', x + '. Miło Cię poznać.')

# indeksowanie wewnatrz str
x = 'Hello World'
print(x[4])
# dlugosc str
print(len(x))

# wyswietljacy tylko l ze zmiennej hello world
print(x[2], x[3], x[9])

# wyswietl pierwszy i ostatni znak z podanego tekstu
y = 'Życie nie ma sensu i wszyscy umrzemy'
x = int(len(y)) - 1

print(y[0] + y[x])

# tekst uytkownika
y = input('Podaj tekst')
x = int(len(y)) - 1
print(y[0], y[x])

# tekst uzytkownika
c = input('Podaj tekst')
print(c[0], c[-1])

# input nastepnie wyswietl pierwszy i osattnie 2 znaki
d = input('Podaj tekst:')
print(d[:2]+d[-2:])

# zadanie domowe
# 1. zmienna z input, zwrocic co drugi znak do 6 wlacznie nastepnie wszystko

x = input('Proszę podać frazę składającą się z co najmniej 8 znaków:')
print(x[0:7:2, 7::])

# 2. zmienna z input, wyswietl od tylu


