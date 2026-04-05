from .factories import CreatureFactory, FlameFactory, AquaFactory

# We only expose the factories, hiding the direct implementation
# of concrete creatures from the package user.
__all__ = ["CreatureFactory", "FlameFactory", "AquaFactory"]
