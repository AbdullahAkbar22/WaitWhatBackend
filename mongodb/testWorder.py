def lettersInString(stringPassed):
	numberLetters = 0
	for i in range(len(stringPassed)):
		if (ord(stringPassed[i]) >= 65 and ord(stringPassed[i]) <= 90) or (ord(stringPassed[i]) >= 97 and ord(stringPassed[i]) <= 122):
			numberLetters += 1
	return numberLetters
	
	
print(str(lettersInString("--")))