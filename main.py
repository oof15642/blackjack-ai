# Imports
import random
from time import sleep

# Variables
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10", "ace"]

deck = [[rank, suit] for suit in suits for rank in ranks]

# Functions
def hand_value(hand):
	valueTemp = 0
	for card in hand:
		if card[0] != "ace":
			valueTemp += int(card[0])
		else:
			if valueTemp + 11 > 21:
				valueTemp += 1
			else:
				valueTemp += 11

	return valueTemp


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

		aiDealer.value = hand_value(aiDealer.hand)
		
		
		hand_value(aiPlayer.hand)
		
		while aiDealer.value <= 21:
			aiDealer.dealer_moves()
			aiDealer.value = hand_value(aiDealer.hand)
			print(aiDealer.value)
			print(aiDealer.hand)
			sleep(1)
	
# Game run
initGame = Game()

initGame.play()