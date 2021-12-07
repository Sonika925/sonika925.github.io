#let's play game 
""" rock+paper=paper
 rock+scissor=rock
 paper+scissor=scissor
 """
import random
you= input("enter (rock,paper,scissor) one of them: ")
list=["rock","paper","scissor"]
computer=random.choice(list)
print(computer)
if you==computer:
    print("huh! draw")
elif((you=="paper" and computer=="rock") or (you=="rock" and computer=="scissor") or (you=="scissor" and computer =="paper")):
    print("Great you won!!")
else:
    print("oops computer won")
print("ThankYou!!")