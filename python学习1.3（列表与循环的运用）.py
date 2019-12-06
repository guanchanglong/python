#a=['x','y','z']
#for a in a:         #for循环后面的冒号不要忘记
#for循环每次输出列表的一个元素
#    print(a)#缩进很重要，忘记缩进和不必要的缩进都会造成错误

#a=[1,2,3,4,5,6]
#for b in range(1,6):    #range函数
#    print(b)

#num=list(range(1,6))#函数list将range的结果直接转化为列表，生成一个数字列表
#print(num)

#num1=list(range(50 , 100 , 2))
               #开始  结束  步长
#print(num1)

#squares=[]
#for a in range(1,11):
#    square=a**2
#    squares.append(square)
#    print(squares)
#上面的代码等价于:
#squares=[a**2 for a in range(1,11)]
#print(squares)

#d=[1,2,3,4,5,6,7,8,9,10]
#print(min(d))   #min函数的作用是找到最小值
#print(max(d))   #max函数的作用是找到最大值
#print(sum(d))   #sum函数的作用是求和

#a=[]
#for i in range(1,10000000):
#    a.append(i)
#    print(sum(a))

#a=['d','c','b','a','x','y','z']
#print(a[0:2])#a[0:3]与a[:3]等价
#生成0到2的列表元素
#print(a[2:3])
#生成第3个列表元素
#print(a[-4:])

a=['a','b','c','d','e','f','g']
b=a
print(b)
for b in b:
    print(b)