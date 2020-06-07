#!/usr/bin/env python3
import sys

class Cube:
    def __init__(self, color):
        self.color = color
        self.left = None
        self.right = None

class CubeList:
    def __init__(self):
        self.head = Cube(None)
        self.tail = Cube(None)
        self.head.right = self.tail
        self.tail.left = self.head

    def append(self, cube):
        cube.left = self.tail.left
        self.tail.left.right = cube
        cube.right = self.tail
        self.tail.left = cube

    def size(self):
        s = 0
        it = self.iter()
        while it.has_next():
            it.next()
            s += 1
        return s

    def __str__(self):
        colors = []
        it = self.iter()
        while it.has_next():
            colors.append(it.next().color)
        return '->'.join(colors)

    def iter(self):
        return self.Iter(self)

    class Iter:
        def __init__(self, cube_list):
            self.cube_list = cube_list
            self.cur = cube_list.head

        def has_next(self):
            return self.cur.right != self.cube_list.tail

        def next(self):
            self.cur = self.cur.right
            return self.cur

        def back(self):
            assert not self.is_head()
            self.cur = self.cur.left

        def is_head(self):
            return self.cur == self.cube_list.head

        def remove(self):
            assert self.cur != self.cube_list.head
            assert self.cur != self.cube_list.tail
            self.cur = self.cur.left
            self.cur.right = self.cur.right.right
            self.cur.right.left = self.cur

def solve(S: str):
    cubes = CubeList()
    for c in S:
        cubes.append(Cube(c))
    for _ in range(100):
        ci = cubes.iter()        
        while ci.has_next():
            l = ci.next()
            if not ci.has_next():
                break
            r = ci.next()
            if l.color == r.color:
                ci.back()
                continue
            ci.remove()
            ci.remove()
    return len(S) - cubes.size()
    

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    print(solve(S))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
