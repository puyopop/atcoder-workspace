n = int(input())
a = list(map(int,input().split()))
count2 = 0
count4 = 0
for i in range(n):
    #２の倍数だが４の倍数でない
    if a[i]%2 == 0 and a[i]%4 != 0:
        count2 += 1
    #４の倍数
    elif a[i]%4 == 0:
        count4 += 3

#print(count2,count4)

#２の倍数が奇数か偶数か判定
if count2 >= 2 and count2%2 == 0:
    count4 += count2
elif count2 >= 2 and count2%2 == 1:
    count4 += count2+1

if count4 >= n:
    print("Yes")
else:
    print("No")
