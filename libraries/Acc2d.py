class Acc2d:
    def __init__(self, array2d):
        h, w = len(array2d), len(array2d[0])
        hh, ww = h + 1, w + 1
        self.acc_table = [[0] * ww for _ in range(hh)]
        for i in range(1, hh):
            for j in range(1, ww):
                self.acc_table[i][j] = self.acc_table[i-1][j] + self.acc_table[i][j-1] - self.acc_table[i-1][j-1] + array2d[i-1][j-1]

    def calc_sum(self, pos1, pos2):
        x, y = pos1
        xx, yy = pos2
        return self.acc_table[xx][yy] - self.acc_table[xx][y] - self.acc_table[x][yy] + self.acc_table[x][y]

    def __str__(self):
        return '\n'.join(map(str, self.acc_table))
