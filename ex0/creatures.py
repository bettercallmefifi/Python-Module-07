from abc import ABC, abstractmethod


class Creature(ABC):
    """
    abstract class representing a base creature.
    """
    def __init__(self, name: str, creature_type: str):
        self.name = name
        self.type = creature_type

    @abstractmethod
    def attack(self) -> str:
        """abstract method for the attack."""
        pass

    def describe(self) -> str:
        """concrete generic method for description."""
        return f"{self.name} is a {self.type} type Creature"


"""fire family"""


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


"""water family"""


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
