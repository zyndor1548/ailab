import itertools

def crpyt(puzzle):
	left, right = puzzle.replace(" ","").split("=")
	left_words = left.split("+")

	words = left_words + [right]

	letters = set("".join(words))

	if len(letters) > 10:
		print("i hate pyton")
		return None
	first_letters = set(word[0] for word in words)

	for perm in itertools.permutations(range(10),len(letters)):
		mapping = dict(zip(letters,perm))
		if any(mapping[i] == 0 for i in first_letters):
			continue
				
		try:
			left_sum = sum(int("".join(str(mapping[c]) for c in word)) for word in left_words)
			right_val = int("".join(str(mapping[c]) for c in right))
			if left_sum == right_val:
				return mapping
		except ValueError:
				continue
	return None
			
    


puzzle = input("Enter Crypt puzzle : ")
solution = crpyt(puzzle)

if solution == None:
	print("no solution")
else:
    print(f"{solution}")
    for letter in sorted(solution):
        print(f"{letter} = {solution[letter]}")
    print(f"{puzzle}")
    left, right = puzzle.replace(" ","").split("=")
    left_words = left.split("+")
    print(f'{"+".join("".join(str(solution[c]) for c in word) for word in left_words)} = {"".join(str(solution[c]) for c in right)}')
	
	

        
		
  
	