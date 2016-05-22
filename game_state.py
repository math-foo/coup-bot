#!/usr/bin/python
import deck_state
import player_state


class GameState(object):
  def __init__(self, num_of_players):
    if num_of_players == 3:
      self.deck = deck_state.DeckState(2)
    else:
      self.deck = deck_state.DeckState(3)
    self.players = {}

    for x in xrange(1,num_of_players+1):
      player_name = "Player{0}".format(x)
      card1 = self.deck.draw()
      card2 = self.deck.draw()
      self.players[player_name] = player_state.PlayerState(card1, card2, 2)

  def display(self):
    self.deck.display()

    for player in self.players.keys():
      player_state = self.players[player]

      print "{0} has:".format(player)
      player_state.display()
