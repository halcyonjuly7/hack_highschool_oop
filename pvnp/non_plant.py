from organism import Organism


class Non_Plant(Organism):
    worth = 20

    def __init__(self):
        super().__init__()
        self._hp = 80
        self._dmg = 5

    def attack(self, plant):
        plant.take_damage(self._dmg)

    def __str__(self):
        return f"NP<hp:{self._hp}, dmg:{self._dmg}>"


