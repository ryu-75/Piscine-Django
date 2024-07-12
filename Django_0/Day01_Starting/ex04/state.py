import sys

def state():
    if len(sys.argv) - 1 != 1:
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
    
    if sys.argv[1] in states and states[sys.argv[1]] in capital_cities:
        print(capital_cities[states[sys.argv[1]]])
    elif sys.argv[1] in capital_cities.values():
        for capital_acronym, city in capital_cities.items():
            if city == sys.argv[1]:
                for state, state_acronym in states.items():
                    if state_acronym == capital_acronym:
                        print(state)
    else:
        print("Unknown state")
            
#************************************************************************************************

state()