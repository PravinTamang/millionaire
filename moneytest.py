
f = open("money.txt")
for money in f.readlines():
	money = money.strip("\n").split(".")
	
