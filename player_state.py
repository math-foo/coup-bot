#!/usr/bin/python
import card


class PlayerState:
  def __init__(self, card1, card2, coins):
    self.card1 = card1
    self.card2 = card2
    self.coins = coins

  def alive(self):
    return self.card1.hidden() or self.card2.hidden()

  def display(self):
    self.card1.display()
    self.card2.display()
    print "And {0} coins".format(self.coins)
