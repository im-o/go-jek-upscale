import numpy as np

allwords = []
len_case = []
m = []
W = ""
def horizontal(i):
	len_w = len(W)
	awal_w = 0
	for x in m:
		var_kanan  = "".join(x).lower() #*nananannana#
		var_kiri   = "".join(x[::-1]).lower() #anannananan*
		index_cell = m.index(list(var_kanan)) #index ['n','a','n','a','n']

		for x in range(len(var_kanan)):#x in nananannana#
			if (W[0]==var_kanan[x]): #jika n == n
				fillt_kanan = var_kanan[x:] #n sampai akhir
				split_wordR = fillt_kanan[awal_w:len_w] # 1 - panjangW = nana
		
				if split_wordR==W and split_wordR==split_wordR[::-1] and len(split_wordR)==len(W): #x==y & x==z & len==len
					allwords.append(var_kanan[x::]+"[{0},{1}]-ke:{2}".format(index_cell+1,x+1,x)) #ana**-n [and get index baris dan kolom]-ke:x
					i+=1
				elif split_wordR==W and split_wordR!=split_wordR[::-1] and len(split_wordR)==len(W): #anan==anan && nana1=anan && 4==4
					allwords.append(var_kanan[x::]+"[{0},{1}]-ke:{2}".format(index_cell+1,x+1,x))
					i+=1
				else:
					pass
			else:
				pass
		for x in range(len(var_kiri)): #anannananan*
			if W[0]==var_kiri[x]:
				fillt_kiri  = var_kiri[x::]  #anannananan*
				split_wordL = fillt_kiri[awal_w:len_w] # 1 - panjangW = nana #anannananan*				
				
				if split_wordL==W and split_wordL!=split_wordL[::-1] and len(split_wordL)==len(W):
					allwords.append(var_kiri[x::] +"[{0},-{1}]-ke:{2}".format(index_cell+1,x+1,x))
					i+=1
	return(i)

def vertical(i):
	len_w     = len(W)
	awal_w    = 0
	after_zip = list(zip(*m))
	# print("XX:",after_zip)
	for x in after_zip:
		up_down = "".join(x).lower() #dari atas ke bawah
		down_up = "".join(x[::-1]).lower() #dari bawah ke atas
		# print("UP:",up_down)
		# print("DOWN:",down_up)
		for x in range(len(up_down)): #x in panjang up_down
			if W[0] == up_down[x]: #n == n
				fillt_up_down = up_down[x:] #nxxxx
				split_wordU   = fillt_up_down[awal_w:len_w] # 1 - panjang len_w = nana
				if split_wordU==W and split_wordU==split_wordU[::-1] and len(split_wordU)==len(W):
					# print("kata sama - Palindrome [ FOUND ]: ",up_down)
					allwords.append(up_down[x::]+"[v]")
					i+=1
				elif split_wordU==W and split_wordU!=split_wordU[::-1] and len(split_wordU)==len(W):
					# print("kata buka Palindrome: ",up_down)
					# print("--- kanan[+]",split_wordU, W)
					allwords.append(up_down[x::]+"[v]")
					i+=1

		for x in range(len(down_up)):
			if W[0] == down_up[x]:
				fillt_down_up = down_up[x:]
				split_wordD   = fillt_down_up[awal_w:len_w]

				if split_wordD==W and split_wordD!=split_wordD[::-1] and len(split_wordD)==len(W):
					# print("--- kiri[*]",split_wordD, W)
					allwords.append(down_up[x::]+"[^]")
					i+=1
	return(i)

def diagonalFunc(i):
	len_w     = len(W)
	awal_w    = 0
	matrix = np.array(m)
	diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]
	diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1))
	after_diag = list([n.tolist() for n in diags])
	# print(after_diag)
	for x in after_diag:
		diagno_rev = "".join(map(lambda x: "".join(x),x)).lower()
		diagaf_rev = "".join(map(lambda x: "".join(x),x[::-1])).lower()

		# print(diagno_rev)
		# print(diagaf_rev)
		for x in range(len(diagno_rev)):
			if W[0] == diagno_rev[x]:
				fillt_diagno_rev = diagno_rev[x:] #nxxxx
				split_wordno_rev = fillt_diagno_rev[awal_w:len_w] # 1 - panjang len_w = nana

				if split_wordno_rev==W and split_wordno_rev==split_wordno_rev[::-1] and len(split_wordno_rev)==len(W):
					# print("kata sama - Palindrome [ FOUND ]: ",diagno_rev)
					allwords.append(diagno_rev[x::]+"v")
					i+=1
				elif split_wordno_rev==W and split_wordno_rev!=split_wordno_rev[::-1] and len(split_wordno_rev)==len(W):
					# print("kata bukan palindrom: ",diagno_rev)
					# print("----[+] diagonal no reverser: ",split_wordno_rev,W)
					allwords.append(diagno_rev[x::]+"v")
					i+=1
		for x in range(len(diagaf_rev)):
			if W[0] == diagaf_rev[x]:
				fillt_diagaf_rev = diagaf_rev[x:] #nxxxx
				split_wordaf_rev = fillt_diagaf_rev[awal_w:len_w] # 1 - panjang len_w = nana
				
				if split_wordaf_rev==W and split_wordaf_rev!=split_wordaf_rev[::-1] and len(split_wordaf_rev)==len(W):
					allwords.append(diagaf_rev[x::]+"^")
					# print("----[*] diagonal after reverser: ",split_wordaf_rev,W)
					i+=1
	return(i)



if __name__ == '__main__':
	T = int(input(""))
	for x in range (T):
		N = int(input(""))
		M = int(input(""))

		for x in range(N):
			brp = input("")
			if len(brp)==M:
				m.append(list(brp))
			else:
				break

		W = input("")
		constarints = (1<=T<=100 and 1<=N<=100 and 1<=M<=100 and 1<=len(W)<=100)
		if constarints == True:
			panjang = diagonalFunc(0)+vertical(0)+horizontal(0)
			len_case.append(panjang)
			# print(np.array(m))
			m.clear()
		else:
			continue

	for x in range(len(len_case)):
		print("Case {0}: {1}".format(x+1,len_case[x]))
	# print(np.array(allwords))

	#ihope i can see gojek opr, please :)