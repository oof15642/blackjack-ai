# Imports
import random
from time import sleep

# Variables
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10", "ace"]

deck = [[rank, suit] for suit in suits for rank in ranks]

gameContinue = True

# change these to costomize game
hitOn17 = False
moneyAmount = 10_000
initialBet = 10
pot = 0

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

	def bet(self):
		print(f"player bets ${initialBet}")
		pot += initialBet

	def dealer_moves(self):
		if self.value <= 17:
			self.draw_card()
		return self.value
		
	def player_moves(self, dealerHand):
		global gameContinue
		global hitOn17

		showingCard = dealerHand[0][0] # dealers first card that is showing to the player

		if self.value == 21:
			print("player has blackjack")
			gameContinue = False

		if self.value == 17 and hitOn17:
			self.draw_card()

		if self.value > 17:
			print("player stands")
			gameContinue = False

		elif self.value == 17 and hitOn17 == False:
			print("player stands")
			gameContinue = False

		elif self.value <= 16 and showingCard + 10 >= 17:
			self.draw_card()

		



	def populate_hand(self):
		self.draw_card()
		self.draw_card()

		

### Game Class ###
class Game():

	def __init__(self):
		self.self = self

	def play(self):
		global gameContinue

		aiDealer = Ai()
		aiPlayer = Ai()
		
		aiDealer.populate_hand()
		aiPlayer.populate_hand()

		aiDealer.value = hand_value(aiDealer.hand)
		aiPlayer.value = hand_value(aiPlayer.hand)

		if aiDealer.value == 21 or aiPlayer.value == 21:
			print()
		
		while aiPlayer.value < 21 and gameContinue:
			print(gameContinue)
			print(aiDealer.hand)

			print(aiPlayer.value)
			print(aiPlayer.hand)
			sleep(1)
			aiPlayer.dealer_moves()
			aiPlayer.value = hand_value(aiPlayer.hand)

		
		#while aiDealer.value <= 21:
		#	print(aiDealer.value)
		#	print(aiDealer.hand)
		#	sleep(1)
		#	aiDealer.dealer_moves()
		#	aiDealer.value = hand_value(aiDealer.hand)
			
	
# Game run
initGame = Game()

initGame.play()