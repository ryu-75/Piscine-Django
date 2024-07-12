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
    for i in content:
        print(content[i], "est de type", type(content))

# ****************************************************************

my_var()