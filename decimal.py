def dec(n):
    if n>1:
        dec(n//2)
    print(n%2,end='')
n=int(input())
a=dec(n)
print(a)
