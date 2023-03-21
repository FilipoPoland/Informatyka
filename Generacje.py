h = 0

while h < 1:
    a = int(input('Podaj wiek osoby, dla której chcesz poznać jej generację:'))

    if a < 13:
        print('Witaj generacjo alfa')
    elif a < 28:
        print('Witaj generacjo z')
    elif a < 48:
        print('Witaj milenialsie')
    elif a < 58:
        print('Witaj generacjo x')
    elif a < 77:
        print('Witaj boomerze')
    elif a < 95:
        print('Witaj cicha generacjo')
    elif a < 123:
        print('Witaj wielka generacjo')
    else:
        print('U ded')
    b = int(input('Wprowadź 0, aby kontynuować program, a 1, aby go zatrzymać.'))
    h = h + b
