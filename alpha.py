def alphabeta(values,depth,branching,ismax,alpha,beta,index=0,path=None):
	if path is None:
		path = []
	if depth == 0:
		return values[index], path + [values[index]]
	if ismax:
		max_val = -float('inf')
		best_path =[]
		for i in range(branching):
			child_index = index * branching + i
			if child_index >= len(values):
				break
			val , childpath = alphabeta(values,depth-1,branching,False,alpha,beta,child_index,path)

			if val > max_val:
				max_val = val
				best_path = [f"max({val})"] + childpath
			alpha = max(alpha,max_val)
			if beta <= alpha:
				break

		return max_val,best_path
	else:
		min_val = float('inf')
		best_path =[]
		for i in range(branching):
			child_index = index * branching + i
			if child_index >= len(values):
				break
			val , childpath = alphabeta(values,depth-1,branching,True,alpha,beta,child_index,path)

			if val < min_val:
				min_val = val
				best_path = [f"min({val})"] + childpath
			beta = min(beta,min_val)
			if beta <= alpha:
				break

		return min_val,best_path
		

values = [5, 3, 2, 4, 1, 3, 6, 2, 8, 7, 5, 1, 3, 4, 6, 2]
branching = 2
depth = 4   # 2^4 = 16 leaf nodes

print("Game Tree Alpha-Beta Pruning")
print("Leaf values:", values)
print("Branching factor:", branching)
print("Depth:", depth)
print("Root player: MIN\n")

value, path = alphabeta(values, depth, branching, False, -float('inf'), float('inf'))

print("Root value:", value)
print("Best path:", path)