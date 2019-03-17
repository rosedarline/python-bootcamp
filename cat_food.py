print("How old is your cat?")
age = input()
if age:
    age = int(age)
    if age <= 1:
        print("kitten food or 'milk'! ")
    elif age >= 2 and age <= 8:
        print("Cat food Adult! ")
    else:
        print("Cat food for Senoir! ")