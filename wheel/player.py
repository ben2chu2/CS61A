"""Player classes for Wheel of Fortune game."""

from wordset import WordMunch
from utils import *
from heapq import nlargest
import random

class Player:
    """Player base class.  Defines initializer and interface.

    >>> from wordset import Dictionary
    >>> p = Player(Dictionary('assets/lincoln.txt'))
    >>> Player.all_words[2]
    'add'
    """
    all_words = None

    def __init__(self, dictionary):
        """Inialize class with a dictionary."""
        # BEGIN
        Player.all_words = []
        for i in dictionary.words():
            Player.all_words.append(i)
        # END

    def guess(self, board):
        """Return a character a a guess."""
        return None

    def pick_word(self):
        """Return a word that is to be guessed."""
        return None

class DummyPlayer(Player):
    """Simple deterministic player for testing."""

    def __init__(self, name):
        self.name = name
        self.calls = -1

    def guess(self, board):
        """Return a character a a guess."""
        self.calls += 1
        return "cfeors"[self.calls]

    def pick_word(self):
        """Return a word that is to be guessed."""
        return 'score'


class HumanPlayer(Player):
    """HumanPlayer is initialized with a name and implements the player interface
    such that:
    - guess requests a guess from a person, via the input device
    - pick_word requests a secret word and verifies that it is in the dictionary

    """
    def __init__(self, name):
        self.name = name

    def guess(self, board):
        """Guess a character."""
        print(board.word())
        print("Guessed chars: ", board.guessed)
        print(self.name, ", please enter your next guess.")
        guess = input()
        while (len(guess) != 1) or (guess in board.guesses()):
            print('Please enter a single character not yet guessed')
            guess = input()
        return guess

    def pick_word(self):
        """Return a secret word from the dictionary."""

        print(self.name,", pick your secret word.")
        word = input()
        while not word in Player.all_words:
            print(word, " is not in the dictionary. Another:")
            word = input()
        return word

class ComputerPlayer(Player):
    """Perform as a player - picking a word or guessing a character

    >>> from wordset import WordSet    # Basic test including total character frequency
    >>> from board import Board
    >>> from secret import SecretWord
    >>> p = Player(WordSet(['one','two','three']))   # Player superclass with the dictionary
    >>> c = ComputerPlayer()
    >>> b = Board(SecretWord('three'))
    >>> c.guess(b)
    'e'
    """
    def __init__(self, name='Computer'):
        # BEGIN
        self.name = name
        # END
    def len_predicate(self, word):
        if len(word) == self.wordlen:
            return True
        else:
            return False

    def wordfilt(self, word):
        lindex = self.board.secret.match(self.max)
        if len(word) == self.wordlen:
            for i in lindex:
                if word[i] != self.max:
                    return False
            return True
        else:
            return False

    def guess(self, board, verbose=False):
        """Guess a character to play based on the current board.
        verbose option allows useful and fun displays.
        """
        # BEGIN
        self.board = board
        self.wordlen = len(board.board_rep)
        if len(board.guessed) == 0:
            self.k = WordMunch(Player.all_words).filter(self.len_predicate)
            diction = WordMunch(Player.all_words).frequency()
            max = nlargest(26, diction, key=diction.get)
            for i in max:
                if i not in board.guessed:
                    self.max = i
                    """ use for printing state of the board (will fail tests though)"""
                    # print(board.word())
                    # print("Guessed chars:" , board.guessed)
                    # print(len(self.k), "possible words.")
                    # print("Computer guesses: ", i)
                    return i
        else:
            self.k = WordMunch(self.k).filter(self.wordfilt)
            diction = WordMunch(self.k).frequency()
            max = nlargest(26, diction, key=diction.get)
            for i in max:
                if i not in board.guessed:
                    self.max = i
                    print(board.word())
                    print("Guessed chars:" , board.guessed)
                    print(len(self.k), "possible words.")
                    print("Computer guesses: ", i)
                    return i
        # END


    def pick_word(self):
        """Pick a random word from the dictionary."""
        # BEGIN
        # return random.choice(Player.all_words)
        return random.sample(Player.all_words, 1)[0]
        # END
