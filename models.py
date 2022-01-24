from common import VerifiedField, Base, Team, ServiceFunctionality
import random

INITIAL = 100


class Squad(ServiceFunctionality):
    """Squad class aggregates Heroes"""
    _name = VerifiedField(value_class=str, size=3)
    _team = Team(value_class=ServiceFunctionality)

    def __init__(self, name):
        self._name = name
        self._team = set()

    @property
    def is_good(self):
        return all([hero._is_good for hero in self._team])

    def total_health(self):
        return sum([hero.get_health for hero in self._team])

    def total_power(self):
        return sum([hero.get_power for hero in self._team if hero.is_alive])

    def get_damage(self, damage):
        """Divide demage randomly between team members"""
        active_team = [hero for hero in self._team if hero.is_alive]
        idx = 0
        while damage and self.squad_alive:
            damage_per_one = random.randint(0, damage)
            if active_team[idx].is_alive:
                damage -= damage_per_one
                active_team[idx].reduce_health(damage_per_one)
            idx = (idx + 1) % len(active_team)

    @property
    def squad_alive(self):
        return bool([hero.is_alive for hero in self._team])

    def get_team(self):
        return self._team


class Hero(ServiceFunctionality):
    """Main character class"""
    _power = VerifiedField(value_class=int, minimum_value=1, maximum_value=INITIAL)
    _health = VerifiedField(value_class=int, minimum_value=0, maximum_value=INITIAL)
    _name = VerifiedField(value_class=str, size=3)
    _is_good = VerifiedField(value_class=int, tiny_int=1)
    _team = Team(value_class=Base)

    def __init__(self, name, power, is_good=1):
        self._health = INITIAL
        self._name = name
        self._is_good = is_good
        self._power = power
        self._team = set()

    def __repr__(self):
        return self._name

    @property
    def is_alive(self):
        return bool(self._health)

    @property
    def is_good(self):
        return bool(self._is_good)

    def reduce_health(self, value):
        self._health = max(0, self._health - value)

    @property
    def get_power(self):
        return self._power

    @property
    def get_health(self):
        return self._health





