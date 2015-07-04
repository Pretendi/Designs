def p11():
	
	f = open('grid_data.txt','r')
	stored = f.read().split('\n')
	for i in range(0, len(stored)):
		stored[i] = stored[i].split(' ')
	
	largest = 0
	for i in range(0, 20):
                for j in range(0, len(stored[i])):
			stored[i][j]=int(stored[i][j])	
	for i in range(0, len(stored)):
		for j in range(0, 20):
			
			if(i<17):
				largest = max(largest, stored[i][j]*stored[i+1][j]*stored[i+2][j]*stored[i+3][j])

			if(j<17):
				largest = max(largest, stored[i][j]*stored[i][j+1]*stored[i][j+2]*stored[i][j+3])
			
			if((i<17) and (j<17)):
				largest = max(largest, stored[i][j]*stored[i+1][j+1]*stored[i+2][j+2]*stored[i+3][j+3])
			
			if((i>2) and (j<17)):
				largest = max(largest, stored[i][j]*stored[i-1][j+1]*stored[i-2][j+2]*stored[i-3][j+3])	
	print largest


p11()
