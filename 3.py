def countChar(input_string, character_in):
	counterChar = 0
	for i in range(len(input_string)):
		if(input_string[i] == character_in):
			counterChar = counterChar + 1
	print(counterChar)

# countChar("arka","a")