import random
import time
name = input("Please enter your name:\n")

answerlist = ["A","B","C","D", "Correct"]

#open randon random line in file
j = 0
i = 1
while i <= 16:
	f = (random.choice(list(open('test.txt'))))
	lines = f.split('[')
	question = lines[0]
	answers = lines[1].strip("\n").split(',')

	print 'Question:', i 

	print(question)
	#time.sleep(3)
	print('A: ' + answers[0])
	#time.sleep(1)
	print('B: ' + answers[1])
	#time.sleep(1)
	print('C: ' + answers[2])
	#time.sleep(1)
	print('D: ' + answers[3])
	#time.sleep(1)

	#assigning values to answers
	a = random.choice(answers)
	b = random.choice(answers)
	c = random.choice(answers)
	d = random.choice(answers)
	# print a , b , c , d 

	answerdict = {
	'A' : answers[0],
	'B' : answers[1],
	'C' : answers[2],
	'D' : answers[3],

	}
	#print answers[4]
	select = input("Select an answer " + name + ":\n")
	select = select.upper()
	
#phone a friend idea

	#Phone a friend
	if select == "2":
		print("Lifeline: Phone a friend")
		#time.sleep(1)
		friend = input("Please enter the name of the person yout want to ring " + name + ":\n")
		print("...dialling " + friend + "... ")
		#time.sleep(2)
		print("Hi " + friend + " it's Chris Tarrent here, " + name + " needs your help!")
		print("Can you help " + name + " by answering this question")
		#time.sleep(1)
		print(question)
		print('A: ' + answers[0])
		print('B: ' + answers[1])
		print('C: ' + answers[2])
		print('D: ' + answers[3])
		print(friend + ":" + answers[7])
		lifeline2 = input("Chris Tarrent: Please select an answer " + name + "\n")
		select = lifeline2.upper()
		 
		#phone a friend

	if select == "1":
		print("Lifeline: 50/50")
		#time.sleep(1)
		print("We will select two answers to remove")
		print("Leaving you with one correct and one incorrect answer")
		print("for ' '  please select the correct answer" )
		#add money counter 
		#time.sleep(1)
		print(answers[5])
		print(answers[6])
		lifeline1 = input("Chris Tarrent: Please select an answer " + name + "\n")
		select = lifeline1.upper()
		 
	
	if select in answerdict:
		if answerdict[select] == answers[4]:
			print('Correct\n')
		else:
			print('Hard luck ' + name  + ', Game over')
			break
		if i == 16:
			print("Congratulations You are a millionaire")
			time.sleep(5)
			break

	i = i + 1