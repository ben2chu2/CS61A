from secret import SecretWord
from board import Board

class Game:
    """Run an entire game.

    Initialization defines the player who pickers secret word and one or more guessers.
    play
       - picker picks the secret word from the dictionary held by all players
       - guessers guess in turn looking at the state of the board until the game is done
       - each guesser continues as long as they guess currect letters
       - returns final board
    winner returns the player who picked the last letter.

    >>> from wordset import Dictionary
    >>> from player import Player, DummyPlayer
    >>> p = Player(Dictionary("assets/lincoln.txt"))
    >>> game = Game(DummyPlayer("pick"), [ DummyPlayer("guess") ] )
    >>> board = game.play(False)
    >>> board.word()
    ['s', 'c', 'o', 'r', 'e']
    >>> len(board.guesses())
    6
    """
    def __init__(self, picker, guessers):
        # BEGIN
        self.brd = Board(SecretWord(picker.pick_word()))
        self.pick = picker
        self.guesser = guessers[0]
        self.wins = False
        # END

    def play(self, verbose=True):
        # BEGIN
        for i in range(11):
            if self.brd.done():
                break
            if '_' not in self.brd.board_rep:
                self.wins = True
                break
            # char = [c for c in self.guesser.guess(self.brd)]
            self.brd.guess(self.guesser.guess(self.brd))
        return self.brd
        # END

    def winner(self):
        # BEGIN
        return self.wins
        # END
