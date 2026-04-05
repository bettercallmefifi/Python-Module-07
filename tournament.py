from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, InvalidStrategyError


def run_tournament(opponents: list) -> None:
    """
    Runs a tournament where every opponent fights all other opponents once.
    opponents: A list of tuples (CreatureFactory, BattleStrategy).
    """
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    # Iterate through all unique pairs of opponents
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            # We instantiate base creatures for the tournament
            fighter1 = factory1.create_base()
            fighter2 = factory2.create_base()

            print("\n* Battle *")
            print(fighter1.describe())
            print("  vs.")
            print(fighter2.describe())
            print("now fight!")

            try:
                # The strategy defines the sequence of actions for each creature
                strategy1.act(fighter1)
                strategy2.act(fighter2)
            except InvalidStrategyError as e:
                # If a creature uses a strategy it's not capable of, abort tournament
                print(f"Battle error, aborting tournament: {e}")
                return


def main():
    # 1. Instantiating Factories
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    # 2. Instantiating Strategies
    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()

    # --- Tournament 0 ---
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    run_tournament([
        (flame_factory, normal_strat),
        (heal_factory, defensive_strat)
    ])

    # --- Tournament 1 ---
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    run_tournament([
        (flame_factory, aggressive_strat),
        (heal_factory, defensive_strat)
    ])

    # --- Tournament 2 ---
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    run_tournament([
        (aqua_factory, normal_strat),
        (heal_factory, defensive_strat),
        (transform_factory, aggressive_strat)
    ])


if __name__ == "__main__":
    main()
