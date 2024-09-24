import sys, requests
from bs4 import BeautifulSoup

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

def find_first_link(el):
    content = {
        'title': '',
        'link': ''
    }
    
    for p in el.find_all('p'):
        for a in p.find_all('a'):
            href = a.get('href', '')
            title = a.get('title', '')
            if href.startswith('/wiki/') and not href.startswith(('/wiki/Help', '/wiki/Special', '#', '/wiki/Wikipedia', '/wiki/File')):
                print(href) 
                content['title'] = title
                content['link'] = href
                return content
    print("Links are not found.")
    return content

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} `cat`")
        sys.exit(1)
    
    wiki_link = f"https://en.wikipedia.org/wiki/{sys.argv[1]}"
    r = requests.get(wiki_link)
    nb_road = 0
    visitedLink = set()
    
    # Fetch the data if the request success
    if r.status_code != 200:
        print("It's a dead end !")
        sys.exit(1)
        
    soup = BeautifulSoup(r.text, 'html.parser')
    content = []
     
    # Find the first link in introduction paragraph
    el = soup.find('div', class_='mw-parser-output')
    scrap = find_first_link(el)
    content.append(sys.argv[1])
    
    # Check if a link exist
    if scrap is not None:
        content.append(scrap['title'])
    else:
        print("It's a dead end !")
        sys.exit(1)
        
    # We loop until Philosophy is found
    while 1:    
        if not scrap['link']:
            print("Link is not exist")
            sys.exit(1)
        
        # We visit all links until philosophy is found
        if '/wiki/' in scrap['link']:
            l = f"https://en.wikipedia.org{scrap['link']}"
            if l not in visitedLink:
                visitedLink.add(l)
                req = requests.get(l)
                if (req.status_code != 200):
                    print(f"Error: {req.status_code}")
                    sys.exit(1)
                soup = BeautifulSoup(req.text, 'html.parser')
                el = soup.find('div', class_='mw-parser-output')
                scrap = find_first_link(el)
                nb_road += 1
                content.append(scrap['title'])
                if scrap['title'] == 'Philosophy':
                    content.append(f"{nb_road} roads from {sys.argv[1]} to philosophy")
                    break
            else:
                print("Link already visit")
                sys.exit(1)
        else:
            print("Link is invalid")
            sys.exit(1)
    