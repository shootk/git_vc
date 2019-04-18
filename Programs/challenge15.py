#challenge15

from random import shuffle

class Card:
    suits = ("spades","hearts","diamonds","clubs")
    values = (None,None,"2","3","4","5","6","7","8","9",
              "10","Jack","Queen","King","Ace")

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __lt__(self,ano_c):
        if self.value < ano_c.value:
            return True
        else:
            if self.value == ano_c.value:
                return self.suit < ano_c.suit
        return False

    def __gt__(self,ano_c):
        if self.value > ano_c.value:
            return True
        else:
            if self.value == ano_c.value:
                return self.suit > ano_c.suit
            return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
           + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(j,i))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.name = name
        self.card = None
        self.wins = 0

class Game:
    def __init__(self):
        name1 = input("Please input Player1's name:")
        name2 = input("Please input Player2's name:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        w = "This round {} win".format(winner)
        print(w)

    def draw(self,p1,p2):
        d = "{} draw {},{} draw {}."
        print(d.format(
            p1.name,p1.card,p2.name,p2.card))

    def print_winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1
        elif p1.wins < p2.wins:
            return p2
        else:
            return None

    def play_game(self):
        cards = self.deck.cards
        print("Start playing 'War Game'.")
        while len(cards) >=2:
            m = "'q' is end , anoser key is play :"
            response = input(m)
            if response == "q":
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()

            self.draw(self.p1,self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        w = self.print_winner(self.p1,self.p2)
        if w != None:
            print("War Game won by {}.".format(w.name))
        else:
            print("Draw")

g = Game()
g.play_game()
