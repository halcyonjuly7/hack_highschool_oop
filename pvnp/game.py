from linked_list import LinkedList
from _queue import _Queue
from stack import Stack
from wave import Wave
from non_plant import NonPlant
from plant import Plant
from card import Card
import random




"""
notes:

Searches for the first nonplant infront of the plant and attacks it.
does in front mean 1 square of the within the same row of the plant?

"""

class Game:
    def __init__(self, file):
        with open(file, "r") as f:
            self.cash, self.height, self.width = [int(x) for x in f.readline().split(" ")]
            self.waves = LinkedList()
            self.waves_num = 0
            for line in f:
                self.waves.add(Wave(*[int(x) for x in line.split(" ")]))
                self.waves_num += 1

        self._board = [[_Queue()for __ in range(self.width)]for _ in range(self.height)]
        self.game_over = False
        self._turn = 0
        self.non_plants = 0
        self._power_ups = Game._init_powerups()


    @staticmethod
    def _init_powerups():
        stack = Stack()
        nums = [1, 2, 3, 4, 5]
        for _ in range(100):
            stack.push(Card(random.choice(nums)))
        return stack

    def draw(self):
        # def draw(self):
        print("Cash: $", self.cash, "\nWaves: ", self.waves_num, sep='')
        s = '  '.join([str(i) for i in range(self.width - 1)])
        print('  ', s)
        for row in range(self.height):
            s = []
            for col in range(self.width):
                if self.is_plant(row, col):
                    char = 'P'
                elif self.is_nonplant(row, col):
                    size = self._board[row][col].size()
                    char = str(size) if size < 10 else "#"
                else:
                    char = '.'
                s.append(char)
            print(row, '  ', '  '.join(s), '\n', sep='')
        print()

    def is_plant(self, row, col):
        front = self._board[row][col].front()
        if front is not None:
            return isinstance(front, Plant)
        return False

    def is_nonplant(self, row, col):
        front = self._board[row][col].front()
        if front is not None:
            return isinstance(front, NonPlant)
        return False

    def remove(self, row, col):
        item = self._board[row][col].dequeue()
        if isinstance(item, NonPlant):
            self.cash += item.worth
    def place_nonplant(self, row):
        self._board[row][self.width - 1].enqueue(NonPlant())
        self.non_plants += 1

    def place_plant(self, row,col):
        if not self._board[row][col].is_empty() or col >= self.width:
            print("cannot place plant there")
            return
        if not self.cash >= Plant.cost:
            print("you don't have enough cash")
            return
        self.cash -= Plant.cost
        self._board[row][col].enqueue(Plant())


    def place_wave(self):
        curr = self.waves.head
        while curr != None:
            if (curr.data.wave_num > self._turn):
                break
            if (curr.data.wave_num == self._turn):
                for i in range(curr.data.num):
                    self.place_nonplant(curr.data.row);
                curr = curr.next
                self.waves.remove_beginning()
                self.waves_num -= 1


    def plant_turn(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.is_plant(row, col):
                    current_plant = self._board[row][col].front()
                    for col_after_plant in range(col, self.width):
                        if self.is_nonplant(row, col_after_plant):
                            current_nonplant = self._board[row][col_after_plant].front()
                            current_plant.attack(current_nonplant)
                            if current_nonplant.hp <= 0:
                                self.remove(row, col_after_plant)
                                self.non_plants -= 1

    def _move_nonplants(self, _from, to):
        from_queue = self._board[_from[0]][_from[1]]
        to_queue = self._board[to[0]][to[1]]
        while not from_queue.is_empty():
            to_queue.enqueue(from_queue.dequeue())




    def _nonplant_attack(self, NonPlant, plant):

        plant.hp -= (NonPlant.size() * NonPlant.front().dmg)
        return plant.hp <= 0



    def nonplant_turn(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.is_nonplant(row, col):
                    current_nonplant = self._board[row][col]
                    before_nonplant_col = col - 1
                    if before_nonplant_col >= 0:
                        if not self.is_plant(row, before_nonplant_col):
                            self._move_nonplants((row, col),
                                                 (row, before_nonplant_col))
                    else:
                        self.game_over = True
                        return

                    if self.is_plant(row, before_nonplant_col):
                        if self._nonplant_attack(current_nonplant, self._board[row][before_nonplant_col].front()):
                            self.remove(row, before_nonplant_col)


    def run(self):
        self.place_wave()
        self.draw()
        self.get_input()
        self.run_turn()
        while not self.game_over  and self.non_plants > 0:
            self.draw()
            self.get_input()
            self.run_turn()

        if not self.game_over:
            print("You Won")
        else:
            print("You Lost")



    def _weaken_powerups(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.is_plant(row, col):
                    self._board[row][col].front().weaken_powerup()



    def run_turn(self):
        self.plant_turn()
        self.nonplant_turn()
        self._weaken_powerups()
        self._turn += 1
        self.place_wave()


    def draw_card(self):
        card = self._power_ups.pop()
        cash_after_cost = self.cash - Card.cost
        if cash_after_cost >= 0:
            for row in range(self.height):
                for col in range(self.width):
                    if self.is_plant(row, col):
                        self._board[row][col].front().apply_powerup(card)
            self.cash = cash_after_cost



    def get_input(self):
        while True:
            ui = input(f"""
            Action?
            [ROW COL] to place plant (${Plant.cost})
            [C] to draw powerup card (${Card.cost})
            [Q] to quit
            [ENTER to do nothing?
            """)

            if (len(ui) > 0):
                if (len(ui) == 1):
                    if (ui.lower() == "c"):
                        self.draw_card()
                        break
                    elif (ui.lower() == "q"):
                        self.game_over = True
                        break
                    else:
                        print(f"Invalid Input {ui}")
                else:
                    try:
                        row, col = [int(x) for x in ui.split(" ")]
                        self.place_plant(row, col)
                        break
                    except:
                        print(f"Invalid Input {ui}")
            else:
                break