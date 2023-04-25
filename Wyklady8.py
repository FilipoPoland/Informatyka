from tkinter import *
import math

kierunekx = 1
kat = 30


def przesun():
    global kat

    x = math.cos(kat * math.pi/180)
    y = math.sin(kat * math.pi / 180)

    c.move(pilka, x, y)

    if c.coords(pilka)[2] >= 600:
        kat = 180 - kat
    elif c.coords(pilka)[0] <= 0:
        kat = 180 - kat
    elif c.coords(pilka)[1] <= 0:
        kat = -kat
    elif c.coords(pilka)[3] >= 600:
        kat = -kat


def clock():
    przesun()
    okno.after(4, clock)


def zmiana(event):
    global kat
    if event.char == 'a':
        kat += 30
    if event.char == 'w':
        kat -= 30


okno = Tk()
okno.title('Program')
okno.geometry('800x800')

c = Canvas(okno, width=600, height=600, bg='#ffffff')
c.pack()

pilka = c.create_oval(30, 30, 60, 60, fill='black')

clock()

okno.mainloop()
