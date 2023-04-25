from tkinter import *
from math import sin, pi

okno = Tk()
okno.title('Program')
okno.geometry('800x600')


def mfunkcja():
    print(1)
    if przycisk['text'] == ' S T A R T ':
        przycisk['text'] = 'S T O P'
    else:
        przycisk['text'] = ' S T A R T '


from random import randint


def oblicz():
    licznik = 0
    for i in range(10000):
        x = randint(0, 179)
        y = randint(0, 99)
        yo = 100 -int(sin(x * pi / 180) * 100)
        if y >= yo:
            img.put("green", (x, y))
            licznik += 1
        else:
            img.put("red", (x, y))

    print(licznik / 10000 * pi)


c = Canvas(okno, width=360, height=200, bg='#ffffff')
c.pack()
img = PhotoImage(width=360, height=200)
c.create_image((180, 100), image=img)

for x in range(360):
    y = 100 - int(sin(x*pi/180)*100)
    img.put('blue', (x, y))

przycisk = Button(okno, text=' S T O P ', command=mfunkcja)
przycisk.pack()
przycisk2 = Button(okno, text=' O B L I C Z ', command=oblicz())
przycisk2.pack()
okno.mainloop()
