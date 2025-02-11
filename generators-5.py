def back(n):
    for i in range(n,0,-1):
        yield i
n=int(input("n="))
print(list(back(n)))