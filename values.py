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



sample = random.sample(deck, 3)
print(sample)
def hand_sum():
  if hand_sum() > 21:
    A = 1
