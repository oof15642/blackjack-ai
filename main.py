# Imports
import random
from time import sleep

# Variables
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10", "ace"]

deck = [[rank, suit] for suit in suits for rank in ranks]

# Functions
def hand_value(hand):
	value = 0
	for card in hand:
		if card[0] != "ace":
			value += int(card[0])
		else:
			if value + 11 > 21:
				value += 1
			else:
				value += 11

	return value


# Classes

### Ai Class ###
class Ai:
	
	def __init__(self):
		self.self = self
		self.hand = []
		self.value = 0
		
	def draw_card(self):
		global deck
		
		cardDraw = random.choice(deck)
		self.hand.append(deck[deck.index(cardDraw)])
		deck.pop(deck.index(cardDraw))

		for card in self.hand:
			if str(card[0]) != "ace":
				self.value += int(cardDraw[0])

			elif self.value + 11 > 21:
				self.value += 1

			else:
				self.value += 11

	def dealer_moves(self):
		while self.value <= 17:
			self.draw_card()
			return self.value
		
	def populate_hand(self):
		self.draw_card()
		self.draw_card()

### Game Class ###
class Game():

	def __init__(self):
		self.self = self

	def play(self):
		aiDealer = Ai()
		aiPlayer = Ai()

		aiDealer.populate_hand()
		aiPlayer.populate_hand()

		
		while aiDealer.value <= 21:
			aiDealer.dealer_moves()
			print(aiDealer.hand)
			sleep(1)
	
# Game run
initGame = Game()

initGame.play()