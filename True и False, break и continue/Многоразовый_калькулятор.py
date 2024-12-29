while True:
    num = int(input())
    op = input()
    if op == 'x':
        print(num)
        break
    else:
        if op == '!':
            if num < 0:
                continue
            elif num == 0:
                print(1)
            else:
                sm = 1 
                for i in range(2, num + 1):
                    sm *= i 
                print(sm)
        
        else:
            n = int(input())
            if op == '+':
                print(num + n)
            elif op == '-':
                print(num - n)
            elif op == '*':
                print(num * n)
            elif op == '/':
                if n == 0:
                    continue
                else:
                    print(num // n)
            elif op == '%':
                if n == 0:
                    continue
                else:
                    print(num % n)
            
            
                