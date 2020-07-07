def Method1(str1,str2):
	return str1.count(str2)

def Method2(str1,str2):
	cnt = 0
	for s in str1.split(" "):
		if str2 in s:
			cnt+= 1
	return cnt


string_1  =  input()

string_2 = input()

print(Method1(string_1,string_2))
print(Method2(string_1,string_2))