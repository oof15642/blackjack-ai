# Imports
import random

# Variables
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "ace"]

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
class ais:
    
    def __init__(self):
        self.self = self
        self.handOne = []
        self.handTwo = []
        self.valueOne = 0
        self.valueTwo = 0
        
    def draw_card(self, handDrawTo):
        global deck
        
        cardDraw = random.choice(deck)
        handDrawTo.append(deck[deck.index(cardDraw)])
        deck.pop(deck.index(cardDraw))
        
        if handDrawTo[0] == "ace" and self.handDrawTo:
            
        
    def populate_hands(self):
        draw_card(self.handOne)
        draw_card(self.handOne)
        
        draw_card(self.handTwo)
        draw_card(self.handTwo)
        
        
        
    def player_move_one(self):
        
    
    
  def make_move(self, handValue):
    if handValue < 17:
      print("Dealer hits")
      cardDrawThree = random.choice(deck)
      self.hand.append(deck[deck.index(cardDrawThree)])
      deck.pop(deck.index(cardDrawThree))

class aiTwoClass:
  def __init__(self):
    self.self = self
    self.hand = []

  def draw(self):
    cardDrawOne = random.choice(deck)
    self.hand.append(deck[deck.index(cardDrawOne)])
    deck.pop(deck.index(cardDrawOne))

    cardDrawTwo = random.choice(deck)
    self.hand.append(deck[deck.index(cardDrawTwo)])
    deck.pop(deck.index(cardDrawOne))

  def make_move_one(self, handValue, aiOneHand):
    

    

class Game():

  def __init__(self, aiOne, aiTwo):
    self.self = self
    self.aiOne = aiOne
    self.aiTwo = aiTwo

  def play(self):
    self.aiOne.draw()
    self.aiTwo.draw()

    self.aiOneValue = hand_value(self.aiOne.hand)
    self.aiTwoValue = hand_value(self.aiTwo.hand)

    if self.aiOneValue != 21:
      print("The dealer has a hand of " + str(self.aiOneValue))
      print("You have a hand of " + str(self.aiTwoValue))

      if self.aiOneValue > self.aiTwoValue:
      

    else:
      print("AI One Wins!")
      exit()
      

    
# Game run
