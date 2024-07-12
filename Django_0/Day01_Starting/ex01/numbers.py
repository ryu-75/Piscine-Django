def read_file(filename):
    f = open(filename, 'r')
    numbers = f.read().split(',')  
    for x in numbers:
        print(x)
        
# ***********************************************

read_file("numbers.txt")