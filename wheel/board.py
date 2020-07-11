"""Board class for Wheel of Fortune game."""

class Board:
    """Board for Wheel of Fortune with attributes board and guessed.
    Attributes:
       board - list of correct characters or "_" in the secret word
       guessed - list of characters guessed so far

    >>> from secret import SecretWord
    >>> b = Board(SecretWord("bookkeeper"))
    >>> len(b)
    10
    >>> b.guess('o')
    2
    >>> b
    < _ o o _ _ _ _ _ _ _ : o >
    >>> b.done()
    False
    >>> b.guess('k')
    2
    >>> b
    < _ o o k k _ _ _ _ _ : o,k >
    >>> b.guess('j')
    0
    >>> b
    < _ o o k k _ _ _ _ _ : o,k,j >
    >>> b.word()
    ['_', 'o', 'o', 'k', 'k', '_', '_', '_', '_', '_']
    >>> b.guesses()
    ['o', 'k', 'j']
    """
    def __init__(self, secret):
        """Create an initial board with no guesses and a secret."""
        # BEGIN
        self.secret = secret
        self.guessed = []
        self.hit = []
        self.missed = []
        self.winner = False
        count = 0
        self.board_rep = []
        for j in range(len(self.secret)):
            self.board_rep.append('_')
        # END

    max_miss = 11

    def __repr__(self):
        return '< ' + " ".join(self.word()) + " : " + ",".join(self.guesses()) + ' >'

    def __len__(self):
        return self.word_len()

    def word_len(self):
        """Return the length of the secret word."""
        # BEGIN
        return len(self.secret)
        # END

    def word(self):
        """Return the current state of guessing the word as a lsit of characters.
        Unguessed positions are represented by '_'
        Guessed positions hold the character.
        """
        # BEGIN
        # if len(self.guessed) == 0:
        #     return self.board_rep

        return self.board_rep
        # END

    def guesses(self):
        """Return a list of the characters guessed so far."""
        # BEGIN
        return self.guessed
        # END

    def hits(self):
        """Return a list of characters correctly guessed."""
        # BEGIN
        return self.hit
        # END

    def misses(self):
        """Return a list of characters incorrectly guessed."""
        # BEGIN
        return self.missed
        # END

    def guess(self, char):
        """Update the board to reflect the guess of char.
        Return the number of indices in the secret word where char occurs.
        If char does not appear in the word, this will be 0.
        """
        # BEGIN
        # if char in self.guessed:
        #     return "Already Guessed"
        listindex = self.secret.match(char)
        if len(self.misses()) < self.max_miss:
            if len(listindex) > 0:
                self.hit.append(char)
                for i in listindex:
                    self.board_rep[i] = char
            else:
                self.missed.append(char)
            self.guessed.append(char)
            return len(listindex)
        else:
            return "No More Guesses."
        # END

    def done(self):
        """Determine if the game is done."""
        # BEGIN
        for i in self.board_rep:
            if i == '_':
                self.winner = False
        if '_' not in self.board_rep:
            self.winner = True
        return self.winner
        # END


    # def miss_man(missed):
    #     missed = min(missed, Board.max_miss)
    #     return "assets/man{0}.txt".format(missed)

    def display(self):
        missed = len(self.misses())
        # path = Board.miss_man(missed)
        # with open(path) as fp:
        #     symbol = fp.read()
        # print(symbol)
        print(self.word())
        print("Guessed chars: ", self.guesses())
