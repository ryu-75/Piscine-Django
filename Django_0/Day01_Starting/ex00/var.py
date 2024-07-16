def my_var():
    content = {
        "first": 42,
        "age": "42",
        "nb": "quarante-deux",
        "monney": 10.50,
        "adult": True,
        "lst": [42],
        "dic": {42: 42},
        "tup": (42,),
        "setting": set()
    }
    for key, value in content.items():
        print(f"{value} est de type {type(value)}")

# ****************************************************************

def main():
    my_var()
    return 0

if __name__ == '__main__':
    main()
