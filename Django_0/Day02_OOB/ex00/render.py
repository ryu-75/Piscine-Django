from setting import name, age, first, job, title
import	sys
import  os

def edit_file():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <template file>")
        exit (1)
    
    template_file = sys.argv[1]
    
    if not template_file.endswith(".template"):
        print(f"Error: {template_file} should have 'template' has extension")
    try:
        with open(sys.argv[1], "r") as file:
            template = file.read()  
        create_html = open("myCV.html", "w")
        create_html.write(f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
</head>
<body>
    {template.replace("{name}", name)}
    <p>What is your firstname ? {first}</p>
    <p>How old are you ? {age} years old</p>
    <p>Ok, then. What is your job ? I'm a {job}</p> 
</body>
</html>
''')
    except FileNotFoundError:
        print(f"Error: {sys.argv[1]} is not found")
        
def main():        
    edit_file()
    
if __name__ == '__main__':
    main()
    
