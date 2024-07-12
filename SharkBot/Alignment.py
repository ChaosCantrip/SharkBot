from typing import Self

import discord


class Alignment:

    def __init__(self, id: str, name: str, colour: discord.Colour):
        self._id: str = id
        self._name: str = name
        self._colour: discord.Colour = colour
        self._weak_to: list[Self] = []
        self._strong_against: list[Self] = []

    # ===== Properties =====

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def colour(self) -> discord.Colour:
        return self._colour

    # ===== Weaknesses and Strengths =====

    def add_weak_to(self, alignment: Self):
        self._weak_to.append(alignment)

    def add_strong_against(self, alignment: Self):
        self._strong_against.append(alignment)

    def is_weak_to(self, alignment: Self) -> bool:
        return alignment in self._weak_to

    def is_strong_against(self, alignment: Self) -> bool:
        return alignment in self._strong_against


NEUTRAL = Alignment("neutral", "Neutral", discord.Colour.greyple())
RED = Alignment("red", "Red", discord.Colour.red())
YELLOW = Alignment("yellow", "Yellow", discord.Colour.gold())
PURPLE = Alignment("purple", "Purple", discord.Colour.purple())
GREEN = Alignment("green", "Green", discord.Colour.green())
BLUE = Alignment("blue", "Blue", discord.Colour.blue())

RED.add_weak_to(BLUE)
RED.add_strong_against(YELLOW)
YELLOW.add_weak_to(RED)
YELLOW.add_strong_against(PURPLE)
PURPLE.add_weak_to(YELLOW)
PURPLE.add_strong_against(GREEN)
GREEN.add_weak_to(PURPLE)
GREEN.add_strong_against(BLUE)
BLUE.add_weak_to(GREEN)
BLUE.add_strong_against(RED)