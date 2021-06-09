import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    ps = sys.stdin.readline().rstrip()
    
    stack = []
    pop_exception = False

    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) == 0:    
                pop_exception = True
                break;
            else:
                stack.pop()
    
    if pop_exception:
        print("NO")
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
        
