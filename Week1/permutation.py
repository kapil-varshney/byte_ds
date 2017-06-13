def isPermutation(L):

	L1 = set(L)
	
	if ((len(L1) != max(L1)) or (min(L1) != 1) or (len(L1) != len(L))):
		return False

	else:
		return True

print(isPermutation([1,2,3,3,4]))