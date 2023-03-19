"""
Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

from typing import Union, Tuple

def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """

    try:
        return int(card)
    except ValueError:
        if card in ('J', 'Q', 'K'):
            return 10
        return 1

def higher_card(card_one: str, card_two: str) -> Union[str, Tuple[str, str]]:
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """

    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)

    if val_one == val_two:
        return card_one, card_two
    return card_one if val_one > val_two else card_two

def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.

    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    val_one = value_of_card(card_one) if card_one != 'A' else 11
    val_two = value_of_card(card_two) if card_two != 'A' else 11

    val_ace = 11 if (val_one + val_two + 11) <= 21 else 1

    return val_ace

def is_blackjack(card_one: str, card_two: str) -> bool:
    """
    Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    cards = {card_one, card_two} & {'10', 'J', 'Q', 'K', 'A'}
    return ('A' in cards) and (len(cards) == 2)

def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    same_val = {'10', 'J', 'Q', 'K'}
    return (len({card_one, card_two} & same_val) == 2) or (card_one == card_two)

def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    cards = ('J', 'Q', 'K')
    val = []
    for c in (card_one, card_two):
        if c in cards:
            val.append(10)
        elif c == 'A':
            val.append(1)
        else:
            val.append(int(c))

    return 9 <= sum(val) <= 11


def can_double_down_w(*cards: str) -> bool:
    """Determine if a blackjack player can place a double down bet.
        :param *cards: str - cards in hand.
        :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    #print(type(cards))
    #print(cards)
    return 8 < sum(value_of_card(c) for c in cards) < 12
