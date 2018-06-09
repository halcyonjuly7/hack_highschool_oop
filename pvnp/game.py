from linked_list import LinkedList
from queue import Queue
from stack import Stack
from wave import Wave
from non_plant import Non_Plant
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
            for line in iter(f.readline, ""):
                self.waves.add(Wave(*[int(x) for x in line.split(" ")]))
                self.waves_num += 1

        self._board = Game._create_board(self.width, self.height)
        self._is_game_over = False
        self._turn_number = 0
        self._non_plants = 0
        self._power_ups = Game._init_powerups()

    @staticmethod
    def _create_board(height, width):
        board = []
        for _ in range(height):
            row = []
            for __ in range(width):
                row.append(Queue())
            board.append(row)
        return board


    @staticmethod
    def _init_powerups():
        stack = Stack()
        nums = [1, 2, 3, 4, 5]
        for _ in range(100):
            stack.push(Card(random.choice(nums)))
        return stack

    def draw(self):
        print("Cash: $", self.cash, "\nWaves: ", self.waves_num, sep="")
        s = " ".join([str(i) for i in range(self.width - 1)])
        print(" ", s)
        for row in range(self.height):
            s = []
            for col in range(self.width):
                if self.is_plant(row, col):
                    char = "P"
                elif self.is_nonplant(row, col):
                    size = self.board[row][col].size()
                    char = str(size) if size < 10 else "#"
                else:
                    char = "."
                s.append(char)
            print(row, " ", " ".join(s), "\n", sep="")
        print()

    def is_plant(self, row, col):
        return isinstance(self._board[row][col].front(), Plant)

    def is_nonplant(self, row, col):
        return isinstance(self._board[row][col].front(), Non_Plant)

    def remove(self, row, col):
        self._board[row][col].dequeue()

    def place_nonplant(self, row):
        self._board[row][self._width - 1].enqueue(Non_Plant())
        self._non_plants += 1

    def place_plant(self, row,col):
        if not self._board[row][col].is_empty() and  col >= self.width:
            print("cannot place plant there")
            return
        if not self.cash >= Plant.cost:
            print("you don't have enough cash")
            return

        self._board[row][col].enqueue(Plant())

    def _place_non_plant_waves(self, wave):

        target_col = self._board[wave.row][self.width - 1]
        for _ in wave.num:
            target_col.enqueue(Non_Plant())
        self._non_plants += wave.num

    def place_wave(self):
        current_wave = self.waves.head
        self._place_non_plant_waves(current_wave)
        current_wave.next = None
        self.waves.head = self.waves.head.next
        self.waves_num -= 1
        self._turn_number += 1


    def plant_turn(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.is_plant(row, col):
                    current_plant = self._board[row][col].front()
                    for col_after_plant in range(col, self.width):
                        if self.is_nonplant(row, col_after_plant):
                            current_non_plant = self._board[row][col_after_plant].front()
                            current_plant.attack(current_non_plant)
                            if current_non_plant.hp <= 0:
                                self.remove(row, col_after_plant)
                                self._non_plants =- 1
                            break

    def _move_non_plants(self, _from, to):
        from_queue = self._board[_from[0]][_from[1]]
        to_queue = self._board[to[0]][to[1]]
        while not from_queue.is_empty():
            to_queue.enqueue(from_queue.dequeue())



    # def non_plant_turn(self):
    #     for row in range(self.height):
    #         for col in range(self.width):
    #             if self.is_nonplant(row, col):
    #                 current_non_plant = self._board[row][col]
    #                 for before_non_plant_col in range(col, -1, -1):
    #                     if self.is_plant(row, before_non_plant_col):
    #                         current_plant = self._board[row][before_non_plant_col]
    #                         current_non_plant.attack(current_plant)
    #                         if current_plant.hp <= 0:
    #                             self.remove(row, col)
    #                             if before_non_plant_col - 1 != 0:
    #                                 self._move_non_plants((row, before_non_plant_col),
    #                                                       (row, before_non_plant_col - 1))
    #                             else:
    #                                 self._is_game_over = True
    #                                 return
    #                         break


    def _non_plant_attack(self, non_plant, plant):
        plant.hp -= non_plant.size() * Non_Plant.dmg
        return plant.hp <= 0



    def non_plant_turn(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.is_nonplant(row, col):
                    current_non_plant = self._board[row][col]
                    before_non_plant_col = col-1
                    if self.is_plant(row, before_non_plant_col):
                        if self._non_plant_attack(current_non_plant, self._board[row][before_non_plant_col]):
                            self.remove(row, col)
                            if before_non_plant_col - 1 != 0:
                                self._move_non_plants((row, before_non_plant_col),
                                                      (row, before_non_plant_col - 1))
                            else:
                                self._is_game_over = True
                                return
                        break


    def run(self):
        while not self._is_game_over and self.waves_num > 0 and self._non_plants > 0:
            self.get_input()
            self.run_turn()

        if not self._is_game_over:
            print("You Won")
        else:
            print("You Lost")



    def _weaken_powerups(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.is_plant(row, col):
                    self._board[row][col].front().weaken_powerup()



    def run_turn(self):
        self._turn_number += 1
        self._weaken_powerups()
        if self.waves.front():
            self.place_wave()
        self.plant_turn()
        self.non_plant_turn()
        self.draw()


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
                        self.over = True
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














