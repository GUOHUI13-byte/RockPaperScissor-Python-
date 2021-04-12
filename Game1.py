import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
RPS=[rock,paper,scissors]
Choice=int(input("What is Your Choice : (0 for Rock,1 for Paper,2 for Scissors) \n" ))
if Choice>2 or Choice<0:
  print("Wrong Input")
else:
  print(RPS[Choice])
  
Com_Choice=random.randint(0,2)
print("Computer has chosen\n")
print(RPS[Com_Choice])


if Choice==Com_Choice:
  print("Draw")
elif (Choice==0 and Com_Choice==1):
  print("You Lose") 
elif (Choice==1 and Com_Choice==2):
  print("You Lose")
elif Choice>Com_Choice:
  print("You Win")
