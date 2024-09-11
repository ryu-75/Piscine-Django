class HotBeverage:
	def __init__(self, name=None, price=None):
		if name is None and price is None:
			self.name = "hot beverage"
			self.price = 0.30
		else:
			self.name = name
			self.price = price

	def description(self):
		return "Just some hot water in a cup"

	def __str__(self):
		print("name : ", self.name)
		print("price : ", self.price)
		print("description: ", self.description())

class Coffee(HotBeverage):
	def __init__(self, name, price):
		HotBeverage.__init__(self, name, price)

	def description(self):
		return "A coffee, to stay awake."

def main():
	# Hot Beverage
	hot_beverage = HotBeverage()
	hot_beverage.__str__()
	print()

	# Coffee
	coffee = Coffee("coffee", 0.40)
	coffee.__str__()
	print()

	#Tea

	# Chocolate

	# Cappuccino

if __name__ == '__main__':
	main()
