class Grid:
    # If a cell is ON and has fewer than two neighbors that are ON, it turns OFF
    # If a cell is ON and has either two or three neighbors that are ON, it remains ON.
    # If a cell is ON and has more than three neighbors that are ON, it turns OFF.
    # If a cell is OFF and has exactly three neighbors that are ON, it turns ON.
    def __init__(self, n):
        grid = []
        for i in range(n):
            grid.append([])
            for _ in range(n):
                grid[i].append(0)

        self.grid = grid
        self.grid_n = n

    def reset_grid(self, n):
        grid = []
        for i in range(n):
            grid.append([])
            for _ in range(n):
                grid[i].append(0)

        self.grid = grid
        self.grid_n = n    

    def set_grid(self, ls):
        self.grid = ls

    def switch_cell(self, i, j):
        moment = self.grid[i][j]
        if moment == 1:
            self.grid[i][j] = 0
        else: self.grid[i][j] = 1

    def _count_neighbors(self, i, j):
        count = 0
        matrix = [(-1, -1),
                  (-1, 0),
                  (-1, 1),
                  (0, -1),
                  (0, 1),
                  (1, -1),
                  (1, 0),
                  (1, 1)]
        for e in matrix:
            try:
                if i == 0 or j == 0 and (e[0] == -1 or e[1] == -1): pass
                else: count += self.grid[i + e[0]][j + e[1]]
            except: pass
        return count

    def _tick_live(self, i, j):
        is_alive = True if self.grid[i][j] == 1 else False
        neighbors = self._count_neighbors(i, j)
        if is_alive and neighbors < 2: return 0
        elif is_alive and (neighbors == 2 or neighbors == 3): return 1
        elif is_alive and neighbors > 3: return 0
        elif not is_alive and neighbors == 3: return 1
        else: return 0


    def update_grid(self):
        new_grid = [[] for _ in range(self.grid_n)]
        for i in range(self.grid_n):
            for j in range(self.grid_n):
                new_grid[i].append(self._tick_live(i, j))
        
        self.grid = new_grid
