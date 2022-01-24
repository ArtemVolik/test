from random import shuffle, uniform
from models import Squad, Hero
from typing import Set, List


class Service:

    @staticmethod
    def join_squad(squad: Squad, heroesList: List[Hero]):
        for hero in heroesList:
            hero.add_to_team(squad)
            squad.add_to_team(hero)

    @staticmethod
    def leave_squad(squadlist: Set[Squad], hero: Hero):
        for squad in squadlist:
            hero.drop(squad)
            squad.drop(hero)

    @staticmethod
    def battle(squad1, squad2):
        Service._remove_duplicated(squad1, squad2)
        squads = [squad1, squad2]
        shuffle(squads)
        squad1, squad2 = squads
        while squad1.total_health() and squad2.total_health():
            probability = uniform(0.5, 1)
            total_damage = int(squad1.total_power() * probability)
            squad2.get_damage(total_damage)
            squad1, squad2 = squad2, squad1
        return squad2

    @staticmethod
    def _remove_duplicated(squad1, squad2):
        duplicates = [hero for hero in squad1.get_team() if hero in squad2.get_team()]
        for hero in duplicates:
            Service.leave_squad([squad1, squad2], hero)

