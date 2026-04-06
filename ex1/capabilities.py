from abc import ABC, abstractmethod


class HealCapability(ABC):
    """
    abstract class defining the healing capability.
    """
    @abstractmethod
    def heal(self) -> str:
        """abstract method to heal."""
        pass


class TransformCapability(ABC):
    """
    abstract class defining the transformation capability.
    it includes a state attribute to keep track of the transformation.
    """
    def __init__(self):
        """attribute to make the state persistent"""
        self.is_transformed = False

    @abstractmethod
    def transform(self) -> str:
        """abstract method to transform the creature."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """abstract method to revert the transformation."""
        pass
