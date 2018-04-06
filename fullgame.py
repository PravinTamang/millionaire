import random
import time
import millionaire


#take name
global name
name = raw_input("Hello, welcome to Who Wants to be a Millionaire! What is your name?" + "\n")

#call introduction function
millionaire.intro(name)

#counters
lifeline_fifty = 0
lifeline_friend = 0
lifeline_audience = 0
j = 0
global i
i = 1
global money
money = ['100','200','300','500','1000','2000','4000','8000','16000','32000','64000','125000','250000','500000','1000000']

answerlist = ["A","B","C","D", "Correct"]

#open random line in file

while i <= 16:
	f = (random.choice(list(open('test.txt'))))
	lines = f.split('[')
	global question
	question = lines[0]
	global answers
	answers = lines[1].strip("\n").split(',')

	print 'Question:', i, "for", money[i-1]

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
	 

	answerdict = {
	'A' : answers[0],
	'B' : answers[1],
	'C' : answers[2],
	'D' : answers[3],

	}
	
	select = raw_input("Select an answer " + name + ":\n")
	select = select.upper()


	#50/50 lifeline
	if select == "1":
		if lifeline_fifty == 0:
			select = millionaire.fifty(answers,money,name,question,i)
			lifeline_fifty = 1
		elif lifeline_fifty != 0:
			print "You've already used this lifeline!"
			i = i - 1

	#Phone a friend lifeline 
	if select == "2":
		if lifeline_friend == 0:
			select = millionaire.friend(answers,money,name,question,i)
			lifeline_friend = 1
		elif lifeline_friend != 0:
			print "You've already used this lifeline!"
			i = i - 1

	#Ask the audience lifeline 
	if select == "3":
		if lifeline_audience == 0:
			select = millionaire.audience(answers,money,name,question,i)
			lifeline_audience = 1
		elif lifeline_audience != 0:
			print "You've already used this lifeline!"
			i = i - 1
		 
	
	if select in answerdict:
		if answerdict[select] == answers[4] and i <= 14:
			print 'Correct\nYou are one step closer to being a Millionaire' +"\n" 
		elif i == 15:
			print "Congratulations. You are a millionaire!"
			time.sleep(5)
			break
		else:
			print 'Hard luck ' + name  + ', Game over'							
			break
		
	if len(select) > 2:
		print "DQ"
		break

	i = i + 1
	
