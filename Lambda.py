# kwadrat = lambda x: x*x
#
# print(kwadrat(4))
#
# fnk = lambda x, y: 2*x+y
# print(fnk(22, 55))
#
# print((lambda x: x*x*x)(5))

lista = list(range(10))
print(lista)

lista2 = [i*2 for i in lista]
print(lista2)

lista3 = [i for i in lista if i % 2 == 0]
print(lista3)

lista4 = ['+' if i % 2 == 0 else '-' for i in lista]
print(lista4)

# 10 do 80 podzielne przez 5
lista6 = [i for i in range(10, 81) if i % 5 == 0]
print(lista6)

lista7 = []
for i in range(1, 31):
    if i % 3 == 0 and i % 4 == 0:
        lista7.append('FizzBuzz')
    elif i % 3 == 0:
        lista7.append('Fizz')
    elif i % 4 == 0:
        lista7.append('Buzz')
    else:
        lista7.append(i)