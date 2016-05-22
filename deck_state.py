#!/usr/bin/python
import card
import random

class DeckState:
  CARD_TYPES = ['Countessa', 'Assassin', 'Captain', 'Duke', 'Ambassador']

  def __init__(self, copies):
    self.cards = []

    for card_type in self.CARD_TYPES:
      for i in xrange(0,copies):
        self.cards.append(card.Card(card_type))

    random.shuffle(self.cards)

  def draw(self):
    new_card = self.cards.pop()
    return new_card

  def replace_and_shuffle(self, card):
    self.cards.append(card)
    random.shuffle(self.cards)

  def display(self):
    print "In the deck there are {0} cards".format(len(self.cards))
    for card in self.cards:
      card.display()
