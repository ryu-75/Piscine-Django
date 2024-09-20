#!/bin/python3

from local_lib.path import path

def create():
    root = path.Path() 
    
    sub = root / "folder"
    
    if sub.exists():
        print("> Folder is already exist")
        exit 
    else:
        print("> Folder is create")
        sub.mkdir(mode=0o777)
    
    file = sub / "filet.txt"
    
    if file.exists():
        print("> File is already exist")
    else:
        print("> File is not exist yet")
        file.touch()
    
    file.write_lines(lines="Hello world !", encoding='utf-8', append=False)
    
    return file.read_text()
    
def main():
    print(create())
    print("> end")
    
if __name__ == "__main__":
    main()