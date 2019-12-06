car=[1323,3534,22314,6354,51232,45345]
cars=['Cadassds','Asdas','Bdfgfg','sdsd','asassx','cdcdcd']
cars.sort()#如果是字符的话，则按字符串开头第一个字母的ASCLL码的大小排列
car.sort()#sort函数可以将列表内的元素按从小到大的顺序排列，该排序对列表的修改是永久性的
print(cars)
print(car)
car=[123,4543,5443,67556,76456,4234,45345]
print(sorted(car))#sorted函数的作用是对列表进行临时排序
print(car)
car.reverse()#reverse的作用是将列表中的元素的排列顺序反转过来，即与原来的排列顺序相反，对列表的修改也是永久性的
print(car)
print(len(car))#len函数的作用是显示列表中有多少个元素

