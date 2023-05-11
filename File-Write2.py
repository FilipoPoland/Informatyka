with open('Data.txt', 'r') as file:
    counter = 0
    for i in range(100000):
        counter += 1
        print(f"{i}: {file.readline(i+1).encode('UTF-8')}")
