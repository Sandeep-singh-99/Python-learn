fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

newList1 = [x for x in fruits if "a" in x]
print(newList1)
