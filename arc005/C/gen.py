H, W = 500, 499
from random import randrange, seed
seed(0)

res = []
for h in range(H):
    res.append([])
    for w in range(W):
        if randrange(10) < 4:
            res[-1].append("#")
        else:
            res[-1].append(".")

res[0][0] = "s"
res[H-1][W-1] = "g"

print(H, W)
print(*["".join(r) for r in res], sep="\n")
