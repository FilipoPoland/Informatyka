# napisz program symulujacy dzialanie

def chec():
    c = input('Czy chcesz sie zalogowac?(t/n): ')
    if c == 't':
        return True
    else:
        return False


def pomoc():
    print('Aby wyświetlić uśmiechniętą minkę wpisz: uśmiech.\n'
          'Aby wyświetlić smutną minkę wpisz: smutek.\n'
          'Aby wyświetlić prostokąt wpisz: prostokat.\n'
          # 'Aby wyświetlić trapez prostokątny wpisz: trapez.\n'
          'Aby obliczyć pole trapezu wpisz: trapez pole.\n'
          'Aby wyświetlić komendy wpisz: pomoc.\n'
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


# zdefiniowanie wstepnych zmiennych
ticker = 0
import

end = True
while end:
    end = chec()
    # zapyttanie uzytkownika czy ma juz konto
    nu = input('Czy jesteś istniejącym użytkownikiem? (t/n)')
    # zdefiniowanie nowego konta
    if nu == 'n':
        # zdefiniowanie nowego loginu
        l_user.append(input('Podaj nazwę użytkownika: '))
        # zdefiniowanie hasla do nowego konta
        l_pass.append(input('Podaj hasło do konta: '))

    # wyswietlenie ilosci poprzednich podejsc
    print(f'Podejście {ticker}.')
    # zapytanie uzytkownika o login
    login = input('Podaj login: ')

    # sprawdzenie loginu
    if login in l_user:
        index = l_user.index(login)
        haslo = input('Podaj hasło: ')
        # sprawdzenie prawdziwosci hasla
        if haslo in l_pass[index]:
            logged = True
            print('Poprawne logowanie')
            pomoc()
            # podczas bycia zalogowanym beda dostepne komendy opisane wewnatrz funkcji while
            while logged:
                komenda = input('Komenda: ')
                if komenda == 'uśmiech':
                    print(':)')
                if komenda == 'smutek':
                    print(':(')
                if komenda == 'prostokat':
                    prostokat()
                if komenda == 'trapez pole':
                    trapezpole()
                if komenda == 'pomoc':
                    pomoc()
                if komenda == 'logout':
                    logged = False
                    print('Zostałeś wylogowany.')
                if komenda == 'wyjdz':
                    end = False
        else:
            print('Błędne hasło.')
            ticker += 1
    elif ticker > 4:
        end = False
    else:
        print('Błędny login.')
        ticker += 1
