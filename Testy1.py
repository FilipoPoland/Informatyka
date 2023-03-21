2 + 2
'Hello world'
print(2 + 2)
print('2+2')

# komentarz

'''komentarz'''

""""komentarz"""

print('Hello world')

a = 'Hello'
b = 'world'

print('a')
print('b')

print(a, b)

print(type(a))
print(type(b))

print('Masowiec')
print('Drobnicowiec')
print('Kontenerowiec')

t = 'Tankowiec'
g = 'Gazowiec'
r = 'RoRo'

print(t)
print(g)
print(r)

print(t, g, r)

# kontkatancja danych
print(t + g + r)

c = a + ' ' + b

print(a + ' ' + b)
print(c)

# potrojne cudzyslowy interpretuja nowe wiersze jako entery do wyswietlenia

print('Gdynia', 'Szczecin' + '\n' + 'Świnoujście')

x = 'Gdynia'
y = 'Szczecin'
z = 'Świnoujście'

print(x, y + '\n' + z)

# definiowanie wielu zmiennych

he, te, pe = 'Kołobrzeg', 'Szczecin', 'Sopot'

print(he, te, pe)

# dla tych samych wartosci
a = b = c = zmienna = 'UMG'
print(a, b, c, zmienna, 'UMG')

# powielanie tekstu
print('Hello world' * 5)

print(('BCT' + '\n' + 'GCT' + '\n' + 'DCT')*4)
print('BCT' + '\n' + ('GCT' * 4) + '\n' + 'DCT')

print('''######
#    #
######''')

print('######\n#    #\n######')

# wyswietl analogicz prostokat o wymiarach 9x5 ze zmiennymi i powielonymi str
print('#'*9+'\n'+('#'+' '*7+'#'+'\n')*3+'#'*9)

print('Ala', end=' ')
print('ma kota')
