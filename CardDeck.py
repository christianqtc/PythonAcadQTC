import random

cardnum = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King'}
cardsuit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

print("Card drawn is a:", random.choice(cardnum), "of", random.choice(cardsuit))
