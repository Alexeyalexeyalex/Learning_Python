# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
firstList = []
secondList = []
resultList = []
with open ("Result1.txt","r") as first:
    firstList = str(first.read()).split("+")
with open ("Result2.txt","r") as second:
    secondList = str(second.read()).split("+")
if len(firstList)<len(secondList):
    firstList, secondList = secondList, firstList
i = 0
while i != len(firstList) - len(secondList):
    resultList.append(firstList[i])
    i+=1

for i in firstList:
    for j in secondList:
        if "**" in i and "**" in j: 
            if i[i.index("**"):] == j[j.index("**"):]:
                resultList.append(" "+str(int(i[:i.index("*")]) + int(j[:j.index("*")]))+"*x"+str(i[i.index("**"):]))
        elif  "**" not in i and "**" not in j: 
            if "x" in i and "x" in j:
                resultList.append(" "+str(int(i[:i.index("*")]) + int(j[:j.index("*")]))+"*x ")
            elif "x" not in i and "x" not in j:
                resultList.append(" "+str(int(i) + int(j)))

print("+".join(resultList))
        
with open('Main.txt','w') as data:
    data.write("+".join(resultList))
                
    


