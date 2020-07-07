n = input()
def Method1(n):
	m = (n+'.')[:-1]
	for c in m:
		if not c.isalnum():
			m = m.replace(c,'')
	return m


def Method2(n):
	m = (n+'.')[:-1]
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-" 
	for c in m:
		if c not in PERMITTED_CHARS:
			m = m.replace(c,'')
	return m


print(Method1(n))
print(Method2(n))