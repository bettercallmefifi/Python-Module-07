from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_creatures() -> None:
    """
    tests the creation, description, attack, and heal abilities
    of the healing creature family.
    """
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    """testing base creature"""
    base = factory.create_base()
    print("  base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    """testing evolved creature"""
    evolved = factory.create_evolved()
    print("  evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transforming_creatures() -> None:
    """
    tests the creation, description, attack, and transformation abilities
    of the transforming creature family.
    """
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    """testing base creature"""
    base = factory.create_base()
    print("  base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    """testing evolved creature"""
    evolved = factory.create_evolved()
    print("  evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    test_healing_creatures()
    print()
    test_transforming_creatures()


if __name__ == "__main__":
    main()
