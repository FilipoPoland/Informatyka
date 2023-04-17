# program tworzenia wpisów do dziennika
import datetime
from Database_logs import list_category, list_date, list_entry
from itertools import islice


def nth_index(iterable, value, n):
    matches = (idx for idx, val in enumerate(iterable) if val == value)
    return next(islice(matches, n-1, n), None)


print('Dziennik: ')
condition = True
condition3 = True
while condition3:
    while condition:
        intent = input('Czy chcesz dokonać wpisu do dziennika?(t/n)')
        if intent == 't':
            category = input('Jaka jest kategoria Twojego wpisu?')
            # adding the category to the list
            list_category.append(category)
            # assign date
            curenttimendate = datetime.datetime.now()
            list_date.append(curenttimendate)
            # asking the user for his/her log entry
            entry = input('Podaj swój wpis: ')
            # appending list entry
            list_entry.append(entry)
            # save all lists

        elif intent == 'n':
            with open('Database_logs.py', 'w') as file:
                file.write('import datetime' + '\n' +
                           'list_date = ' + str(list_date) + '\n' +
                           'list_category = ' + str(list_category) + '\n' +
                           'list_entry = ' + str(list_entry) + '\n')
            condition = False

    q1 = True
    while q1:
        tmp = input('Czy chcesz kontynuować program?(t/n)')
        if tmp == 't':
            condition3 = True
            q1 = False
        elif tmp == 'n':
            condition3 = False
            q1 = False

    condition2 = True
    while condition2:
        display = input('Czy wyświetlić wpisy dziennika?(t/n)')
        if display == 't':
            kategoria = input('Podaj kategorię wpisu lub wpisz: wszystkie')
            if kategoria == 'wszystkie':
                for i in range(len(list_date)):
                    print(list_date[0+i], list_category[0+i], list_entry[0+i], sep='\n')
                    condition2 = False
            elif kategoria not in list_category:
                print('Kategorii nie ma w bazie danych.')
                contition2 = True
            elif kategoria in list_category:
                idx = nth_index(list_category, kategoria, 'n')
                print(list_date[idx], list_category[idx], list_entry[idx], sep='\n')