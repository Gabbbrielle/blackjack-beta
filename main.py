import random
import time
from replit import clear

def play_game():
  deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
  random.shuffle(deck)
  player = []
  py = []
  player_stand = False
  # house_stand = False
  def bust(who):
      if sum(who) > 21 and 11 not in who:
          print(f"{sum(who)}, You bust.")
          if who == player:
              flag = True
              return flag
          elif who == py:
              flag = True
              return flag
      elif sum(who) > 21 and 11 in who:
          ace = who.index(11)
          who.remove(11)
          who.insert(ace, 1)
          time.sleep(2)
          print(f"\nAce has been changed to 1.\nYour hand is {', '.join(map(str,player))}\nYour new total is {sum(who)}\n")
          flag = False
          return flag
      else:
          flag = False
          return flag
  
  def hit(who, num):
      """add to the player determined in the first parameter, the number of card in the second parameter to the player's hand """
      draw = random.sample(deck,num)
      for card in draw:
          who.append(card)
      if who == player:
          print(f'\n{", ".join(map(str,player))}')
          print(f"Your total is {sum(player)}")
      elif who == py and num == 2:
          time.sleep(1)
          print(f"dealer shows {py[0]}\n")
      elif who == py and num == 1:
          time.sleep(1)
          print(", ".join(map(str,py)))
          print(f"Dealer's total is {sum(py)}\n ")

  def evaluate_blackjack(who):
      """Will evaluate if there is a blackjack and 'stand' the user specified in the parameter by changing the flag to True  """
      if sum(who) == 21:
          print("Blacjack!")
          flag = True
          return flag

  def py_play():
      """automates the computer play according to basic blackjack rules. Draws a card until a min of 17 then evaluate eithe a bust or a stand """
      print(f"\nDealer has {', '.join(map(str,py))}\nDealer's total is {sum(py)}\n")
      if player_stand == True and sum(player) > 21:
        evaluate_game()
      else:
        time.sleep(1)
        while sum(py) < 17:
            hit(py, 1)
            time.sleep(1)
        time.sleep(1)
        if sum(py) in range(17, 22):
            print(f"Dealer stand at {sum(py)}")
            # flag = True
            # return flag
        elif sum(py) > 21:
            print(f"{sum(py)}, dealer losts" )

  def evaluate_game():
      """evaluate who has won the game based on the hand total of each player including the computer's hand. Returns the winner """
      if sum(player) > sum(py) and sum(player) <= 21:
          print(f"\nYou have {sum(player)}, player wins")
      elif sum(player) == sum(py):
          print(f"\n{sum(player)} to {sum(py)}. Game is a draw")
      elif sum(player) < sum(py) and sum(py) <= 21:
        print(f'\n{sum(py)} for dealer, {sum(player)} for player. Dealer wins')
      play_again = input("Do you want to play again? y or n ")
      if play_again == "y":
        play_game()
      else:
        clear()
        print("goodbye")

  hit(player, 2)
  # stand_player = evaluate_blackjack(player)
  hit(py, 2)

  while player_stand == False:
      if sum(player) == 21:
        player_stand = True
      else:
        time.sleep(1)
        x = input("hit or stand? ")
        if x == "hit":
            hit(player, 1)
            player_stand = bust(player)
        else:
            print(f"Your total is {sum(player)}")
            player_stand = True
  time.sleep(1)
  py_play()
  evaluate_game()
play_game()


   
