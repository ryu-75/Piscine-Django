import sys, requests
from bs4 import BeautifulSoup

class roads_to_philosophy:
    step: int = 1
    
    def __init__(self) -> None:
        self.visitedLink = set()
        self.content = []

    def fetch_wikipage(self, link: str):
        try:
            res = requests.get(link)
            res.raise_for_status()
            return res
        except requests.HTTPError as e:
            if res.status_code == 404:
                print("It's a dead end")
                sys.exit(1)
            print("An error occurred: {e}")
            sys.exit(1)
        

    def scrap_wikipedia(self, link: str):
        wiki_link = f"https://en.wikipedia.org/wiki/{link}"
        # Fetch the webpage
        res = self.fetch_wikipage(wiki_link)
        # Parse the html content
        soup = BeautifulSoup(res.text, 'html.parser')
        # Find the first link in introduction paragraph
        el = soup.find('div', id='mw-content-text')
        scrap = self.find_first_link(el)
        # Add the starting page and the first link from the first paragraph
        self.content.append(sys.argv[1])
        self.content.append(scrap['title'])
        self.step += 1
        # Loop through the article until 'Philosophy' is found
        while scrap['title'] != 'Philosophy':    
            if not scrap['link']:
                print("There is no link to visited.")
                sys.exit(1)
            # Visit the next link if it's lead to a wikipedia page
            if '/wiki/' in scrap['link']:
                wiki_link = f"https://en.wikipedia.org{scrap['link']}"
                # Check if the link is already visited or not
                if wiki_link not in self.visitedLink:
                    self.visitedLink.add(wiki_link)
                    # Repeat the second operation
                    res = self.fetch_wikipage(wiki_link)
                    soup = BeautifulSoup(res.text, 'html.parser')
                    el = soup.find('div', id='mw-content-text')
                    scrap = self.find_first_link(el)
                    self.content.append(scrap['title'])
                    self.step += 1
                else:
                    print("It leads to an infinite loop !")
                    sys.exit(1)
            else:
                print("Link is invalid")
                sys.exit(1)
        self.display_visited_link(self.content)
        print(f"{self.step} roads from {sys.argv[1]} to philosophy !")

    
    def display_visited_link(self, content):
        for title in content:
            print(title)

    def find_first_link(self, el):
        content = {
            'title': '',
            'link': ''
        }
        
        for p in el.find_all('p'):
            for a in p.find_all('a'):
                href = a.get('href', '')
                title = a.get('title', '')
                if href.startswith('/wiki/') and not href.startswith(('/wiki/Help', '/wiki/Special', '#', '/wiki/Wikipedia', '/wiki/File', '/w/', "https")):
                    content['title'] = title
                    content['link'] = href
                    return content
        print("Links are not found.")
        return content

if __name__ == '__main__':
    if len(sys.argv) == 2 and len(sys.argv[1]) != 0:
        philosophy = roads_to_philosophy()
        philosophy.scrap_wikipedia(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} `cat`")
        sys.exit(1)
        
    

    