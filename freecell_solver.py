'''
###

 Microsoft Freecell Game Solver

###
'''

import numpy



order_of_magnitude = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
red_suits = ["H", "D"]
black_suits = ["C", "S"]

Heart_foundation = []
Diamond_foundation = []
Club_foundation = []
Spade_foundation = []

free_cells = ["","","",""]

tableau_piles = [
    ["JC", "KH", "8C", "3H", "7C", "9S", "9H"],
    ["TD", "AH", "3C", "4C", "6H", "KD", "TH"],
    ["3S", "6D", "JD", "6C", "7H", "2H", "AC"],
    ["7S", "QH", "5C", "7D", "AS", "5H", "2D"],
    ["4S", "AD", "TC", "5D", "KC", "QD"],
    ["8D", "8S", "KS", "QS", "9C", "2S"],
    ["2C", "4H", "4D", "JH", "QC", "9D"],
    ["6S", "JS", "3D", "5S", "8H", "TS"]
]

def move_card(from_pile, to_pile):
    tmp = from_pile.pop()
    to_pile.append(tmp)

def get_facecard(card):
    return card[0]

def get_suit(card):
    return card[1]

def are_cards_different_colors(card1, card2):
    suit1 = get_suit(card1)
    suit2 = get_suit(card2)

    if (suit1 in red_suits and suit2 in red_suits) or (suit1 in black_suits and suit2 in black_suits):
        return False
    else:
        return True

###  Check if difference between cards is one (and from_pile < to_pile) and not the same suit
###  also take into account empty decks (in decks or freecells)?
def is_valid_move(from_pile, to_pile):
    from_card = from_pile[-1]
    to_card = to_pile[-1]
    return False


def is_victory_condition():
    if Heart_foundation[-1] == "KH" and Diamond_foundation[-1] == "KD" and \
       Club_foundation[-1] == "KC" and Spade_foundation[-1] == "KS" :
        return True
    else:
        return False

def solve_freecell():
    if is_victory_condition():
        return True

    # Go through all the tableau piles for a valid move

    # forwards


    # backwards

    # Go through all the free cells for a valid move
    # Move cards from free cell to tableau pile:
    for free_cell in free_cells:
        if free_cell = "" :
            for tableau_pile in tableau_piles:
                if is_valid_move(free_cell, tableau_pile):
                    # ****** SPECIAL CASE:  MOVE FREE CELLS **********
                    #move_card(free_cell, tableau_pile)

                    if solve_freecell():
                        return True
                    
                    # If we've gotten to this point, there was no solution for this chain
                    # undo the move
                    #move_card(tableau_pile, free_cell)
    
    # Move cards from tableau pile to free cell:

    return False


def print_solution():
    print()

if __name__ == "__main__":
    if solve_freecell():
        print_solution()
    else:
        print("Freecell puzzle not solvable.")