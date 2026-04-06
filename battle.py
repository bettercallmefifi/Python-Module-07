from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    """
    verifies that a factory can create its base and evolved creatures,
    describe them, and make them attack.
    """
    print("Testing factory")

    """creation and testing of the base creature"""
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    """creation and testing of the evolution"""
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def testing_battle(
        factory1: CreatureFactory, factory2: CreatureFactory
        ) -> None:
    """
    makes two base creatures from two different factories fight.
    """
    print("Testing battle")

    """creation of the fighters"""
    fighter1 = factory1.create_base()
    fighter2 = factory2.create_base()

    """presentation"""
    print(fighter1.describe())
    print("  vs.")
    print(fighter2.describe())
    print("  fight!")

    """ attack """
    print(fighter1.attack())
    print(fighter2.attack())


def main() -> None:
    """
    instantiation of the factories (the only direct contact point allowed)
    """
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    """running the tests required by the subject"""
    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    testing_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
