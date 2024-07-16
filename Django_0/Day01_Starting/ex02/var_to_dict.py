# We create and return a dict with the content of d
def create_dict():
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]

    dic = {}
    for name, year in d:
        dic[year] = name

    return dic

# ****************************************************************

# We loop through the dictionnary to display the content from create_dict()
def display_dict():
    for year, name in create_dict().items():
        print(f"{year} : {name}")

# ****************************************************************

def main():
    display_dict()

if __name__ == '__main__' :
    main()
