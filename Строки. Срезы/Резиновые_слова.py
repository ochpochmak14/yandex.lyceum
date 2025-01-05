s = input()
if len(s) % 2 != 0:
    curr = len(s) // 2
    step = 0
    spaces2 = 1 
    for spaces in range(len(s) // 2, -1, -1):
        if step == 0:
            print(spaces * ' ', s[curr], spaces * ' ', sep='')
            step += 1 
        else:
            print(spaces * ' ', s[curr - step], spaces2 * ' ', s[curr + step], spaces * ' ', sep='')
            step += 1
            spaces2 += 2 
else:
    ok = True
    spaces2 = 2
    curr_spaces = (len(s)) // 2 - 1
    curr_ind = len(s) // 2 - 2
    print((len(s) // 2 - 1) * ' ', s[(len(s) // 2 - 1):len(s) // 2 + 1:], (len(s) // 2 - 1) * ' ', sep='')
    if len(s) == 2:
        ok = False
    if ok:
        for spaces in range(len(s) // 2 - 2, -1, -1):
            print(spaces * ' ', s[curr_ind], spaces2 * ' ', s[len(s) - 1 - curr_ind], spaces * ' ', sep='')
            spaces2 += 2 
            curr_ind -= 1 
            
            
            
    