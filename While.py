# napisz program symulujacy dzialanie

def chec():
    c = input('Czy chcesz sie zalogowac?(t/n): ')
    if c == 't':
        return True
    else:
        return False


def help():
    print('Aby wyświetlić uśmiechniętą minkę wpisz: uśmiech.\n'
          'Aby wyświetlić smutną minkę wpisz: smutek.\n'
          'Aby wyświetlić prostokąt wpisz: prostokat.\n'
          # 'Aby wyświetlić trapez prostokątny wpisz: trapez.\n'
          'Aby obliczyć pole trapezu wpisz: trapez pole.\n'
          'Aby wyświetlić komendy wpisz: help.\n'
          'Aby się wylogować wpisz: logout.')


def prostokat():
    a = '#'
    b = ' '
    bok_a = int(input('Jak duży ma być bok a?'))
    bok_b = int(input('Jak duży ma być bok b?'))

    print(a * bok_a + ('\n' + a + b * (bok_a - 2) + a) * bok_b + '\n' + a * bok_a)


def trapezpole():
    print('W celu obliczenia pola trapezu: ')
    a = float(input('Podaj podstawę 1 trapezu: '))
    b = float(input('Podaj podstawę 2 trapezu: '))
    h = float(input('Podaj wysokość trapezu: '))

    # obliczenie pola trapezu
    print((a + b) / 2 * h)


l_user = ['admin']
l_pass = ['admin']

while chec():
    nu = input('Czy jesteś istniejącym użtkownikiem? (t/n)')
    if nu == 'n':
        l_user.append(input('Podaj nazwę użytkownika: '))
        l_pass.append(input('Podaj hasło do konta: '))

    login = input('Podaj login: ')
    haslo = input('Podaj hasło: ')

    if login in l_user:
        index = l_user.index(login)
        if haslo in l_pass[index]:
            logged = True
            print('Poprawne logowanie')
            help()
            while logged:
                komenda = input('Komenda: ')
                if komenda == 'uśmiech':
                    print(':)')
                if komenda == 'smutek':
                    print(':(')
                if komenda == 'prostokat':
                    prostokat()
                # if komenda == 'trapez':
                #     trapez()
                if komenda == 'trapez pole':
                    trapezpole()
                if komenda == 'logout':
                    logged = False
                    print('Zostałeś wylogowany.')
    elif login in l_user:
        print('Błedne hasło.')
    else:
        print('Błędny login.')
