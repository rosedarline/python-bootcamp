users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

#using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

#using map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))

#list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]



