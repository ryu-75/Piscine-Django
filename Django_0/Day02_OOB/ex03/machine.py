import beverages
import random
from beverages import HotBeverage, Coffee, Cappuccino, Tea, Chocolate

class CoffeeMachine:
	drinks = 0

	def __init__(self):
		pass

	class EmptyCup(HotBeverage):
		def __init__(self):
			HotBeverage.__init__(self, "empty cup", 0.90)

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.\n")

	def repair(self):
		self.drinks = 0
		return "Coffee machine is repaired\n"

	def serve(self, beverage):
		if (self.drinks == 10):
			raise CoffeeMachine.BrokenMachineException
		elif (round(random.random()) == 1):
			return beverage
		return CoffeeMachine.EmptyCup()


def main():
	coffee_machine = CoffeeMachine()
	coffee = Coffee("coffee", 0.50)
	cappuccino = Cappuccino("cappuccino", 0.45)
	chocolate = Chocolate("chocolate", 0.60)
	tea = Tea("tea", 0.30)
	hot_beverage = HotBeverage("hot beverage", 0.30)
	i = 1

	while coffee_machine.drinks <= 10:
		try:
			if (coffee_machine.drinks != 10):
				if (i == 20):
					break
				coffee_machine.drinks +=1
				i += 1
				print(f"drinks: {coffee_machine.drinks}")
				print(random.choice((
      								coffee_machine.serve(coffee), 
        		               		coffee_machine.serve(chocolate), 
        		                  	coffee_machine.serve(cappuccino), 
        		                    coffee_machine.serve(tea), 
					    			coffee_machine.serve(hot_beverage)
        		  				)))
		except coffee_machine.BrokenMachineException as e:
			print(f"{e}")
			print(coffee_machine.repair())

if __name__ == "__main__":
	main()
