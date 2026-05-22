import random

n = int(input("Enter number of nods : "))
  
dist = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        num = random.randint(1,10)
        dist[i][j] = num
        dist[j][i] = num
for i in range(n):
	print(f"node {i}: {dist[i]}")
path = list(range(n))
random.shuffle(path)

def path_cost(path):
    cost = 0
    for i in range(n-1):
        cost += dist[path[i]][path[i+1]]
    cost += dist[path[-1]][path[0]]
    return cost

cost = path_cost(path)

for _ in range(1000):
    improve = False
    for i in range(n):
        for j in range(i+1,n):
            new_path = path[:]
            new_path[i],new_path[j] = new_path[j],new_path[i]
            new_cost = path_cost(new_path)
            
            if new_cost < cost:
                path = new_path
                cost = new_cost
                improve = True
    if not improve:
        break

print(f"sortest path = {path}")
print(f"cost = {cost}")