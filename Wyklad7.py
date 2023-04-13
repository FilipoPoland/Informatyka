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


c = Canvas(okno, width=360, height=200, bg='#ffffff')
c.pack()
img = PhotoImage(width=360, height=200)
c.create_image((180, 100), image=img)

for x in range(20, 100):
    img.put('yellow', (x, 40))

for x in range(360):
    y = 100 - int(sin(x*pi/180)*100)
    img.put('blue', (x , y))

przycisk = Button(okno, text=' S T O P ', command=mfunkcja)
przycisk.pack()

okno.mainloop()
