n=int(input("Enter No."))
a=0
b=1
print(a)
print(b)
i=2
x=()
while(i<=n):
    c=a+b
    a=b
    b=c
    i=i+1
    x.append(c)
print(x[-1])


