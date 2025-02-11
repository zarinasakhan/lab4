def my_list(N):
    for i in range(1, N+1):
        yield i**2
N=int(input("N="))
print(list(my_list(N)))