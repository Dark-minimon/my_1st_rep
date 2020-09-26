x=5
for i in range (1, x+1):
	for m in range (x+1, i, -1):
		print(" ", end=' ')
	for m in range (1, i+1):
		print(m, end=' ')
	for m in range (i-1, 0, -1):
		print(m, end=' ')
	print("\n")
