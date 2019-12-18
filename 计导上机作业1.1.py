#统计并输出字符串中小写元音字母的个数
#x=input()
#a1=x.count('a')
#e1=x.count('e')
#i1=x.count('i')
#o1=x.count('o')
#u1=x.count('u')
#y=a1+e1+i1+o1+u1
#print(str(y))

#jmu-python-涨工资
#a = input()
#a=a.split(" ")
#a=[eval(a[i]) for i in range(len(a))]
#for i in range(len(a)):
#    if a[i]<5000:
#        a[i]=a[i]*1.5
#print(*a)

#分析活动投票情况
#a=input()
#a=a.split(",")
#b=[]
#a=[str(a[i]) for i in range(len(a))]
#a1 = a.count('6')
#e1 = a.count('7')
#i1 = a.count('8')
#o1 = a.count('9')
#u1 = a.count('10')
#if a1==0:
#    b=b+[6]
#if e1==0:
#    b=b+[7]
#if i1==0:
#    b=b+[8]
#if o1==0:
#    b=b+[9]
#if u1==0:
#    b=n+[10]
#print(" ".join('%d' %i for i in b))

#列表去重
#list1=eval(input())
#list2=[]
#for l in range(len(list1)):
#    flag=1
#    for m in range(1,l):
#        if list1[l]==list1[m]:
#            flag=0
#    if flag==1:
#        list2.append(list1[l])
#print(' '.join([str(list2[l]) for l in range(len(list2))]))

#字典合并
#a_dict=dict(eval(input()))
#b_dict=dict(eval(input()))
#c_dict={}
#d = {k:v for d in [a_dict, b_dict] for k,v in d.items()}
#for k,v in a_dict.items():
#    for j,l in b_dict.items():
#        if k==j:
#            c_dict[j] =l+v
#d.update(c_dict)
#print(d)
a_dict=dict(eval(input()))
b_dict=dict(eval(input()))
for x in b_dict:
    if x not in a_dict:
        a_dict[x]=b_dict[x]
    else:
        a_dict[x]+=b_dict[x]
print("{",end="")
a=[x for x in a_dict.keys() if type(x)==type(1)]
b=[x for x in a_dict.keys() if type(x)==type('a')]
a.sort()
b.sort()
c=0
n=len(a_dict)
for i in a+b:
    c+=1
    if type(i)==type(1):
        print("{}:{}".format(i,a_dict[i]),end='')
    else:
        print('"{}":{}'.format(i,a_dict[i]),end='')
    if c!=n:
        print(',',end='')
print("}")