#!/bin/python3

import requests, json, sys, dewiki

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./request__wikipedia.py `cat`")
        sys.exit(1)
    else:
        searched = sys.argv[1]
        wiki_link = f"https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles={sys.argv[1]}"
        r = requests.get(wiki_link)
        
        if r.status_code != 200 or len(r.text) == 0:
            print("An error occured. Data cannot be fetch")
            sys.exit(1)
        else:
            data = r.json()
            
            if 'query' not in data:
                print("Error")
                sys.exit(1)
            wiki_data = next(iter(data['query']['pages'].values()))
            if 'revisions' in wiki_data:
                wiki_content = wiki_data['revisions'][0]['*']
                wiki_text = dewiki.from_string(wiki_content)
                create = open(f"{sys.argv[1]}.wiki", "w")
                create.write(wiki_text)
                create.close()
            else:
                print("They is not revisions in data")