import random
import time
import millionaire

#take name
global name
name = raw_input("Hello, welcome to Who Wants to be a Millionaire! What is your name?" + "\n")

#call introduction function
millionaire.intro(name)

#counters
global money
money = '100'
lifeline_fifty = 0
lifeline_friend = 0
lifeline_audience = 0

answerlist = ["A","B","C","D", "Correct"]

#open randon random line in file
j = 0
i = 1
while i <= 16:
	f = (random.choice(list(open('test.txt'))))
	lines = f.split('[')
	global question
	question = lines[0]
	global answers
	answers = lines[1].strip("\n").split(',')

	print 'Question:', i 

	print question
	print 'A: ' + answers[0]
	print 'B: ' + answers[1]
	print 'C: ' + answers[2]
	print 'D: ' + answers[3]


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
	select = raw_input("Select an answer " + name + ":\n")
	select = select.upper()


	#50/50 lifeline
	if select == "1":
		if lifeline_fifty == 0:
			millionaire.fifty(answers,money,name)
			lifeline_fifty = 1
		elif lifeline_fifty != 0:
			print "You've already used this lifeline!"
			i = i - 1

	#Phone a friend lifeline 
	if select == "2":
		if lifeline_friend == 0:
			millionaire.friend(answers,money,name,question)
			lifeline_friend = 1
		elif lifeline_friend != 0:
			print "You've already used this lifeline!"

	#Ask the audience lifeline 
	if select == "3":
		if lifeline_audience == 0:
			millionaire.audience(answers,money,name,question)
			lifeline_audience = 1
		elif lifeline_audience != 0:
			print "You've already used this lifeline!"
		 
	
	if select in answerdict:
		if answerdict[select] == answers[4]:
			print 'Correct\nYou are one step closer to being a Millionaire' 
		else:
			print 'Hard luck ' + name  + ', Game over'							
			break
		if i == 16:
			print "Congratulations You are a millionaire!"
			time.sleep(5)
			break

	i = i + 1
	