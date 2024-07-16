def open_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    return (parse_file_content(lines))

        
def parse_file_content(lines):
    tabs = {}

    for line in lines:
        name, properties_str = line.split('=')
        name = name.strip()
        
        properties_list = properties_str.split(',')
        properties = {}
        for prop in properties_list:
            key, value = prop.split(':')
            properties[key.strip()] = value
        tabs[name] = properties
    return tabs

def html_content(molecules):
    index = 0
    name = '''  <tr>
            '''
    for molecule, properties in molecules.items():
        while index < int(properties['position']):
            name +='''    <td style="padding:1rem;"></td>
            '''
            index += 1
        name += f'''    <td>
                    <h4 style="background-color: lightblue; text-align: center">{molecule}</h4>
                    <ul style="list-style: none">
                        <li>N°{properties['number']}</li>
                        <li style="font-weight: bold">{properties['small'].strip()}</li>
                        <li>{properties['molar']}</li>
                    </ul>
                </td>
            '''
        index += 1
        if index == 18:
            name +='''</tr>'''             
            if molecule != "Ununoctium":
                name +='\n'             
                name +='''            <tr>
            '''          
            else:
                break  
            index = 0
    return name

def periodic_table_html(filename):
    html = open("periodic_table.html", "w")
    molecules = open_file(filename)
    
    html.write('''
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='utf-8'>
        <meta name='viewport' content='width=device-width initial-scale=1.0'>
        <title>Periodic Table</title>
        <style>
            li {
                padding: 0px 14px;
                margin: 5px;
            }
        </style>
    </head>
    <body>
        <h1>Periodic Table</h1>
        <table>
          ''')
    
    html.write(html_content(molecules))
    
    html.write('''
        </table>
    </body>
    </html>
    
    ''')
    
    html.close()

def main():
    periodic_table_html("periodic_table.txt")
    
if __name__ == '__main__':
    main()