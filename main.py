import random
myname=input("Please enter you name= ")
print(myname)
number,guess=random.randint(1,10),0
guess=int(input("Take a guess: "))
if guess==number:
  print("Well done", myname, "you gussed the number")
else:
  print("Incorrect, better luck next time")