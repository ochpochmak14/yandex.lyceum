n = int(input())

cnt = 1
row_cnt = 0
while cnt <= n:
    cnt2 = 0
    while cnt2 <= row_cnt and cnt <= n:
        print(cnt, end=' ')
        cnt += 1
        cnt2 += 1
    print() 
    row_cnt += 1
    
    
            