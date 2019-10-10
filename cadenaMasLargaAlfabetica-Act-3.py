alf = {'0':1,'1':2,'2':3,'3':4,'4':5,'5':6,    #En este diccionario puse valores para el abecedario
'6':7,'7':8,'8':9,'9':10,'a':11,'b':12,	       #para luego compararlos de acuerdo a estos y no los de ascii 
'c':13,'d':14,'e':15,'f':16,'g':17,'h':18,     #que nos fallan
'i':19,'j':20,'k':21,'l':22,'m':23,'n':24, 
'ñ':25,'o':26,'p':27,'q':28,'r':29,'s':30,
't':31,'u':32,'v':33,'x':34,'y':35,'z':36}
s = input()
startIndex = 0
finalIndex = 0
newStart = 0
newEnd = 0
for i in range(len(s)):
	if i == 0 or alf[str(s[i])] >= alf[str(s[i-1])]:
		newEnd = i				#Si el valor de la letra es mayor significa que
							#va despues en el alfabeto
							#total que si todo va bien y 
							#en orden se asigna el actual como el final
	
	else:						
		newEnd = i-1
		newStart = i
	if (newEnd - newStart) > (finalIndex - startIndex):
		finalIndex, startIndex = newEnd, newStart
print("La subcadena más larga en orden alfabético es:", s[startIndex:finalIndex + 1])
