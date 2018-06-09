from organisnm import Organism

class Plant(Organism):
    cost = 35
    def __init__(self, power_up=0):
        super().__init__()
        self._power_up = power_up

    @property
    def powerup(self):
        return self._power_up
    
    def attack(self,nonplant):
        nonplant.take_damage(self.dmg + self._power_up)


    def apply_powerup(self, card):
        self._power_up += card.power


    def weaken_powerup(self):
        self._power_up //= 2


