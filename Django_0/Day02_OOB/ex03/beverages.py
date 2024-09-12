class HotBeverage:
	def __init__(self, name=None, price=None):
		self.name = name if name is not None else "hot beverage"
		self.price = price if price is not None else 0.30

	def description(self):
		return "Just some hot water in a cup"

	def __str__(self):
		return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}\n"

# *************************************************************

class Coffee(HotBeverage):
	def __init__(self, name, price):
		HotBeverage.__init__(self, name, price)

	def description(self):
		return "A coffee, to stay awake."

# *************************************************************

class Tea(HotBeverage):
	def __init__(self, name, price):
		HotBeverage.__init__(self, name, price)

	def description(self):
		return "Just some hot water in a cup."

# *************************************************************

class Chocolate(HotBeverage):
	def __init__(self, name, price):
		HotBeverage.__init__(self, name, price)

	def description(self):
		return "Chocolate, sweet chocolate..."

# *************************************************************

class Cappuccino(HotBeverage):
	def __init__(self, name, price):
		HotBeverage.__init__(self, name, price)

	def description(self):
		return "Un po’ di Italia nella sua tazza!"

# *************************************************************
