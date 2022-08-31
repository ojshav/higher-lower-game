from art import logo
from art import vs
from game_data import data
import random
from replit import clear
def random_account():
  return random.choice(data)

def info(account):
  name = account["name"]
  description =account["description"]
  country = account["country"]
  return f"{name}, is a {description} from {country}"
def check_answer(guess,a_followers,b_foolowers):
  if a_followers > b_foolowers:
    return guess == "a"
  else:
    return guess == "b"
  
def play():
  print(logo)
  score = 0
  should_continue = True
  player_A = random_account()
  player_B = random_account()
  while should_continue:
    player_A = player_B
    player_B = random_account()
    while player_A == player_B:
      player_B = random_account()
    print(f"compare A :{info(player_A)}")
    print(vs)
    print(f"compare B :{info(player_B)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    A_followers_count = player_A["follower_count"]
    B_followers_count = player_B["follower_count"]
    is_correct = check_answer(guess,A_followers_count,B_followers_count)
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

play()

      
  
  
