import art
import random

EASY_TURNS=10
HARD_TURNS=5

def Check_ans(guess,answer,turns):
  if answer<guess:
    print("Too high")
    return turns-1
  elif guess<answer:
    print("Too Low")
    return turns-1
  else:
    print(f"You won the answer was:{answer}.")

    
def Set_difficulty():
  level=input("chosse a difficulty.Type 'easy' or 'hard'.\n")
  if level=="easy":
    return EASY_TURNS

  else:
    return HARD_TURNS

def Play():
  print(art.logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer=random.randint(0,100)

  turns=Set_difficulty()
  guess=0
  while guess != answer:
    print(f"You have {turns} attempts left")
  
    guess=int(input("Make a guess:"))
  
    turns=Check_ans(guess,answer,turns)
    if turns==0:
      print("You lost. Ran out of turns")
    elif guess!=answer:
      print("Guess again")


Play()

