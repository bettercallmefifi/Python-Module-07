from abc import ABC, abstractmethod


class HealCapability(ABC):
    """
    Abstract class defining the healing capability.
    """
    @abstractmethod
    def heal(self) -> str:
        """Abstract method to heal."""
        pass


class TransformCapability(ABC):
    """
    Abstract class defining the transformation capability.
    It includes a state attribute to keep track of the transformation.
    """
    def __init__(self):
        # Attribute to make the state persistent
        self.is_transformed = False

    @abstractmethod
    def transform(self) -> str:
        """Abstract method to transform the creature."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Abstract method to revert the transformation."""
        pass
