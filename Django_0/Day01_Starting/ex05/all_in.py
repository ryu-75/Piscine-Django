import sys

def all_in():
    if len(sys.argv) - 1 < 1:
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
    
    args = sys.argv[1:]
    
    for arg_list in separate_arguments(args[0]):
        arg = arg_list[0]
        if arg.capitalize() in states and states[arg.capitalize()] in capital_cities:
            print(f"{arg} is the state of {capital_cities[states[arg.capitalize()]]}")
        elif arg.capitalize() in capital_cities.values():
            for capital_acronym, city in capital_cities.items():
                if city == arg.capitalize():
                    for state, state_acronym in states.items():
                        if state_acronym == capital_acronym:
                            print(f"{arg} is the capital city of {state}")
        else:
            print(f"{arg} is neither a capital city nor a state")
            
#************************************************************************************************

def separate_arguments(args):
    return [[word] for word in args.replace(',', ' ').split()]
    
# ************************************************************************************************
all_in()