n = int(input())
road_ans = 1
height_ans = 0
for i in range(1, n + 1):
    num = int(input())
    ok = False
    min_height = ''
    for j in range(1, num + 1):
        height = int(input())
        if min_height != '':
            if height < min_height:
                min_height = height
        else:
            min_height = height
    if min_height > height_ans:
        height_ans = min_height
        road_ans = i
print(road_ans, height_ans)
        

        
        