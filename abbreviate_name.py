#Given a person's name, return the person's initials (uppercase)
def get_initials(fullname):
    return '.'.join([x[0].upper() for x in fullname.split(' ')])

answer = get_initials("Ozzie Smith")
print(f"The initials are {answer}") 