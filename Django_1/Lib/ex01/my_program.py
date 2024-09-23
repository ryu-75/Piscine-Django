#!/bin/python3

from local_lib.path import path

def main():
    directory = path.Path('directory')
    
    if directory.exists() is False:
        directory.mkdir()
    else:
        print("Directory is already exist")
    
    file = path.Path('file.txt')
    directory.cd()
    
    if file.exists() is False:
        file.touch()
    else:
        print("File is already exist")
    
    file.chmod(0o777)
    file.write_text(text='Hello world !\n', encoding='utf-8', append=True)
    
    

if __name__ == '__main__':
    main()