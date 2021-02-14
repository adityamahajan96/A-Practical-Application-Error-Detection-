def matmul(a,b):
	if len(a[0]) != len(b):
		return -1
	c = []
	for i in range(len(a)):
		temp = []
		for j in range(len(b[0])):
			temp.append(0)
		c.append(temp)
	
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(a[0])):
				c[i][j] = c[i][j]+a[i][k]*b[k][j]
	
	
	return c

def transpose(a):
	c = []
	for i in range(len(a[0])):
		temp = []
		for j in range(len(a)):
			temp.append(0)
		c.append(temp)
		
	for i in range(len(a)):
		for j in range(len(a[0])):
			c[j][i] = a[i][j]
	
	return c
	

def padZeroes(E, key):
	for i in range(len(key)-1):
		E = E+"0"
	
	return E
	
def binaryDivision(dividend, key):
	rem = ""
	quo = ""
	curr = dividend[0:len(key)]
	#print("Curr is ", curr)
	for i in range(len(key),len(dividend)+1):
		if curr[0] == "1":
			quo = quo + "1"
			#print("key is ",key)
			rem = xorKey(curr, key)
		else :
			quo = quo + "0"
			rem = curr
		
		#print("rem is ", rem)
		if i == len(dividend):
			curr = rem[1:]
			break
		curr = rem[1:]+dividend[i]
		#print("curr is ", curr)	
	
	
	return curr

def xorKey(curr, key):
	ans = ""
	for i in range(len(key)):
		if curr[i] == key[i]:
			ans = ans + "0"
		else :
			ans = ans + "1"
			
	return ans
