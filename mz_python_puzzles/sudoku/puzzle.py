class Puzzle(object):
    def __init__(self, unit):
        self.unit = unit
        self.size = unit * unit
        self.grid = [[None] * self.size for i in range(self.size)]

    def __getitem__(self, row):
        return self.grid[row]

    def known_cells(self):
        for r in range(self.size):
            for c in range(self.size):
                if self[r][c]:
                    yield [r, c, self[r][c]]


def parse_puzzle(input):
    lines = input.split('\n')

    unit = int(lines[0])
    puzzle = Puzzle(unit)

    for r in range(puzzle.size):
        fixed_value_pieces = lines[r + 1].split()
        assert len(fixed_value_pieces) == puzzle.size

        for c in range(puzzle.size):
            if fixed_value_pieces[c] != '_':
                puzzle[r][c] = int(fixed_value_pieces[c])

    return puzzle
