def Method1(str1,str2):
	return str1.count(str2)

def Method2(str1,str2):
	cnt = 0
	i = 0
	while i<len(str1):
		j = 0
		while j<len(str2):
			if str2[j]==str1[i]:
				j+=1
				i+=1
			else:
				break
		if j==len(str2):
			cnt+=1
			i-=1
		else:
			i-=j
		i+=1
	return cnt

string_1  =  input()

string_2 = input()

print(Method1(string_1,string_2))
print(Method2(string_1,string_2))
