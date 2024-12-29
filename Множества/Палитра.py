n = int(input())
color_count = 0
color_gen_cnt = 0

common_set = set()
was = set()

for i in range(n):
    m = int(input())
    for colr in range(m):
        color = input()
        if color in common_set:
            if color not in was:
                color_count += 1
                was.add(color)
            
            color_gen_cnt += 1
        
        common_set.add(color)
print(len(was), color_gen_cnt + len(was))

        