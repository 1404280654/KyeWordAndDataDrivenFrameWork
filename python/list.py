
#简单数组
sample_list = ['a',1,('a','b')]

#Python 列表操作

sample_list = ['a','b',0,1,3]


#在列表中插入一个值

sample_list[0:0] = ['sample value']

#得到列表的长度

list_length = len(sample_list)

#列表遍历

for element in sample_list:
    print(element)

#Python 列表高级操作/技巧

#产生一个数值递增列表

num_inc_list = range(30)

#will return a list [0,1,2,...,29]

#用某个固定值初始化列表

initial_value = 0

list_length = 5

sample_list = [ initial_value for i in range(10)]

sample_list = [initial_value]*list_length

# sample_list ==[0,0,0,0,0]

#附：python内置类型

#1、list：列表（即动态数组，C++标准库的vector，但可含不同类型的元素于一个list中）

a = ["I","you","he","she"] #元素可为任何类型。

#下标：按下标读写，就当作数组处理

#以0开始，有负下标的使用

#0第一个元素，-1最后一个元素，

#-len第一个元 素，len-1最后一个元素

#取list的元素数量

len(list) #list的长度。实际该方法是调用了此对象的__len__(self)方法。

#创建连续的list

L = range(1,5) #即 L=[1,2,3,4],不含最后一个元素

L = range(1, 10, 2) #即 L=[1, 3, 5, 7, 9]

#list的方法
"""
L.append(var) #追加元素

L.insert(index,var)

L.pop(var) #返回最后一个元素，并从list中删除之

L.remove(var) #删除第一次出现的该元素

L.count(var) #该元素在列表中出现的个数

L.index(var) #该元素的位置,无则抛异常

L.extend(list) #追加list，即合并list到L上

L.sort() #排序

L.reverse() #倒序

list 操作符:,+,*，关键字del

a[1:] #片段操作符，用于子list的提取

[1,2]+[3,4] #为[1,2,3,4]。同extend()

[2]*4 #为[2,2,2,2]

del L[1] #删除指定下标的元素

del L[1:3] #删除指定下标范围的元素
"""


"""
dictionary的方法

D.get(key, 0) #同dict[key]，多了个没有则返回缺省值，0。[]没有则抛异常

D.has_key(key) #有该键返回TRUE，否则FALSE

D.keys() #返回字典键的列表

D.values()

D.items()

D.update(dict2) #增加合并字典

D.popitem() #得到一个pair，并从字典中删除它。已空则抛异常

D.clear() #清空字典，同del dict

D.copy() #拷贝字典

D.cmp(dict1,dict2) #比较字典，(优先级为元素个数、键大小、键值大小)
"""

#第一个大返回1，小返回-1，一样返回0

#dictionary的复制

dict1 = dict #别名

dict2=dict.copy() #克隆，即另一个拷贝。



#可以用list的 [],:操作符提取元素。就是不能直接修改元素。

str = "Hello My friend"

#字符串是一个整 体。如果你想直接修改字符串的某一部分，是不可能的。但我们能够读出字符串的某一部分。子字符串的提取

str[:6]

#字符串包含 判断操作符：in，not in

#“He” in str

#“she” not in str
"""
string模块，还提供了很多方法，如

S.find(substring, [start [,end]]) #可指范围查找子串，返回索引值，否则返回-1

S.rfind(substring,[start [,end]]) #反向查找

S.index(substring,[start [,end]]) #同find，只是找不到产生ValueError异常

S.rindex(substring,[start [,end]])#同上反向查找

S.count(substring,[start [,end]]) #返回找到子串的个数

S.lowercase()

S.capitalize() #首字母大写

S.lower() #转小写

S.upper() #转大写

S.swapcase() #大小写互换

S.split(str, ‘ ‘) #将string转list，以空格切分

S.join(list, ‘ ‘) #将list转string，以空格连接
"""

#处理字符串的内置函数

len(str) #串长度


max('abcxyz') #寻找字符串中最大的字符

min('abcxyz') #寻找字符串中最小的字符
