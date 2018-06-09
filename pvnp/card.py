class Card:
    cost = 5

    def __init__(self, power):
        self._power = power

    @property
    def power(self):
        return self._power

