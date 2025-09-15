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


ch=[rock,paper,scissors]

cc= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if cc==0:

  print(rock)
if cc==1:
    print(paper)
if cc==2:
    print(scissors)
print("campuetr choice")
ch1 =random.randint(0,2)
print(ch[ch1])

if cc==0 and ch1==0:
    print("drwo")
if cc==1 and ch1==1:
    print("drwo")
if cc==2 and ch1==2:
    print("drwo")

if cc==0 and ch1==1:
    print("you lose")
if cc==1 and ch1==2:
   print("you lose")
if cc==2 and ch1==0:
    print("you lose")

if cc==0 and ch1==2:
    print("you win")
if cc==1 and ch1==0:
   print("you win")
if cc==2 and ch1==1:
    print("you win")

