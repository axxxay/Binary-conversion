for _ in range(int(input())):
    n= int(input())
    s = ""
    if 1<=n<=100:
        b = bin(n)
        for i in str(b)[2:]:
            if i == "0":
                s += "1"
            else:
                s += "0"
        s = int(s,2)
    else:
        s = "wrong input"
    print(s)