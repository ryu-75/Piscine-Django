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
			exc = CoffeeMachine.BrokenMachineException
			return exc()
		elif (round(random.random()) == 1):
			return beverage
		return CoffeeMachine.EmptyCup()


def main():
	coffee_machine = CoffeeMachine()
	coffee = Coffee("coffee", 0.50)
	i = 0

	while coffee_machine.drinks <= 10:
		if (i == 20):
			break
		print(f"drinks: {coffee_machine.drinks}")
		print(coffee_machine.serve(coffee))
		if (coffee_machine.drinks == 10):
			print(coffee_machine.repair())
		coffee_machine.drinks +=1
		i += 1

if __name__ == "__main__":
	main()
