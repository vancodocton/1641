# create matrix 5*5
myList = []
for i in range(5):
    tmp = []
    for j in range(i, i + 5):
        tmp.append(j + 1)
    myList.append(tmp)
print(myList)

# a.1st method
middleRows = []
middleRows.append(myList[1])
middleRows.append(myList[2])
middleRows.append(myList[3])
middleRows = myList[1:4]

middleRows = myList.copy()
middleRows.pop(4)
middleRows.pop(0)

print(middleRows)

# b.
lastRows = []
lastRows.append(myList[len(myList) - 2])
lastRows.append(myList[len(myList) - 1])

n = int(input("Enter n = "))

selectedList = myList[n]
tmp  = min(selectedList)
# c.
print("Max = ", max(myList[n]))
print("Min = ", min(myList[n]))

# d.
print("Sum = ", sum(myList[n]))

# e.
sorted(myList[n])
print(myList[n])


