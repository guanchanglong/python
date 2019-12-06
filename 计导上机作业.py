#x = input()
#x = list(x)
#a = int(x[0])
#b = int(x[1])
#c = int(x[2])
#if c == 0:
#    if b == 0:
#        print(a)
#    else:
#        print("%d%d" % (b, a))
#else:
#    print("%d%d%d" % (c, b, a))

#n=int(input())
#i=0
#while i<=n:
#    x=3**i
#    print("pow(3,%d)=%d"%(i,x))
#    i = i + 1

N=int(input())
sum = 0
a, b = 2, 1
while N>0:
    float(sum)
    sum = sum + (a/b)
    a = a + b
    b = a - b
    N=N-1
print("%.2f"%sum)

