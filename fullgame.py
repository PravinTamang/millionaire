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
lifeline_ friend = 0

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
	#time.sleep(3)
	print 'A: ' + answers[0]
	#time.sleep(1)
	print 'B: ' + answers[1]
	#time.sleep(1)
	print 'C: ' + answers[2]
	#time.sleep(1)
	print 'D: ' + answers[3]
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
	select = raw_input("Select an answer " + name + ":\n")
	select = select.upper()

	##if select != "A" or "B" or "C" or "D" or "1" or "2" or "3":
	#	select = raw_input("Please select a valid answer " + name + ":\n")

 

	#50/50 lifeline
	if select == "1":
		millionaire.fifty(answers,money,name)
		lifeline_fifty = 1

	#Phone a friend lifeline 
	if select == "2":
		millionaire.friend(answers,money,name,question)
		lifeline_friend = 2

	#Phone a friend lifeline 
	if select == "3":
		print "Lifeline: Ask the audience"
		time.sleep(1)
		print "Our audience all have remotes and will vote on what they believe to be the right answer"
		time.sleep(2)
		print "Please allow a couple of seconds for the audience to select their answers " + name
		time.sleep(4)
		aud = (random.choice(list(open('asktheaudience.txt'))))
		aud = aud.split(',')
		print "The votes are in"
		time.sleep(1)
		print "A:",answers[0], " ", aud[0]
		print "B:",answers[1], " ", aud[1]
		print "C:",answers[2], " ", aud[2]
		print "D:",answers[3], " ", aud[3]
		time.sleep(1)
		print "\nHopefully you found that helpful"
		time.sleep(1)
		lifeline3 = raw_input("Chris Tarrent: Please select an answer " + name + "\n")
		select = lifeline3.upper()





		 
	
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
	