import random
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
A = deck[0]
J = deck[9]
Q = deck[10]
K = deck[11]

deck2 = {
  "clubs (♣)":[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
  "diamonds (♦)": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
  "hearts (♥)": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
  "spades (♠)": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
}

def hit(x): 
    hand_py.append(random.sample(deck,x))
    hand_player.append(random.sample(deck,x))



sample = random.sample(deck, 3)
print(sample)
def hand_sum():
  if hand_sum() > 21:
    A = 1
