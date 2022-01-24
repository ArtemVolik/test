from service import Service
from models import Hero, Squad


def main():
    shrek = Hero(power=100, name="Shrek", is_good=1)
    cartoon = [
        Hero(power=50, name="Fiona", is_good=1),
        Hero(power=70, name="CatInBoots", is_good=1),
        Hero(power=30, name="Donkey", is_good=1),
        shrek
    ]
    avengers = [
        Hero(power=50, name="Tor", is_good=1),
        Hero(power=60, name="SuperMan", is_good=1),
        Hero(power=40, name="CaptainAmerica", is_good=1),
        shrek
    ]
    squad1 = Squad(name="CartoonTeam")
    squad2 = Squad(name="Avengers")

    Service().join_squad(squad1, cartoon)
    Service().join_squad(squad2, avengers)
    winner = Service().battle(squad1, squad2)
    return winner


if __name__ == "__main__":
    winner_team = main()
    print([(hero._name, hero._health) for hero in winner_team.get_team()])
