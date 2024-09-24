import sys, requests
from bs4 import BeautifulSoup

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

def find_first_link(el):
    content = {
        'title': '',
        'link': ''
    }
    
    if el:
        p_el = ""
        for p in el.find_all('p'):
            if not p.get_text(strip=True):
                continue
            else:
                p_el = p
                break
        if p_el and p_el.find('a'):
            content['title'] = p_el.a['title']
            content['link'] = p_el.a['href']
        else:
            print("DOM element is not found")
            sys.exit(1)
    return content

def cut_title(str, length):
    if len(str) > length:
        return str[:length]
    return str

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} `cat`")
        sys.exit(1)
    
    wiki_link = f"https://en.wikipedia.org/wiki/{sys.argv[1]}"
    r = requests.get(wiki_link)
    nb_road = 0
    
    # Fetch the data if the request success
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        content = []
        
        # Find the first link in introduction paragraph
        el = soup.find('div', class_='mw-parser-output')
        scrap = find_first_link(el)
        content.append(sys.argv[1])
        content.append(scrap['title'])
        # Loop until Philosophy is met
        while scrap['title'] != 'Philosophy':
            print(scrap['link'])
            if not scrap['link']:
                print("Link is not exist")
                sys.exit(1)
            if 'wiki/' in scrap['link']:
                l = f"https://en.wikipedia.org{scrap['link']}"
                req = requests.get(l)
                print(req)
                if (req.status_code == 200):
                    soup = BeautifulSoup(req.text, 'html.parser')
                    el = soup.find('div', class_='mw-parser-output')
                    scrap = find_first_link(el)
                    nb_road += 1
                    content.append(scrap['title'])
                    print(content)
                    if scrap['title'] == 'Philosophy':
                        content.append(f"{nb_road} roads from {sys.argv[1]} to philosophy")
                        break
                else:
                    print("An error occured")
            else:
                print("Link is invalid")
                sys.exit(1)
    else:        
        print("It's a dead end !")
    