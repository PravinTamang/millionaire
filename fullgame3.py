import random
import time
import millionaire3


#take name
global name
name = input("Hello, welcome to Who Wants to be a Millionaire! What is your name?" + "\n")

#call introduction function
millionaire3.intro(name)

#counters
lifeline_fifty = 0
lifeline_friend = 0
lifeline_audience = 0
j = 0
global i
i = 1
global money
money = ['$100','$200','$300','$500','$1000','$2000','$4000','$8000','$16000','$32000','$64000','$125000','$250000','$500000','$1000000']

answerlist = ["A","B","C","D", "Correct"]

#open random line in file
questionList = list(open("test.txt"))


while i <= 16:
	f = questionList.pop(random.randint(0,len(questionList) - 1))
	lines = f.split('[')
	global question
	question = lines[0]
	global answers
	answers = lines[1].strip("\n").split(',')

	print('Question:', i, "for", money[i-1])
	time.sleep(1)
	print(question)
	time.sleep(1)
	print('A: ' + answers[0])
	time.sleep(1)
	print('B: ' + answers[1])
	time.sleep(1)
	print('C: ' + answers[2])
	time.sleep(1)
	print('D: ' + answers[3])
	time.sleep(1)
	
	 

	answerdict = {
	'A' : answers[0],
	'B' : answers[1],
	'C' : answers[2],
	'D' : answers[3],

	}
	
	select = input("Select an answer " + name + ":\n")
	select = select.upper()


	#50/50 lifeline
	if select == "1":
		if lifeline_fifty == 0:
			select = millionaire3.fifty(answers,money,name,question,i)
			lifeline_fifty = 1
		elif lifeline_fifty != 0:
			print("You've already used this lifeline!")
			i = i - 1

	#Phone a friend lifeline 
	if select == "2":
		if lifeline_friend == 0:
			select = millionaire3.friend(answers,money,name,question,i)
			lifeline_friend = 1
		elif lifeline_friend != 0:
			print("You've already used this lifeline!")
			i = i - 1

	#Ask the audience lifeline 
	if select == "3":
		if lifeline_audience == 0:
			select = millionaire3.audience(answers,money,name,question,i)
			lifeline_audience = 1
		elif lifeline_audience != 0:
			print("You've already used this lifeline!")
			i = i - 1
		 
	
	if select in answerdict:
		if answerdict[select] == answers[4]:
			time.sleep(1)
			print('\n' + 'That is the correct answer.' + "\n")
		if i > 10 and i < 15:
			print("You are one step closer to being a millionaire." + "\n")
		if i == 15:
			print("Congratulations. You are a millionaire!")
			time.sleep(5)
			break		
	if select in answerdict:
		if answerdict[select] != answers[4]:
			print('Hard luck ' + name  + ', Game over. The right answer is', str(answers[4]) + "!")
			break
		
	if len(select) > 1:
		print("You have been disqualified, sorry!")
		break

	i = i + 1
	
