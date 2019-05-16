class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
user1 = User("Leo", "Adam", 2) 
user2 = User("Rose", "Adam", 31)
print(user1.first, user1.last, user1.age)
print(user2.first, user2.last)
