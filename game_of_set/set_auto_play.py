import itertools
import random

class Set(object):

    def __init__(self):

        self.colors = ["red", "green", "purple"]
        self.shapes = ["diamond", "squiggle", "oval"]
        self.shadings = ["solid", "outlined", "striped"]
        self.numbers = ["one", "two", "three"]

        deck = []

        for color in self.colors:
            for shape in self.shapes:
                for shading in self.shadings:
                    for number in self.numbers:
                        card = {}
                        card["color"] = color
                        card["shape"] = shape
                        card["shading"] = shading
                        card["number"] = number

                        deck.append(card)

        random.shuffle(deck)

        self.deck = deck
        self.board = []
        self.sets = []

    def deal(self, cards=12):

        out = []
        for _ in range(cards):
            out.append(self.deck.pop())

        return out

    def play(self):

        print("Dealing 12 cards onto the board.")
        self.board = self.deal(12)

        while len(self.deck) > 0:
            self.sets += self.find_sets(self.board)
            self.board += self.deal(3)

        # Find the very last set(s).
        self.sets += self.find_sets(self.board)

        return (len(self.sets), self.sets)

    @staticmethod
    def display_cards(cards):

        print(["Number", "Color", "Shape", "Shading"])
        for card in cards:
            print([card["number"], card["color"], card["shape"], card["shading"]])

    @staticmethod
    def find_sets(board):
       
        sets = []

        # Calculate all the ways to combine current board into 3 card trios
        combinations = itertools.combinations(range(len(board)), 3)
        combination = next(combinations, False)

        while combination:

            if Set.is_a_set(board[combination[0]], board[combination[1]], board[combination[2]]) is True:

                sets.append([board[combination[0]], board[combination[1]], board[combination[2]]])
                del board[combination[2]]
                del board[combination[1]]
                del board[combination[0]]

                # re-calculate the possible combos of card trios on updated board
                combinations = itertools.combinations(range(len(board)), 3)
                combination = next(combinations, False)
                continue

            else:
                # Move to next combo without updating the board/removing cards
                combination = next(combinations, False)
                continue

        return sets

    @staticmethod
    def is_a_set(card1, card2, card3):

        for attribute in ["color", "shape", "shading", "number"]:
            if (Set.all_unique([
                    card1[attribute],
                    card2[attribute],
                    card3[attribute],
                ]) is False and Set.all_same([
                    card1[attribute],
                    card2[attribute],
                    card3[attribute],
                ]) is False):

                return False

        return True

    @staticmethod
    def all_unique(arr):
        return len(set(arr)) == len(arr)

    @staticmethod
    def all_same(arr):
        return len(set(arr)) == 1

# ------------------------------------------------------------------------------

def main():
    game = Set()
    discovered, sets = game.play()
    print("You discovered {} set(s).".format(discovered))
    for i, subset in enumerate(sets):
        print("Set #{index}".format(index=(i + 1)))
        Set.display_cards(subset)


if __name__ == "__main__":
    main()