n = int(input())
ls = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]
for i in range(n):
    print(ls[i % 5])    