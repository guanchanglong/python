#age=18
#message="Happy"+ " "+str(age)+"rd Birthday"#str函数的作用是将不是非字符串值表示为字符串
#print(message)

#print(0xA+0xB)#'0x’前缀表示十六进制，0xA 0xB分别表示10和11,故输出21

#bicycles=['trek','cannodale','redline','specialized']#python中的列表
#print(bicycles)
#print(bicycles[0])#与C语言中的数组类似
#print(bicycles[0].title())
#print(bicycles[-1])#-1可以指向列表中的最后一个元素
#message="My first bicycle was a"+bicycles[0].title()+"."
#print(message)
#print("message")#加了""后这样是输出字符串类型的数据

#motorcycles=['honda','yamaha','suzuki']
#print(motorcycles)
#motorcycles[0]='ducati'#将列表中的一个元素修改
#print(motorcycles)
#motorcycles.append('ducati')
#print(motorcycles)

#motorcycles=[]
#motorcycles.append('honda')#append函数的作用是在列表中创建新的元素
#motorcycles.append('yamaha')
#motorcycles.append('suzuki')
#print(motorcycles)

#motorcycles=['honda','yamaha','suzuki']
#motorcycles.insert(0,'ducati')#insert函数的作用是在列表中插入新的元素，插入后其位置后面的元素往后移
#书写形式为.insert(插入元素位置，待插入的元素）
#print(motorcycles)

#motorcycles=['honda','yamaha','suzuki']
#print(motorcycles)
#del motorcycles[0]#del函数的作用是删除列表中的元素
#print(motorcycles)

#motorcycles=['honda','yamaha','suzuki']
#print(motorcycles)
#popped_motorcycles=motorcycles.pop()#此处就将列表末尾的元素删除，并将它的值赋给了另一个变量
#函数pop可删除列表末尾的元素，并且让你能够接着使用它
#print(motorcycles)
#print(popped_motorcycles)

#motorcycles=['honda','yamaha','suzuki']
#last_owned=motorcycles.pop()
#print("The last motorcycles I owned was a "+last_owned.title()+".")

#motorcycles=['honda','yamaha','suzuki']
#first_owned=motorcycles.pop(0)#pop函数也可以直接删除列表中指定的对象，此时该元素已经不在列表中了
#print('The first motorcycles I owned was a '+first_owned.title()+'.')

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive)#remove函数用法与pop函数类似，只不过remove函数是删除指定了值的元素
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")