# https://kopricky.github.io/code/For_Python/bit.html
class BIT:
    def __init__(self, node_size):
        self._node = node_size+1
        self.bit = [0]*self._node
 
    def add(self, index, add_val):
        index += 1
        while index < self._node:
            self.bit[index] += add_val
            index += index & -index
 
    def sum(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.bit[index]
            index -= index & -index
        return res
