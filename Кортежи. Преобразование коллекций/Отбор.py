n = int(input())

names = list()
marks = list()
strings = list()

for i in range(n):
    item = input()
    
    name = ""
    mark = item[len(item) - 1]
    
    print(item)
    
    for j in range(len(item)):
        if item[j] == " ":
            break
        name += item[j]
    names.append(name)
    marks.append(int(mark))
    strings.append(item)
print()
for i in range(n):
    if marks[i] >= 4:
        print(strings[i])    