L1 = [5,48,75,96,18]
print(L1[4])
L1[1] = 17
L1[3] = L1[2]+L1[4]
print(L1[-1])

for l in L1:
    print(l, end=' ')
print()
for l in L1:
    print(l)
print()
for i in range(len(L1)-1,0,-1):
    print(L1[i])