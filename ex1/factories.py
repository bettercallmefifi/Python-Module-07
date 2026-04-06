from ex0.factories import CreatureFactory
from ex0.creatures import Creature
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    """
    concrete factory for the healing creatures family.
    """
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """
    concrete factory for the transforming creatures family.
    """
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
