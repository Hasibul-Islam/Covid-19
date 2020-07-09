'''
I have tried 2 methods here.
'''
n = input()
def Method1(n):
	'''
	input: takes a parameter as string. n is the name of the string.
	operation: removes every character that are not alphanumeric. Used in built alphanumeric method.
	output: returns the string after removing the non alphanumeric characters.
	'''
	m = (n+'.')[:-1]
	for c in m:
		if not c.isalnum():
			m = m.replace(c,'')
	return m


def Method2(n):
	'''
	input: takes a parameter as string. n is the name of the string.
	operation: removes every character that are not alphanumeric. Used a list of permited characters so that I can check whether
	the characters are accepted or not.
	output: returns the string after removing the non alphanumeric characters.
	'''
	m = (n+'.')[:-1]
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-" 
	for c in m:
		if c not in PERMITTED_CHARS:
			m = m.replace(c,'')
	return m


print(Method1(n)) #Call Method1
print(Method2(n)) #Call Method2