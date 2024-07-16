import sys

def state():
    if len(sys.argv) - 1 != 1:
        print(f"Usage: {sys.argv[0]} <STATE or CITY>")
        exit(1)

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    arg = sys.argv[1]
    
    if arg.capitalize() in states and states[arg.capitalize()] in capital_cities:
        print(capital_cities[states[arg.capitalize()]])
    elif arg.capitalize() in capital_cities.values():
        for capital_acronym, city in capital_cities.items():
            if city == arg.capitalize():
                for state, state_acronym in states.items():
                    if state_acronym == capital_acronym:
                        print(state)
    else:
        print("Unknown state")

#************************************************************************************************

def main():
    state()

if __name__ == '__main__' :
    main()
