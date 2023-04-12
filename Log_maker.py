# program tworzenia wpisów do dziennika
import datetime

print('Dziennik: ')
condition = True
list_category = []
list_date = []
list_entry = []
while True:
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
            with open('Database_logs', 'w') as file:
                file.write('list_date = ' + str(list_date) + '\n' + 'list_category = ' + str(list_category) + '\n' +
                           'list_entry = ' + str(list_entry))
        elif intent == 'n':
            condition = False

    display = input('Czy wyświetlić wpisy dziennika?(t/n)')
    condition2 = True
    while condition2:
        if display == 't':
            kategoria = input('Podaj kategorię wpisu lub wpisz: wszystkie')
            if kategoria == 'wszystkie':
                for i in range(len(list_date)):
                    print('', list_date[0+i], list_category[0+i], list_entry[0+i], sep='\n')
                    condition2 = False
            elif kategoria != list_category[kategoria]:
                print('Kategorii nie ma w bazie danych.')
                contition2 = True
            elif kategoria == list_category[kategoria]:
                print(list_category.index(kategoria))
                for i in range(list_category.count(kategoria)):
                    print('', list_date[0+i], list_category[kategoria], list_entry[0+i], sep='\n')
                    condition2 = False
