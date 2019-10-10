alf = {'0':1,'1':2,'2':3,'3':4,'4':5,'5':6,
'6':7,'7':8,'8':9,'9':10,'a':11,'b':12,
'c':13,'d':14,'e':15,'f':16,'g':17,'h':18,
'i':19,'j':20,'k':21,'l':22,'m':23,'n':24,
'ñ':25,'o':26,'p':27,'q':28,'r':29,'s':30,
't':31,'u':32,'v':33,'x':34,'y':35,'z':36}

s = input()

startIndex = 0
finalIndex = 1
newStart = 0
newEnd = 0

for i in range(len(s)):
	if i == 0 or alf[str(s[i])] >= alf[str(s[i-1])]:
		newEnd = i
	else:
		newEnd = i-1
		newStart = i
	if (newEnd - newStart) > (finalIndex - startIndex):
		finalIndex, startIndex = newEnd, newStart

print(s[startIndex:finalIndex + 1])
