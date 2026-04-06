from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """custom exception raised when a strategy """
    """is applied to an incompatible creature."""
    pass


class BattleStrategy(ABC):
    """
    abstract strategy class defining how a creature should act in a tournament.
    """
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """returns True if the creature is compatible with this strategy."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """executes the strategy's actions."""
        pass


class NormalStrategy(BattleStrategy):
    """normal strategy: simply attacks."""
    def is_valid(self, creature: Creature) -> bool:
        """Suitable for any Creature"""
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
                )

        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """aggressive strategy: transforms, attacks, then reverts."""
    def is_valid(self, creature: Creature) -> bool:
        """only suitable for creatures with TransformCapability"""
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
                )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    """defensive strategy: attacks, then heals."""
    def is_valid(self, creature: Creature) -> bool:
        """Only suitable for creatures with HealCapability"""
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
                )
        print(creature.attack())
        print(creature.heal())
