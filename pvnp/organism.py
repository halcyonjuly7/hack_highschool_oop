class Organism:
    def __init__(self):
        self._hp = 35
        self._dmg = 10

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def dmg(self):
        return self._dmg

    def take_damage(self, damage):
        self._hp -= damage


