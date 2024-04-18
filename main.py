import random

random_card1 = random.randint(1,10)
random_card2 = random.randint(1,10)

botcard1 = random.randint(1,10)
botcard2 = random.randint(1,10)

humanscore = random_card1 + random_card2
print(f"Your cards are {random_card1} and {random_card2} for a total score of {humanscore}\nYour opponent has card {botcard1}")


while humanscore < 21:
  hit = input("Would you like to hit? (y/n) ")
  if hit == "n":
    print(f"Your opponent has a {botcard1} and {botcard2} for a total score of {botcard1 + botcard2}")
  if botcard1 + botcard2 < humanscore:
      print(f"You win! Your opponent had cards {botcard1} and {botcard2} for a total score of {botcard1 + botcard2}")
  elif botcard1 + botcard2 > humanscore:
      print("You lose! Your opponent had cards {botcard1} and {botcard2} for a total score of {botcard1 + botcard2}")
  elif botcard1 + botcard2 == humanscore:
          print(f"It's a draw! Your opponent had cards {botcard1} and {botcard2} for a total score of {botcard1 + botcard2}")
  else:
    humanscore = humanscore + random.randint(1,10)
    print(f"You got a {humanscore - (random_card2 + random_card1)} for a total score of {humanscore}. Your opponent had cards {botcard1} and {botcard2} for a total score of {botcard1 + botcard2}")
        
        
    

