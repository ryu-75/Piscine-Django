def read_file(filename):
    f = open(filename, 'r')
    numbers = f.read().split(',')
    for x in numbers:
        print(x)

# ***********************************************

def main():
    read_file("numbers.txt")
    return 0

if __name__ == '__main__' :
    main()
