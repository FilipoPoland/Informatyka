import datetime

condition = True
list_category = []
list_date = []
list_entry = []
while True:
    while condition:
        intent = input('Do you wish to make a log entry?(y/n)')
        if intent == 'y':
            category = input('What is the category of your log entry?\n'
                             'Personal / Medical / Engineering / Navigation / Observations / Security')
            # adding the category to the list
            list_category.append(category)
            # assign date
            list_date.append(datetime.date.today())
            # asking the user for his/her log entry
            entry = input('Please provide the log entry: ')
            # appending list entry
            list_entry.append(entry)
        elif intent == 'n':
            condition = False

    display = input('Do you wish to display a log entry?(y/n)')
    if display == 'y':
        index = input('Please provide the index of the entry you would like to display')
        if index == 'all':
            for i in range(len(list_date)):
                print('', list_date[0+i], list_category[0+i], list_entry[0+i], sep='\n')
        else:
            print('', list_date[int(index)], list_category[int(index)], list_entry[int(index)], sep='\n')
    elif display == 'n':
        condition = True
