def play():
  import random 
  dice=random.choice([1,2,3,4,5,6])

  print("Number on dice is ",dice)
  print()

  choice=input("Do you want to roll the dice again? ").strip().lower()
  print()
  if choice=="yes":
    play()
  else:
      print("Thank you for playing ")
start=input(" Do you want to start the rolling the dice ? ").strip().lower()
if start=="yes":
    play()
else:
    print("Bye bye ")