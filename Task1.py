n = input()
def Method1(n):
	m = (n+'.')[:-1]
	for c in m:
		if not c.isalnum():
			m = m.replace(c,'')
	print(m)


def Method2(n):
	m = (n+'.')[:-1]
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-" 
	for c in m:
		if c not in PERMITTED_CHARS:
			m = m.replace(c,'')
	print(m)


Method1(n)
Method2(n)