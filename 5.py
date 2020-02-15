def findHighestProfit(hargaSaham):
	sahamKecil = min(hargaSaham)
	lokasi_sahamKecil = hargaSaham.index(min(hargaSaham))
	sahamBesar = max(hargaSaham[lokasi_sahamKecil : len(hargaSaham)])
	profit = sahamBesar - sahamKecil
	if(profit > 0):
		print(profit)
	else:
		print("Tidak bisa mendapatkan profit pada hari-hari ini")

profit1 = [10, 2, 11, 20, 3, 5]
profit2 = [33, 29, 11, 3]

# findHighestProfit(profit1)
# findHighestProfit(profit2)