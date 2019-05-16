# Inheritance Example Using Super()
import pickle
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


# pickling
leo = Cat("Leo","Scottish Fold", "String")
with open("pets.pickle", "wb") as file:
    pickle.dump(leo, file)
# unpickling
with open("pets.pickle", "rb") as file:
    leo_cat = pickle.load(file)
    print(leo_cat)

