import random
# i = 1
# while True:
#   print(i)
#    i += 1

# i = 1
# while i < 10:
#    print(i)
#    i += 1

# suma = 0
# y = int(input('Do jakiej liczby chciałbyś policzyć sumę'))
# z = int(input('Od jakiej liczby chciałbyś policzyć sumę'))
# y += 1
#
# for x in range(z, y):
#     suma += x
# print(suma)

listz = []
suma = 0
for x in range(8):
    listz.append(random.randint(-100, 100))
print(listz)

maks = -100
for x in listz:
    if 0 > x > maks:
        maks = x
print('Max:', maks)
#komentarz
