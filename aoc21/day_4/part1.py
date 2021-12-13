from functools import reduce


class Board:
    def __init__(self, board):
        self.board = board
        self.drawn_number = [-1000 for i in range(25)]

    def add_number(self, number):
        if number in self.board:
            self.drawn_number[self.board.index(number)] = number

    # I read it wrong. This was uneccessary
    def _horizontal_value(self, pos):
        return int(self.drawn_number[5*pos]) +\
            int(self.drawn_number[5*pos + 1]) +\
            int(self.drawn_number[5*pos + 2]) +\
            int(self.drawn_number[5*pos + 3]) +\
            int(self.drawn_number[5*pos + 4])\

    def _horizontal(self, pos):
        return True if self._horizontal_value(pos) > 0 else False

    # I read it wrong. This was uneccessary
    def _vertical_value(self, pos):
        return int(self.drawn_number[5 - 1]) +\
            int(self.drawn_number[5 + 1 * 5 - 1]) +\
            int(self.drawn_number[5 + 2 * 5 - 1]) +\
            int(self.drawn_number[5 + 3 * 3 - 1]) +\
            int(self.drawn_number[5 + 4 * 4 - 1])\

    def _vertical(self, pos):
        return True if self._vertical_value(pos) > 0 else False

    def unmarked_value(self):
        unmarked_sum = 0
        for i, number in enumerate(self.drawn_number):
            if number == -1000:
                unmarked_sum += int(self.board[i])
        return unmarked_sum

    def check(self):
        for i in range(5):
            if self._horizontal(i):
                return self.unmarked_value()
            if self._vertical(i):
                return self.unmarked_value()
        return False

data = list(map(lambda x: x.strip(), open('data.txt', 'r')))
#data = list(map(lambda x: x.strip(), open('test.txt', 'r')))
numbers, input_data = data[0].split(","), data[2:]
boards = []

board = []
for i, line in enumerate(input_data):
    if line == "":
        boards.append(Board(board))
        board = []
    else:
        for x in list(x for x in line.split(" ")):
            if x != "":
                board.append(x)
    if i == len(input_data) - 1:
        boards.append(Board(board))
        board = []

winner = False
for number in numbers:
    for board in boards:
        if winner:
            break
        board.add_number(number)
        if board.check():
            print("board check", board.check() * int(number))
            winner = True
            break
