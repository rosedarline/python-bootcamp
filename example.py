# # The __repr__ method
# class Person:
#     name = 'Rose'

#     def __repr__(self):
#         return repr(self.name)

# rose = Person()
# print(f"{rose} is totally awesome!")

class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
    
    def speak(self):
        return f"{self.name} I heard there were monsters running around last night"
        