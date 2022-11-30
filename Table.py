class Table:
    def __init__(self, rows, cols):
        self.table = [[0] * cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_vale(self, row, col):
        if row > self.rows - 1 or row < 0 or\
                col > self.cols - 1 or col < 0:
            return None
        return self.table[row][col]

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def add_row(self, row):
        self.table.insert(row, [0 for _ in range(self.cols)])
        self.rows += 1

    def add_col(self, col):
        for row in self.table:
            row.insert(col, 0)
        self.cols += 1

    def delete_row(self, row):
        self.table.pop(row)
        self.rows -= 1

    def delete_col(self, col):
        for row in self.table:
            row.pop(col)
        self.cols -= 1


tab = Table(3, 3)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_vale(i, j), end='\t')
    print()
print()

tab.set_value(0, 0, 1000)
tab.set_value(1, 1, 2000)
tab.set_value(2, 2, 3000)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_vale(i, j), end='\t')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_vale(i, j), end='\t')
    print()
print()

tab.add_row(0)
tab.add_col(0)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_vale(i, j), end='\t')
    print()
print()

tab.delete_col(3)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_vale(i, j), end='\t')
    print()
print()
