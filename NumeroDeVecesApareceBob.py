s = input()
res = 0
for i in range(len(s)):
	if i < len(s)-2:
		if s[i] == 'b' and s[i + 1] == 'o' and s[i + 2] == 'b':
			res = res + 1
print("Número de veces que se produce bob es:", res) 
