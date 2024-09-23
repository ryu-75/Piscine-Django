import sys, requests
from bs4 import BeautifulSoup

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} `cat`")
        sys.exit(1)
    else:
        r = requests.get(f"https://en.wikipedia.org/wiki/{sys.argv[1]}")
        
        
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            i = 0
            txt = soup.find('body')
            if txt:
                filter_html = filter('<i>', txt)
                
                print(filter_html)
                for link in txt.find('a'):
                    print(link.find('href'))
                
                
                # file = open(f"{sys.argv[1]}.html", "w")
                # file.write(el[0])
                # file.close()
                