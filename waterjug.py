from collections import deque

def dfs(max1,max2,goal):
	stack = [(0,0,[])]
	visited = set()
	visited.add((0,0))

	while stack:
		jug1,jug2,path = stack.pop()
		if jug1 == goal or jug2 == goal:
			return path+[(jug1,jug2)]
		moves = []        

		if jug1 < max1:
			moves.append((max1,jug2))
		if jug2 < max2:
			moves.append((jug1,max2))
		if jug1 > 0:
			moves.append((0,jug2))
		if jug2 > 0:
			moves.append((jug1,0))
		if jug1 > 0 and jug2 < max2:
			diffrence = min(jug1 , max2 - jug2)
			moves.append((jug1 - diffrence,jug2 + diffrence))
		if jug2 > 0 and jug1 < max1:
			diffrence = min(jug2 , max1 - jug1)
			moves.append((jug1 + diffrence,jug2 - diffrence))
		for state in moves:
			if state not in visited:
				visited.add(state)
				stack.append((state[0],state[1],path + [(jug1,jug2)]))

	return None

max1=int(input("Enter first jug size (4) = "))
max2=int(input("Enter secondjug size (3) = "))
goal=int(input("Enter Goal state = "))

path = dfs(max1,max2,goal)
if path:
	for i,state in enumerate(path,1):
		print(f"{i} {state}")
else :
	print("no solution")