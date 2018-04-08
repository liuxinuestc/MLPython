
t = 30
ticket = [3,5,62,3,6,5,8]

maxT = max(ticket)

ticket.remove(maxT)
N = len(ticket)
bag = [[0 for i in range(t)] for j in range(N)]

for i in range(N):
    for j in range(1,t):
        if ticket[i] <= j:
            bag[i][j] = max(bag[i-1][j],bag[i-1][j-ticket[i]]+ticket[i])
        else:
            bag[i][j] = bag[i-1][j]
print(bag[N-1][t-1]+maxT)

a = 1
for i in range(10):
    a = a*2+1

print(a)