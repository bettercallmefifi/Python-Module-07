from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """
    abstract factory to create creatures of the same family.
    """
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    """concrete factory for the Fire family."""
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """concrete factory for the Water family."""
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
