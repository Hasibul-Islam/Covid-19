'''
Tried two methods here.
'''

def Method1(str1,str2):
	'''
	input: 2 parameters. str1,str2. str1 is the main string and str2 is the string to find in str1.
	operation: simply returns the number of counts of occurence of str2 in str1 using built in count funtion.
	output: returns an integer number: the number of occurence.
	'''
	return str1.count(str2)

def Method2(str1,str2):
	'''
	input: 2 parameters. str1,str2. str1 is the main string and str2 is the string to find in str1.
	operation: simply returns the number of counts of occurence of str2 in str1. Here checking whether a sequence of characters of
	str1 are matched with characters of str2. 
	output: returns an integer number: the number of occurence.
	'''
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

print(Method1(string_1,string_2)) #call Method1
print(Method2(string_1,string_2)) #call Method2
