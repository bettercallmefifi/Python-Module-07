from typing import List, Tuple

from ex0 import FlameFactory, AquaFactory
from ex0.factories import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    """
    runs a tournament where every opponent fights all other opponents once.
    opponents: A list of tuples (CreatureFactory, BattleStrategy).
    """
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    # Validate input list: each item must be a
    # (CreatureFactory, BattleStrategy)
    for item in opponents:
        if not isinstance(item, tuple) or len(item) != 2:
            print("Battle error: invalid opponents list - malformed entry")
            return
        factory, strategy = item
        if not isinstance(factory, CreatureFactory) or not isinstance(
            strategy, BattleStrategy
        ):
            # If any entry is malformed or uses an invalid strategy object,
            # abort and do nothing (per requested behavior).
            print("Battle error: invalid opponent types, aborting")
            return

    """iterate through all unique pairs of opponents"""
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            """we instantiate base creatures for the tournament"""
            fighter1 = factory1.create_base()
            fighter2 = factory2.create_base()

            print("\n* Battle *")
            print(fighter1.describe())
            print("  vs.")
            print(fighter2.describe())
            print("  now fight!")

            try:
                """ the strategy defines the sequence """
                """of actions for each creature"""
                strategy1.act(fighter1)
                strategy2.act(fighter2)
            except InvalidStrategyError as e:
                """ if a creature uses a strategy it's """
                """not capable of, abort tournament"""
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    """ 1. instantiating Factories"""
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    """2. instantiating Strategies"""
    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()

    """--- tournament 0 ---"""
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (flame_factory, normal_strat),
        (heal_factory, defensive_strat)
    ])

    """--- tournament 1 ---"""
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (flame_factory, aggressive_strat),
        (heal_factory, defensive_strat)
    ])

    """--- tournament 2 ---"""
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (aqua_factory, normal_strat),
        (heal_factory, defensive_strat),
        (transform_factory, aggressive_strat)
    ])


if __name__ == "__main__":
    main()
