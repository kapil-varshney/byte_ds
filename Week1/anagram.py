import re

def isAnagram(a, b):

	str1 = re.sub('\s', '', a).lower()
	str2 = re.sub('\s', '', b).lower()

	if (len(str1) != len(str2)):
		return False

	string1 = [ch for ch in str1]
	string2 = [ch for ch in str2]
	i = 0
	l = len(string1)

	while i<l :
		
		char = string1[i]
		
		if char in string2:
			string1.remove(char)
			string2.remove(char)
			l-=1

		else:
			i+=1


	if (string1 == string2):
		return True
	
	return False


print(isAnagram("Tom Marvolo Riddle", "I am Lord Voldemort"))