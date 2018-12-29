len_case = []
T = int(input(""))

while T > 0:
	A = int(input(""))
	B = int(input(""))
	K = int(input(""))

	a = 1 <= T <= 100
	b = 1 <= A <= B < 10000
	c = 1 <= K < 10000

	if a and b and c:
		jml_case = []
		for x in range(A,B+1):
			if x % K == 0:
				jml_case.append(x)
			else:
				continue
		len_case.append(len(jml_case))
		T-=1
	else:
		break

for x in range (len(len_case)):
	print("Case {0}: {1}".format(x+1,len_case[x]))