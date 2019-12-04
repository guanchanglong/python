#name="adA loveLace"
#print(name.title())#title函数可以将每个字符串开头第一个字母大写输出
#print(name.upper())#upper函数可以将字符串中的每个字母都大写输出
#print(name.lower())#lower函数可以将字符串中的每个字母都小写输出

#first_name="ada"
#last_name="lovelace"
#full_name=first_name+" "+last_name#可以使用（+）来合并字符串，这种合并字符串的方式称为拼接
#print(full_name)
#print("hello,"+full_name.title()+"!")
#message="Hello,"+full_name.title()+"!"
#print(message)

#print("python")
#print("language:\nPython\nC\nJavaScript")#跟C语言类似（\n）是python中的换行

#favorite_language="python "
#print(favorite_language.rstrip())#rstrip函数可以消除字符串末尾的空格然后输出该字符串
#print(favorite_language)#但不用rstrip函数，再次输出该变量时，它还是存在空格的，说明rstrip函数只是暂时消除字符串中的空格
#favorite_language="python  "
#favorite_language=favorite_language.rstrip()#可以创建一个新的变量来存储去掉空格的字符串
#print(favorite_language)

favorite_language="python"
print(favorite_language.lstrip())