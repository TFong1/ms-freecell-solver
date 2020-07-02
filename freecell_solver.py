'''
###

 Microsoft Freecell Game Solver

###
'''


order_of_magnitude = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
red_suits = ["H", "D"]
black_suits = ["C", "S"]

Heart_deck = []
Diamond_deck = []
Club_deck = []
Spade_deck = []

decks = [
    ["JC", "KH", "8C", "3H", "7C", "9S", "9H"],
    ["TD", "AH", "3C", "4C", "6H", "KD", "TH"],
    ["3S", "6D", "JD", "6C", "7H", "2H", "AC"],
    ["7S", "QH", "5C", "7D", "AS", "5H", "2D"],
    ["4S", "AD", "TC", "5D", "KC", "QD"],
    ["8D", "8S", "KS", "QS", "9C", "2S"],
    ["2C", "4H", "4D", "JH", "QC", "9D"],
    ["6S", "JS", "3D", "5S", "8H", "TS"]
]

def move_card(from_deck, to_deck):
    tmp = from_deck.pop()
    to_deck.append(tmp)

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

###  Check if difference between cards is one (and from_deck < to_deck) and not the same suit
###  also take into account empty decks (in decks or freecells)?
def is_valid_move(from_deck, to_deck):
    from_card = from_deck[-1]
    to_card = to_deck[-1]
    return


