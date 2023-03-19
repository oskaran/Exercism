#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:44:11 2022

@author: oskar
"""

from operator import eq
from typing import Union

def value_of_card(card: str, ace_val: int = 1) -> int:

    """Determine the scoring value of a card.
    :param card: str - given card.
    :return: int - value of a given card (J, Q, K = 10, 'A' = 1) numerical value otherwise.
    """

    if card in "JQK":
        return 10
    if card == "A":
        return ace_val
    return int(card)

def higher_card(card1: str, card2: str) -> Union[str, tuple[str, str]]:

    """Determine which card has a higher value in the hand.
    :param card1, card2: str - cards dealt.  J, Q, K = 10, 'A' = 1, all others are numerical value.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    if value_of_card(card1) > value_of_card(card2):
        return card1
    if value_of_card(card1) < value_of_card(card2):
        return card2
    return card1, card2

def value_of_ace(*cards: str) -> int:
    """Calculate the most advantageous value for the ace card.
        :param *cards: str - cards in hand.
        :return: int - value of the upcoming ace card (either 1 or 11).
    """
    return 1 if sum(value_of_card(c, ace_val=11) for c in cards) >= 11 else 11

def is_blackjack(*cards: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.
        :param *cards: str - cards in hand.
        :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    return sum(value_of_card(c, ace_val=11) for c in cards) == 21

def can_split_pairs(*cards: str) -> bool:
    """Determine if a player can split their hand into two hands.
        :param *cards: str - cards in hand.
        :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """

    return eq(*(value_of_card(c) for c in cards))

def can_double_down(*cards: str) -> bool:
    """Determine if a blackjack player can place a double down bet.
        :param *cards: str - cards in hand.
        :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """

    return 8 < sum(value_of_card(c) for c in cards) < 12
