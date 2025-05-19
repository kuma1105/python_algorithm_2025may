for _ in range(int(input())):
    stk = []
    isVPS = True
    for ch in input():
        if ch == '(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                # stk가 비었고 닫는 괄호가 들어왔을 때
                isVPS = False
                break
    if stk:
        isVPS = False
    
    print('YES' if isVPS else 'NO')