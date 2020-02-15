import numpy as np

def validateColor(hexCodeWarna):
	karakter_benar = np.array([0, 1, 2, 3, 4, 5, 6, 7,
								'A', 'B', 'C', 'D', 'E', 'F',
								'a', 'b', 'c', 'd', 'e', 'f'])
	if(hexCodeWarna[0] == '#' and 3 <= len(hexCodeWarna) - 1 <= 6):
		for i in range(1, len (hexCodeWarna)):
			if(np.any(hexCodeWarna[i] == karakter_benar)):
				if(i == len(hexCodeWarna) - 1):
					print("Format Hex Code Benar!")
			else:
				print("Format Hex Code Salah!")
				break
	else:
		print("Format Hex Code Salah!")

# validateColor("#eee")
# validateColor("#eeeeeee")
# validateColor("#F3F3F3")
# validateColor("#ezff8d")