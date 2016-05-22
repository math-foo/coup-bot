#!/usr/bin/python

class Card:
  def __init__(self, influence_type):
    self.influence_type = influence_type
    self.hidden = True

  def reveal(self):
    self.hidden = False

  def hidden(self):
    return self.hidden

  def display(self):
    if self.hidden:
      print "{0} (hidden)".format(self.influence_type)
    else:
      print "{0} (visible)".format(self.influence_type)
