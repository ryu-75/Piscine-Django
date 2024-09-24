class Coffee:
	def __str__(self):
		return "This is the worst coffee you ever tasted"

	def work(self):
		return Exception(f"I’m just an intern, I can’t do that...")

# Inherit Coffee class
class Intern(Coffee):
	# Constructor
	def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
		self.name = name

	# Getter
	def __str__(self):
		return self.name

	# Instance of Coffee class
	def make_coffee(self):
		return Coffee()

def main():
	internA = Intern()
	internB = Intern("Mark")

	print(f"InternA : ", internA.__str__())
	print(f"InternB : ", internB.__str__())

	print(f"InternA : ", internA.work())
	print(f"InternB : ", internB.make_coffee())

if __name__ == '__main__':
	main()
