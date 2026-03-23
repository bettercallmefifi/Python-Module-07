from abc import ABC, abstractmethod

# 'Card' is an abstract class that defines the skeleton of behavior
# shared by all card types.
# It contains:
# **Two methods with concrete (implemented) behavior
# **One abstract method 'play' that must be implemented in subclasses
# This design is called the Template Method pattern; it allows card
# types to customize their way of playing.
# This pattern can also control the order of operations while giving
# flexibility.
# To clarify, mana in card games is a resource required to play a card.
# We will see how to use it in the play implementation.


class Card(ABC):
    # Parameterized constructor:
    # name: the name of the card (e.g., "Fire Dragon")
    # cost: how much mana is needed to play this card (e.g., 5 mana)
    # rarity: a string flag used to describe card rarity
    #         (e.g., "common", "rare", "legendary")
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    # Abstract method: must be implemented by all subclasses
    # Each card type (Creature, Spell, Artifact) plays differently
    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    # Gives child classes the name, cost, rarity, and type.
    # They can add their specific data by overriding this function.
    # Returns a dictionary with basic card information
    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__,  # Dynamic type name
        }

    # Before playing, we should always validate that cost <= available_mana
    def is_playable(self, available_mana: int) -> bool:
        return self.cost <= available_mana

    # This function is similar to the toString method.
    # We override it so that printing the object (even inside a list)
    # shows a readable representation.
    def __repr__(self):
        return f"{self.name} ({self.cost})"
