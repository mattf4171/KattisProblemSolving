from enum import Enum


class CellType(Enum):
    WATER = "W"
    LAND = "L"
    CLOUD = "C"

    @staticmethod
    def from_str(symbol):
        if symbol == "W":
            return CellType.WATER
        elif symbol == "L":
            return CellType.LAND
        elif symbol == "C":
            return CellType.CLOUD


class Direction:
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    @staticmethod
    def get_directions():
        return Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT

    @staticmethod
    def get_coordinates(coordinates: tuple, offset: tuple):
        return tuple(map(sum, zip(coordinates, offset)))


class Cell:
    def __init__(self, cell_type: CellType, x, y):
        self.cell_type = cell_type
        self.x = x
        self.y = y
        self.visited = False

    def __str__(self):
        return f"{{{self.cell_type}, {self.visited}}}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.cell_type == other.cell_type


class Surface:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.surface_map = []

    def get(self, x, y):
        if x >= self.n_cols or y >= self.n_rows or x < 0 or y < 0:
            return None
        return self.surface_map[y][x], (x, y)

    def add_row(self, row):
        self.surface_map.append(row)

    def get_neighbors(self, coordinates: tuple):
        return list(filter(
            lambda n: n is not None,
            [
                self.get(*Direction.get_coordinates(coordinates, direction))
                for direction in Direction.get_directions()
            ]
        ))

    def make_islands(self):
        for y_i, y_v in enumerate(self.surface_map):
            for x_i, x_v in enumerate(y_v):
                if x_v.cell_type == CellType.LAND and not x_v.visited:
                    x_v.visited = True
                    self.__make_island(x_i, y_i)

    def __make_island(self, x_i, y_i):
        def can_attach(cell: Cell):
            if cell.cell_type == CellType.CLOUD:
                cell.cell_type = CellType.LAND
            return cell.cell_type == CellType.LAND

        for neighbor in list(filter(lambda n: can_attach(n[0]), self.get_neighbors((x_i, y_i)))):
            self.__make_island(*neighbor[1])

    def __str__(self):
        return "".join(str(row) + "\n" for row in self.surface_map)


def main(*args, **kwargs):
    n_rows, n_cols = map(lambda x: int(x.strip()), input().split())
    surface = Surface(n_rows, n_cols)
    for y_i in range(n_rows):
        surface.add_row([Cell(CellType.from_str(x_v), x_i, y_i) for x_i, x_v in enumerate(list(input()))])
    surface.make_islands()
    print(surface)


if __name__ == '__main__':
    main()


# 4 4
# LWWC
# CWWC
# CWWC
# CCCC