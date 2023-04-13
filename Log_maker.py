# program tworzenia wpisów do dziennika
import datetime
from Database_logs import list_category, list_date, list_entry

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
            list_date.append(datetime.datetime.now())
            # asking the user for his/her log entry
            entry = input('Podaj swój wpis: ')
            # appending list entry
            list_entry.append(entry)
            # save all lists

        elif intent == 'n':
            with open('Database_logs', 'w') as file:
                file.write('list_date = ' + str(list_date) + '\n' + 'list_category = ' + str(list_category) + '\n' +
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

    display = input('Czy wyświetlić wpisy dziennika?(t/n)')
    condition2 = True
    while condition2:
        from Database_logs import list_category, list_date, list_entry
        if display == 't':
            kategoria = input('Podaj kategorię wpisu lub wpisz: wszystkie')
            if kategoria == 'wszystkie':
                for i in range(len(list_date)):
                    print('', list_date[0+i], list_category[0+i], list_entry[0+i], sep='\n')
                    condition2 = False
            elif kategoria not in list_category:
                print('Kategorii nie ma w bazie danych.')
                contition2 = True
            elif kategoria in list_category:
                print(list_category.index(kategoria))
                for i in range(list_category.count(kategoria)):
                    ind2 = list_category.index(kategoria)
                    print('', list_date[ind2], list_category[ind2], list_entry[ind2], sep='\n')
                    condition2 = False
