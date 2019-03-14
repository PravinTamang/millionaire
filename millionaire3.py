# Who Wants to Be a Millionaire
# Josh Malone

import sys
import random
import time

def intro(name):
   print("Ok " + name + " this is how the game works:" + "\n")
   time.sleep(2)
   print("You are asked a multiple choice question, with options A, B, C and D.")
   time.sleep(2)
   print("If you get the correct answer, you earn money and move onto the next question.")
   time.sleep(4)
   print("If you guess incorrectly then you lose the money you have earned,")
   time.sleep(2)
   print("although there are checkpoints along the way that allow you to keep a certain amount of money should you get a question wrong further on.")
   time.sleep(4)
   print("The questions increase in difficulty as you progress but you can make use of the 3 'lifelines' we will give you:")
   time.sleep(4)
   print("\n1. 50/50") 
   time.sleep(2) 
   print("This allows you to cut the possible answers from 4, down to 2.\nPress 1 to access")
   time.sleep(4)
   print("\n2. Phone a Friend")
   time.sleep(2)
   print("Place a call to a predetermined friend that will hopefully help you with an answer.\nPress 2 to access")
   time.sleep(4)
   print("\n3. Ask the Audience")
   time.sleep(2) 
   print("Our wonderful people (bots) in the audience will vote on the correct answer and we shall show you the results\nPress 3 to access")
   time.sleep(4)
   print("One more thing, when answering, please use either A, B, C or D or you will be disqualified!")
   time.sleep(2)
   print("\nReady to get started? Lets go!" + "\n" + "===================================================================\n")
   time.sleep(2)

#Lifelines:

#50/50
def fifty(answers,money,name,question, i):
   while True:
      print("Lifeline: 50/50")
      time.sleep(1)
      print("We will select two answers to remove")
      time.sleep(1)
      print("Leaving you with one correct and one incorrect answer")
      #add money counter 
      time.sleep(1)
      print("You're left with the options of: \n",answers[5], "\nor \n",answers[6])
      
      lifeline1 = input("Please select the correct answer "  + name + ":\n")
      select = lifeline1.upper()
   #if trying to use 2 lifelines on one question   
      if select == "2":
         print("You can only use one lifeline per question, sorry.")
         i = i - 1
         continue
      if select == "3":
         print("You can only use one lifeline per question, sorry.")
         i = i - 1
         continue
      if select == "1":
         print("You've already used this lifeline!")
         continue
      return select

#Phone a friend
def friend(answers,money,name,question,i):
   while True:
      print("Lifeline: Phone a friend")
      time.sleep(1)
      friend = input("Please enter the name of the person you want to ring " + name + ":\n")
      print("...dialling " + friend + "... ")
      time.sleep(2)
      print("Hi " + friend + ", " + name + " needs your help!")
      time.sleep(2)
      print("Can you help " + name + " by answering this question?")
      time.sleep(2)
      print(question)
      time.sleep(1)
      print("The possible answers are: ")
      time.sleep(1)
      print('A: ' + answers[0])
      time.sleep(1)
      print('B: ' + answers[1])
      time.sleep(1)
      print('C: ' + answers[2])
      time.sleep(1)
      print('D: ' + answers[3])
      time.sleep(2)
      print(friend + ":" + answers[7])
      lifeline2 = input("Please select an answer " + name + ":\n")
      select = lifeline2.upper()
   #if trying to use 2 lifelines on one question
      if select == "1":
         print("You can only use one lifeline per question, sorry.")
         i = i - 1
         continue
      if select == "3":
         print("You can only use one lifeline per question, sorry.")
         i = i - 1
         continue
      if select == "2":
         print("You've already used this lifeline!")
         continue
      return select

#Ask the Audience
def audience(answers,money,name,question,i):
   while True:
      print("Lifeline: Ask the audience")
      time.sleep(1)
      print("Our audience all have remotes and will vote on what they believe to be the right answer")
      time.sleep(2)
      print("Please allow a couple of seconds for the audience to select their answers " + name)
      time.sleep(4)
      aud = (random.choice(list(open('asktheaudience.txt'))))
      aud = aud.split(',')
      print("The votes are in")
      time.sleep(1)
      print("A:",answers[0], " ", aud[0])
      time.sleep(1)
      print("B:",answers[1], " ", aud[1])
      time.sleep(1)
      print("C:",answers[2], " ", aud[2])
      time.sleep(1)
      print("D:",answers[3], " ", aud[3])
      time.sleep(1)
      print("\nHopefully you found that helpful")
      time.sleep(1)
      lifeline3 = input("Chris Tarrent: Please select an answer " + name + "\n")
      select = lifeline3.upper()
   #if trying to use 2 lifelines on one question
      if select == "1":
         print("You can only use one lifeline per question, sorry.")
         i = i - 1
         continue
      if select == "2":
         print("You can only use one lifeline per question, sorry.")
         i = i - 1
         continue
      if select == "3":
         print("You've already used this lifeline!")
         continue
      return select