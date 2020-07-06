n = input()
for c in n:
	if not c.isalnum():
		n = n.replace(c,'')
print(n)