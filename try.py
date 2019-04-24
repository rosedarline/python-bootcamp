# THE BASIC SYNTAX:

def get(d,key):
	try:
		return d[key]
	except KeyError:
		return None
d = {"name": "Julio"}
print(get(d, "city"))
d["city"]






























# try:
# except:
# else:
# finally: