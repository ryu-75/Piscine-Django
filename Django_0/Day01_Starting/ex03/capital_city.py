import sys

def capital_city():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <STATE>")
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

    state_name = sys.argv[1]

    if state_name in states and states[state_name] in capital_cities:
        print(f"{capital_cities[states[state_name]].}")
    else:
        print("Unknown state")

#************************************************************************************************

def main():
    capital_city()

if __name__ == '__main__' :
    main()
