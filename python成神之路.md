 #if的用法
> 简单if语句
```python
if conditional_test:
    do something 满足if后所跟函数的条件后执行之后的缩进代码
```
## 例题
假设有一个表示某人年龄的变量，而你想知道这个人是否符合投票的年龄，可使用
如下代码：
```python
age = 19
❶ if age >= 18:
❷ print("You are old enough to vote!")

```
当中python会检查age的值是否大于18，大于就会执行所进的代码，若小于就会跳过这串代码。
# if-else语句
```python
 age = 17
❶ if age >= 18:
 print("You are old enough to vote!")
 print("Have you registered to vote yet?")
❷ else:
 print("Sorry, you are too young to vote.")
 print("Please register to vote as soon as you turn 18!")
```
其中age函数如果满足if后面的条件则执行if后的缩进代码；若不满足则执行else后的缩进代码
### 结果如下
```python
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```
## if-elif-else结构
## 例题
在现实世界中，很多情况下需要考虑的情形超过两个。例如，来看一个根据年龄段
收费的游乐场：
4岁以下免费；
4～18岁收费25美元；
18岁（含）以上收费40美元。
```python
 age = 12
❶ if age < 4:
 print("Your admission cost is $0.")
❷ elif age < 18:
 print("Your admission cost is $25.")
❸ else:
 print("Your admission cost is $40.")
```
❶处的if 测试检查一个人是否不满4岁。如果是，Python就打印一条合适的消息，
并跳过余下测试。❷处的elif 代码行其实是另一个if 测试，仅在前面的测试未通
过时才会运行。在这里，我们知道这个人不小于4岁，因为第一个测试未通过。如果
这个人未满18岁，Python将打印相应的消息，并跳过else 代码块。如果if 测试和
elif 测试都未通过，Python将运行❸处else 代码块中的代码。
> 为了让代码简洁可不在if-elif-else 代码块中打印门票价格，而只在其中设
置门票价格，并在它后面添加一个简单的函数调用print() ：
```python
age = 12
 if age < 4:
❶ price = 0
 elif age < 18:
❷ price = 25
 else:
❸ price = 40
❹ print(f"Your admission cost is ${price}.")
```
判断age函数，age不满足if但是满足elif，则执行elif下的缩进代码最后print输出值是25


## 使用多个elif代码块
>可根据需要使用任意数量的elif 代码块。例如，假设前述游乐场要给老年人打
折，可再添加一个条件测试，判断顾客是否符合打折条件。下面假设对于65岁
（含）以上的老人，可半价（即20美元）购买门票：
```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age <65:
    price = 40
else:
    price = 20
    print ("your admission cost is $(price).")
           
```
## 省略else代码
将上述代码块中的
```python
else:
    price = 20
```
修改为
```python
elif age >=65:
    price = 20
```
即可

# 使用if处理列表
```python
requeted_toppongs = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppongs:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
```
输出结果：
```python
Adding mushrooms.
Adding green peppers.
Adding sxtea cheese.

Finished marking your pizza! # 上述代码是简单的for循环
```
如果披萨店的青椒用完了，该如何处理，此时可以用if补救，在for循环中包含if语句
```python
requested_toppings = ['','','']
```
# 第六章 ： 字典
##使用字典
`alie_0.py`
```python
alie_0 = {'color':'green';'points':5}
print(alie_0[color])
print(alie_0[points])
```
## 访问字典中的值
要获取与键相关联的值，可依次指定字典名和放在方括号内的键
```python
alie_0 = {'color':'green'}
print(alie_0[color])
```
这将返回字典alien_0 中与键'color' 相关联的值：
`运行结果`
```python
green
```
字典中可以包含任意数量的键值对
`alie_0.py`中包含两组键值对
```python
alie_0 = {'color':'green';'points':5}
print(alie_0[color])
print(alie_0[points])
```
其中就包含着代表颜色的`color`，和分数的`points`
现在，你可访问外星人alien_0 的颜色和分数。如果玩家射杀了这个外星人，就可
以使用下面的代码来确定应获得多少分
```python
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
```
上述代码首先定义了一个字典。然后，从这个字典中获取与键'points' 相关联的
值，并将这个值赋给变量new_points 。接下来，将这个整数转换为字符
串，并打印一条消息，指出玩家获得了多少分：
```python
you just earned 5 poiints
```
## 添加键值对
字典是动态结构能随时添加键值对
`alien_0.py`
```python
alien_0 = {'color':'green';'points':5}
print(alien_0)
alien_0['x_zhou'] = 0
alien_0['y_zhou'] = 25
print(alien_0) 
```
上述代码在`alien_0`的字典中添加了x轴和y轴
`打印结果为`
```python
{'color': 'green', 'points': 5, 'x_zhou': 0, 'y_zhou': 25}
```
注意添加键值的时候是`字典名称['键值名称'] = 常量（或变量）`
在创造字典时时`字典名称 = {'键值名称'：常量(或变量)}`
# 创造一个空字典
以`alien.py`为例
```python
alien = {}
alien['color'] = 'blue'
alien['points'] = 5
print(alien)
```
运行结果为
```python
{'color': 'blue', 'porint': 5}
```
使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时，通常需
要先定义一个空字典。
# 修改字典里的值
要修改字典中的值，可依次指定字典名、用方括号括起的键，以及与该键相关联的
新值。
以`alien_1.py`为例
```python
alien_1 = {'color':'green'}
print(f"the alien_1 color is:{alien_1['color']}")
alien_1['color'] = 'blue'
print(f"the alien_1 new color is : {alien_1['color']}")
```
注意打印字典时print（f"字符串alien_1['color']"）

开头括号中一定要有f
`运行结果`
```python
the alien_1 color is:green
the alien_1 new color is : blue
```
来看一个更有趣的例子，对一个能够以不同速度移动的外星人进行位置跟踪。为
此，我们将存储该外星人的当前速度，并据此确定该外星人将向右移动多远：
`alien_2.py`
```python
alien_2 = {'x_zhou':0,'y_zhou':25,'speed':'medium'}#当前alien的位置
print(f"Original position: {alien_2['x_zhou']}")
if alien_2['speed'] == 'slow':
    x_zhouspeed = 1
elif alien_2['speed'] == 'medium':
    x_zhouspeed = 2
else:
    x_zhouspeed = 3
alien_2['x_zhou'] = alien_2['x_zhou'] + x_zhouspeed
print(f"the new position: {alien_2['x_zhou']}")
```
## 有问题记得回来看看运行结果为3 答案为2
# 删除键值
以`alien_3.py`为例
```python
alien_3 = {'color':'green','priont':5}
print(alien_3)
del alien_3['color']
print(alien_3)
```
运行结果
```python
{'color': 'green', 'priont': 5}
{'priont': 5}
```
注意：消失的键值会永远消失
# 由类似对象组成的字典
以`favourite_languages.py`为例
```python
favourite_languages = {
    'jun':'python',
    'chen':'c',
    'dunck':'java',
    'junke':'php',
}
languages = favourite_languages['chen'].title()
print(f"chen's favourite languages is {languages}")
```
`运行结果`
```python
chen's favourite languages is C
```
# 使用get()来访问值
方法get() 的第一个参数用于指定键，是必不可少的；第二个参数为指定的键不存
在时要返回的值，是可选的：
`alien_4.py`
```python
alien_4 = {'color':'green','priont':'5'}
priont_value = alien_4.get('priont','on priont value')
print(priont_value)
```
# 遍历字典
一个python字典可能只包括几个键值对，也可能包含包含几百万个键值对。

鉴于字典可能包含大量数据，python支持对字典进行遍历，字典可用于以各种方式储存信息，因此有多种遍历方式：可遍历字典的所有键值对，也可仅遍历 键或键。
## 遍历所有键值对
探索各种遍历方法前，先来看一个新字典，它用于存储有关网站用户的信息。
下面的字典存储一名用户的用户名、名和姓：
`username.py`
```python
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
```
`运行结果`
```python
key: username
value: efemi

key: first
value: enrico

key: last
value: fermi
```
`favourite_languaged.py`
```python
favourtie_languages = {
    'jen':'pytoon',
    'sarah':'c',
    'phll':'ruby',
}
for name,languages in favourtie_languages.items(): #代码让python遍历字典中的每个键值对，并将键赋给变量name，将值赋给变量languages
    print(f"{name.title()}'s favorite languages is {languages.title()}")
    
```
`运行结果`
```python
Jen's favorite languages is Pytoon
Sarah's favorite languages is C
Phll's favorite languages is Ruby
```
## 遍历字典中的所有键
在不需要使用字典中的值时，方法keys()很有用。下面来遍历字典
`favourite_languaged.py`
```python
favourtie_languages = {
    'jen':'pytoon',
    'sarah':'c',
    'phll':'ruby',
}
for name in  favourite_language.keys():#这一处代码让python提取字典favourite_languages中的所有的键，并依次将他们赋给变量name。输出列出了每个被调查的名字
    print(name.title())
```
```python
jen
sarah
phll
```
遍历字典时，会默认遍历所有的键。因此，如果将上述代码中：
```python
for name in favourite_languages:
```
替代为：
```python
for name in favourite_languages.keys()
```
输出将不变。
显式地使用方法keys() 可让代码更容易理解，你可以选择这样做，但是也可以省
略它。
在这种循环中，可使用当前键来访问与之相关联的值。下面来打印两条消息，指出
两位朋友喜欢的语言。像前面一样遍历字典中的名字，但在名字为指定朋友的名字
时，打印一条消息，指出其喜欢的语言：
文件`favourite_languages2.py`
```python
favourite_languages ={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil','sarah']#创建了一个列表，其中包含收到打印消息的朋友。
for name in favourite_languages2.keys():#在循环中，打印每个人的名字，并检查当前的名字是否在列表friend中
    print(f"Hi {name.title()}.")
    if name in friends:#如果在，就打印一句特殊的问候语，其中包含这位朋友的语言。为获悉朋友喜欢的语言，我们使用了字典名，并将 变量name的当前值作为键
        language2 = favourite_languages2[name].title()
        print(f"\t{name.title()},I see you love {languages2}!")
```
```python
Hi Jen.
Hi Sarah.
 Sarah, I see you love C!
Hi Edward.
Hi Phil.
 Phil, I see you love Python!
```
还可以用keys()确定某个人是否接受了调查。下面的代码确定phil是否接受了调查：
`favourite_langyages3.py`
```python
   favorite_languages3 = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
if 'erin' not in favorite_languages3.keys():#此处代码只是核实'erin'是否包含在这个列表中，如果不包含在`favourite_languages3`中则打印出下面这句话
    print("Erin, please take our poll!")
```
`结果为：`
```python
Erin, please take our poll!
```
方法keys()并非只是用于遍历：实际上，它返回一个列表，其中包含字典中的所有键。因此上述注释处代码只能核实'erin'，是否包含在上边的列表
## 按特定顺序遍历字典中的所有键
要以特定的顺序返回元素：
> 在for的循环语句中对键进行返回的排序。因此，可以使用~soted()~获得按特定顺序排列的副本
```python
favourite_languages5 = {
    'jen':'python',
    'sarach':'c',
    'phil':'python',
}
for name in sorted(favourite_languages5.keys()):
    print(f"{name.title()},thank you takling the poll.")
```
```python
Jen,thank you takling the poll.
Phil,thank you takling the poll.
Sarach,thank you takling the poll.
```
这条for语句类似于其他for语句，不同之处就是对方法`dictionary.keys()`的结果调用函数`soted()`。这让python列出的字典中所有的键，并在遍历前对这个列表进行排序。输出表迷宫，按顺序显示了所有被调查者的名字
## 遍历字典中的所有值
如果主要对字典包含的值感兴趣，可使用方法values() 来返回一个值列表，不包
含任何键。例如，假设我们想获得一个列表，其中只包含被调查者选择的各种语
言，而不包含被调查者的名字，可以这样做：
`favourite_languages5.py`
```python
favourite_languages5 = {
    'jen':'python',
    'sarach':'c',
    'phil':'python',
}
print("the following languages have been mentioned:")
for language3 in favourites_languages5.values():
    print(languages.title())
```
`运行结果：`
```python
The following languages have been mentioned:
Python
C
Ruby
Python
```
这种做法提取字典中的值，但是没有考虑重复。涉猎很少时，还可以使用但是如果被调查者很多，最终的列表会出现包含大量的重复项，为剔除重复项可以使用集合（set）。集合中每个每个元素都是独一无二的：
```pytohn
favourite_languages7 = {
    'jen':'python',
    'sarah':'c',
    'phil':'python'
}
print("the following languageas have been mentiond:")
for languages7 in set(favourite_languages7.values()):
    print(languages7.title())
```
```python
The following languages have been mentioned:
Python
C
```
注意：可以使用一对花括号直接创造集合，并在其中用逗号分隔元素：
```python
>>>languages8 = {'python','ruby','python','c'}
>>>languages8
{'ruby','python','c'}
```
集合和字典很容易混淆因为他们都是一对花括号定义。当花括号没有键值对时，定义的很可能是集合。不同于列表和字典，集合不会以特定的顺序存储元素。
# 嵌套
有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为
嵌套 。你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。正如
下面的示例将演示的，嵌套是一项强大的功能。
##  字典列表
alien_0中包含一个外星人的各种信息，但是无法存储第二个外星人的信息，更别说屏幕上全部的外星人的信息了，如何管理外星人
`alien2.0_py`
```python
alien_0 = {'color':'grenn','points':5}
alien_1 = {'color':'red','points':5}
alien_2 = {'color':'yellow','points':5}
alien_plus = {alien_0,alien_1,alien_2}
for alien in alien_plus:
    print(alien)
```
```python
{'color':'green','points':5}
{'color':'red','points':5}
{'color':'yellow','points':5}
```
为更符合实际情况，外星人不只是三个，且每个外星人都使用代码自动生成的。
在下面示例中使用range()生成了30个外星人：
`alien_por.py`
```python
#创建一个用于存储外星人的空列表。
aliens = []
#创建30个绿色外星人
for alien_number in range(30):#range()返回一系列数，其中唯一的用处就是告诉python要重复多少次循环
    new_aliens = {'color':'green','points':5,'slow'}#每次重复会创建alien附加在列表aliens末尾
    aliens.append(new_alien)
    #显示前5个外星人。
for alien in aliens[:5]:#打印列表的长度，证明确实窗键了30个外星人
    print(alien)
print("...")
#显示创建了多少个外星人。
print(f"Total number of aliens:{len(aliens)}")        
```
进阶版`aliens_por.py`
想象一下，可能随着游戏的进行，有
些外星人会变色且加快移动速度。必要时，可使用for 循环和if 语句来修改某些
外形人的颜色。例如，要将前三个外星人修改为黄色、速度为中等且值10分，可这
样做：
```python
aliensx = []
for alien_num in range(30):
    xin_aliens = {'color':'red','points':5,'speed':'slow'}
    aliensx.apppend(xin_aliens)
for alienx in aliensx[:3]:
        if alien['color'] == 'grenn':
            alien['color'] = 'yellow'
            alien['speed'] = 'fast'
            alien['points'] = 10
for alien in aliensx[:3]:
    print(alien);
print(".......")
```
可进一步扩展这个循环，在其中添加一个elif 代码块，将黄色外星人改为移动速
度快得分值15分的红色外星人，如下所示（这里只列出了循环，而没有列出整个程
序）`有出入以代码为准`：
`aliens_por_max.py`
```python
aliensx_0 =[]
for alien_num0 in range(10):
    xin_alien_0 = {'color':'green','points':5,'speed':'slow'}
    aliensx_0.append(xin_alien_0);
for alieno in aliensx_0[:2]:
    if alieno['color'] == 'green':
        alieno['color']='red'
        alieno['points'] = '100'
        alieno['speed'] = 'fast'
    elif alieno['color'] == 'red':
        alieno['color'] = 'yellow'
        alieno['points'] = '12'
        alieno['speed'] = 'min';
for alienp in aliensx_0[0:10]:
    print(alienp);
```
`结果为：`
```python
{'color': 'red', 'points': '100', 'speed': 'fast'}
{'color': 'red', 'points': '100', 'speed': 'fast'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
```
## 在字典中存储列表
在下面的示例中，存储了比萨的两方面信息：外皮类型和配料列表。配料列表是一
个与键'toppings' 相关联的值。要访问该列表，我们使用字典名和
键'toppings' ，就像访问字典中的其他值一样。这将返回一个配料列表，而不是
单个值：
`pizza_1.py`
```python
# 存储所点比萨的信息。
❶ pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }
 # 概述所点的比萨。
# 存储所点比萨的信息。
❷ print(f"You ordered a {pizza['crust']}-crust pizza "
 "with the following toppings:")
❸ for topping in pizza['toppings']:
 print("\"f+topping)
```
首先创建一个字典，其中存储了有关顾客所点比萨的信息（见❶）。在这个字典中，
一个键是'crust' ，与之相关联的值是字符串'thick' ；下一个键
是'toppings' ，与之相关联的值是一个列表，其中存储了顾客要求添加的所有配
料。制作前，我们概述了顾客所点的比萨（见❷）。如果函数调用print() 中的字
符串很长，可以在合适的位置分行。只需要在每行末尾都加上引号，同时对于除第
一行外的其他各行，都在行首加上引号并缩进。这样，Python将自动合并圆括号内
的所有字符串。为打印配料，编写一个for 循环（见❸）。为访问配料列表，使用
键'toppings' ，这样Python将从字典中提取配料列表。
`运行结果：`
```python
You ordered a thick-crust pizza with the following toppings:
 mushrooms
 extra cheese
```
每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。在本
章前面有关喜欢的编程语言的示例中，如果将每个人的回答都存储在一个列表中，
被调查者就可选择多种喜欢的语言。在这种情况下，当我们遍历字典时，与每个被
调查者相关联的都是一个语言列表，而不是一种语言；因此，在遍历该字典的for
循环中，我们需要再使用一个for 循环来遍历与被调查者相关联的语言列表：
`favoutie_language_10,py`
```python
❶ favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
❷ for name, languages in favorite_languages.items():
 print(f"\n{name.title()}'s favorite languages are:")
❸ for language in languages:
 print(f"\t{language.title()}")
```
如你所见，现在与每个名字相关联的值都是一个列表（见❶）。请注意，有些人喜欢
的语言只有一种，而有些人有多种。遍历字典时（见❷），使用变量languages 来
依次存储对字典中每个值的引用，因为我们知道这些值都是列表。在遍历字典的主
循环中，使用了另一个for 循环（见❸）来遍历每个人喜欢的语言列表。现在，每
个人想列出多少种喜欢的语言都可以：
`运行结果：`
```python
Jen's favorite languages are:
 Python
 Ruby
Sarah's favorite languages are:
 C
Edward's favorite languages are:
 Ruby
 Go
Phil's favorite languages are:
 Python
 Haskell
```
# 用户输入和whille循环
## 函数input的工作原理
`parrot.py`
```pyhon
message = input("Tell me somrhing,and I will repeaat it back to you :"
print (message))
```
注意：Sublime Text等众多编辑器不能运行提示用户输入的程序。你可以使用Sublime Text 来编写提示用户输入程序，但是必须在终端运行他们。
### 编写清晰的程序
`greeter.py`
```python
name = input("please rnter your name:")
print(f"\nhello,(name)!")
```
`运行结果`
```python
Tell me something,and I will repeat it back to you:0
0
please enter your name:0

hello,0!
```
有时候，提示可能超过一行。例如，你可能需要指出获取特定输入的原因。在这种情况下，可能提示赋给一个变量，再将该变量传递给函数inpu().这样，即便超过一行，input()语句也会非常清晰。
`greeter.py`
```python
prompt = "if you tell us who you are,we can personalize the messgae you see."
prompt += "\nWhat is your fisrt name?"
name = input(prompt)
print(f"\nHello,{names}!")
```
```python
if you tell us who you are ,we can personalize the messages you see.
What is your first name?0

Hello,0
```
### 使用int()来获取数值输入
使用函数input()时，python将用户输入解读为字符串。请看下面让用户输入年龄的解释器会话：
```python
>>> age = input("How old you?")
How old are you?21
>>>age
'21'
```
用户输入的是数21，但我们请求python提供变量age的值时，它返回的是‘21’————用户输入数值的字符串表示。我们怎么知道python将输入解读成了字符串？
因为这个数用括号括起了。如果只想打印输入，这一点问题都没有：但如果试图将输入作为数来使用，就会引发错误：
```python
 >>> age = input("How old are you? ")
 How old are you? 21
❶ >>> age >= 18 
 Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
❷ TypeError: unorderable types: str() >= int()
```
试图将输入用于数值比较时（见❶），Python会引发错误，因为它无法将字符串和整
数进行比较：不能将赋给age 的字符串'21' 与数值18 进行比较（见❷）。

为解决这个问题，可使用函数int() ，它让Python将输入视为数值。函数int()
将数的字符串表示转换为数值表示，如下所示：
```python
 >>> age = input("How old are you? ")
 How old are you? 21
 >>> age = int(age)
 >>> age >= 18
 True
```
在本例中，用户根据提示输入21后。python将这个数解读为字符串随后
函数int()将数的字符串转化成 数值表示，这样就可以将变量age同18比较大小 ，测试结果为ture
如何在实际程序中使用int()呢？请看下面的程序，它判断一个人是否满足坐过山车的身高要求：
`rollercoaster.py`
```python
height = input("How tall are you,in inches?")
height = int(hight)
if height >= 48:
    print("\nYou're tall enough to ride")
else:
    print("\nYou'll be able to ride when you're a little older.")    
```
在此程序中为何可以将height同48进行比较呢？因为在比较前，hight = int(height)将输入转换成了数值表示。如果输入的数字大于或等于48，就指出用户满足身高条件：
### 求模运算符%
略//小学生都会自己不会，证明你是九年义务教育漏网之鱼
## while循环
### 使用while循环
可使用while循环来数数。列如，下面的while循环从1数到5：
`counting.py`
```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```
 在第一行，将1 赋给变量current_number ，从而指定从1开始数。将接下来的
while 循环设置成：只要current_number 小于或等于5，就接着运行这个循
环。循环中的代码打印current_number 的值，再使用代码current_number
+= 1 （代码current_number = current_number + 1 的简写）将其值加
1。
只要满足条件current_number <= 5 ，Python就接着运行这个循环。因为1小于
5，所以Python打印1 并将current_number 加1，使其为2；因为2小于5，所以
Python打印2 并将current_number 加1，使其为3；依此类推。一旦
current_number 大于5，循环就将停止，整个程序也将结束：  
```python
1
2
3
4
5
```
### 让用户选择何时退出
可以使用while 循环让程序在用户愿意时不断运行，如下面的程序parrot.py所
示。我们在其中定义了一个退出值 ，只要用户输入的不是这个值，程序就将接着运
行：
`parrot.py`
```python
prompt = "\nTell me somethin"
prompt = "\nEntter 'quit' to end"
message = ""
while message != 'qiut':
    message = input(prompt)
    print(message)
```
`结果如下：`
```python
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
quit
```
以上代码并不完美其中它将单词‘quit’也作为一条消息打印出来
可以用一条简单的if语句来修复
```python
prompt = "\nTell me somethin"
prompt = "\nEntter 'quit' to end"
message = ""
while message != 'qiut':
    message = input(prompt)
    if message != 'quit'
    print(message)
```
`打印结果为：`
```python
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```
## 使用标志
`active.py`
```python
 prompt = "\nTell me something, and I will repeat it back to you:"
 prompt += "\nEnter 'quit' to end the program. "
 active = True#指定一个变量active设置为ture，让程序为最初始的活动状态
 while active:#当active不在为ture，循环就会停止
    message = input(prompt)
    if message == 'quit':
        active = False
     else:
        print(message)
```
## break 退出循环
```python
pro = 'tsts'
por = += 'tsts'
while Ture:
    city = input(por)
    if city == 's':
        break
    else:
        print('sb')
```
以while Ture 打头的循环将不断的运行，直到遇见 break语句，。这个程序中的循环不断让用户输入他到过的城市名字直到用户输入'quit'为止，当用户输入quit语句，导致python退出循环
## 在循环中使用contiune
`counting.py`
```python
current_num = 0
while current_num < 10:
    current_num += 1
    if current_num %  2 ==0:
        contiune
    print(current_num)
```
首先current设置为0，由于它小于10，python进入while循环。进入循环后，以步长为1的方式上述增长，因此current_num为1，接下来，current_num与2的求模运算结果。如果为零（意味着current_num可以被二整除），就执行continue语句，让python忽略剩余的代码，并返回循环的开头。如果当前数不能被2整除，就执行循环中剩余的代码，将这个数打印出来开：
```python
1
2
3
4
5
```
## 避免无限循环
每个while循环必须有停止运行的途径，这样才不会没完没了地只执行下去。例如，下面的循环从1到5：
`counting.py`
```python
x = 1
while x <= 5:
    print(x)
    x += 1
```
每个程序员都会偶尔因不小心而编写出无限循环，在循环的退出条件比较微妙时尤
其如此。如果程序陷入无限循环，可按Ctrl + C，也可关闭显示程序输出的终端窗
口。
要避免编写无限循环，务必对每个while 循环进行测试，确保其按预期那样结束。
如果你希望程序在用户输入特定值时结束，可运行程序并输入这样的值。如果在这
种情况下程序没有结束，请检查程序处理这个值的方式，确认程序至少有一个这样
的地方能让循环条件为False ，或者让break 语句得以执行。
`注意` 　Sublime Text等一些编辑器内嵌了输出窗口，这可能导致难以结束无限
循环，不得不通过关闭编辑器来结束。在这种情况下，可在输出窗口中单击鼠
标，再按Ctrl + C，这样应该能够结束无限循环。
## 使用while循环处理列表和字典
假设有一个列表包含新注册但是未验证的网站用户。验证这些用户后，如何将他们转移到另一个已验证的用户列表中？
```python
nucomfirmed_user = ['alice','bran','candace']
confirmed_user = []
while uncomfirmed_user:
    current_users = unconfirmed_user.pop()
    print(f"Verifying user:{current_users.title()}")
print("\nThe following users have been confirmed:")
for confired_users in confirmed_user:
    print(confirmed_user.title())
```
## 删除维特定值的列表元素
使用方法remove（）来删除特定值的列表函数
```python
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
```
## 使用用户输入来填充字典
可以使用while循环提示用户输入任意多的信息。下面创建一个调查程序，其中的循环每次执行时都时提示输入被调查者的名字和回答。我们将收集的数据，以便于将回答同别调查者关联起来：
```python
responses = ()
#设置一个标识，指出调查者是否继续。
polling_active = True
while polling_active:
    #提示输入被调查者的名字和回答。
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    #将循环存入字典中。
    response[name] = response
    #看看是否还有参与调查。
    repeat = input("Would you like to let anther person respond?(yes/no)")
    if repeat == "no":
        poling_avitve = False
    #调查结束，显示结束
    print("------po;; results-------")
    for name,response in response.items():
        print(f"{name}wold like to climb {response}.")
```
items() //以列表的形式返回可任遍历的（键，值）元组数数组
# 函数
## 定义函数
`gree_user.py`
```python
def greet_user():#使用关键字def来告诉python，你要定义一个函数，这就是函数的定义
    """显示问候文本"""#这一段就是注释用三个双引号括住来表示
    print("hello")#这一段缩进就是就是构成的函数体
greet_user()#代码执行greet_user()，这个函数唯一的用处就是执行打印"hello"
```
以上代码演示了最简单的函数结构。
要使用这个函数，可调用它。函数调用 让Python执行函数的代码。要调用 函数，
可依次指定函数名以及用圆括号括起的必要信息，如❹处所示。由于这个函数不需要
任何信息，调用它时只需输入greet_user() 即可。和预期一样，它打印Hello! ：
```python
hello
```
## 向函数传递信息
只需稍作修改，就可让函数greet_user() 不仅向用户显示Hello! ，还将用户的
名字作为抬头。为此，可在函数定义def greet_user() 的括号内添加
username 。通过在这里添加username ，可让函数接受你给username 指定的
任何值。现在，这个函数要求你调用它时给username 指定一个值。调用
greet_user() 时，可将一个名字传递给它，如下所示：
```python
def greet_user(username):
 """显示简单的问候语。"""
 print(f"Hello, {username.title()}!")
greet_user('jesse')
```
```python
Hello, Jesse!
```
## 实参和形参
前面定义函数greet_user() 时，要求给变量username 指定一个值。调用这个
函数并提供这种信息（人名）时，它将打印相应的问候语。
在函数greet_user() 的定义中，变量username 是一个形参 （parameter），
即函数完成工作所需的信息。在代码greet_user('jesse') 中，值'jesse' 是
一个实参 （argument），即调用函数时传递给函数的信息。调用函数时，将要让函
数使用的信息放在圆括号内。在greet_user('jesse') 中，将实参'jesse' 传
递给了函数greet_user() ，这个值被赋给了形参username 。
注意 　大家有时候会形参、实参不分，因此如果你看到有人将函数定义中的变
量称为实参或将函数调用中的变量称为形参，不要大惊小怪。
`不懂没关系反正经过社会的毒打就懂了`
`好吧来玩笑的`
## 传递实参
### 位置实参 
调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形
参。为此，最简单的关联方式是基于实参的顺序。这种关联方式称为位置实参 。
为明白其中的工作原理，来看一个显示宠物信息的函数。这个函数指出一个宠物属
于哪种动物以及它叫什么名字，如下所示：
```python
def describle_pet(animal_pet,pet_name):#这个函数的定义表明，它需要一种动物类型和名字
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s is {pet_name.title()}")
describle_pet('hamster','harry')#调用函数中，实参’hamster‘,被赋给形参animal_type，而形参’harry‘被赋给形参pet_name
```
```python
I have a hamster.
My hamster's name is Harry.
```
#### 多次调用函数
可以根据需要调用函数任意次。要再描述一个宠物，只需要再次调用describe_pet()即可：
```python
def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster','harry')
describe_pet('dog','willie')
```
第二次调用describe_pet() 函数时，向它传递了实参'dog' 和'willie'
。与第一次调用时一样，Python将实参'dog' 关联到形参animal_type ，并
将实参'willie' 关联到形参pet_name 。与前面一样，这个函数完成了任
务，但打印的是一条名为Willie的小狗的信息。至此，有一只名为Harry的仓
鼠，还有一条名为Willie的小狗：
```python
I have a hamster.
My hamster's name is Harry.
I have a dog.
My dog's name is Willie.
```
多次调用函数是一种效率极高的工作方式，只需要在函数中编写一次宠物信息的代码
然后每当需要需要描述新宠物时，都调用该函数并向它提供新宠物的信息。
即便描述宠物的代码增加到了10行，依然只需使用一行调用函数的代码，就可
描述一个新宠物。
### b.位置实参的顺序很重要
使用位置实参来调用函数时，如果实参的顺序不对，结果可能出乎意料：
```python
def describe_pet(animal_type, pet_name):
 """显示宠物的信息。"""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('harry', 'hamster')
```
在这个函数调用中，先指定名字，再指定动物类型。由于实参'harry' 在前，
这个值将赋给形参animal_type 。同理，'hamster' 将赋给形参pet_name
。结果是有一个名为Hamster的harry：
```python
I have a harry.
My harry's name is Hamster.
```
如果你得到的结果像上面一样可笑，请确认函数调用中实参的顺序与函数定义
中形参的顺序一致
## 关键字实参
关键字实参 是传递给函数的名称值对。因为直接在实参中将名称和值关联起来，所
以向函数传递实参时不会混淆（不会得到名为Hamster的harry这样的结果）。关键
字实参让你无须考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的
用途。
下面来重新编写pets.py，在其中使用关键字实参来调用describe_pet()：
```python
def describe_pet(animal_type, pet_name):
 """显示宠物的信息。"""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')
```
函数describe_pet() 还和之前一样，但调用这个函数时，向Python明确地指出
了各个实参对应的形参。看到这个函数调用时，Python知道应该将实参'hamster'
和'harry' 分别赋给形参animal_type 和pet_name 。输出正确无误，指出有
一只名为Harry的仓鼠。
关键字实参的顺序无关紧要，因为Python知道各个值该赋给哪个形参。下面两个函
数调用是等效的:
```python
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```
注意 　使用关键字实参时，务必准确指定函数定义中的形参名。
## 默认值
编写函数时，可以给每个形参来指定默认值。在调用用函数中给形参提供实参时，
python将使用指定的实参值：否则，将使用形参的默认值。因此，给形参指定默认值。
因此，给形象按指定默认值后，可以在函数调用中省略相应的实参。使用默认可简化函数的调用，
还可以清楚的指出函数的典型用法。
例如，如果你发现调用describe_pet()时，描述的大多数是小狗，就可以将形参aniaml_type的默认值设置为"dog".这样，调用describe_pet()来描述小狗是，就不用提供这样的信息：
```python
def descirbe_pet(pet_name,animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {type_name.title()}")
describe_pet(pet_name='willie')
```
这里修改了函数describe_pet()的定义，在其中给的形参animal_type指定了默认值’dog‘。这样调用这个函数是，如果没有给animal_type指定值，python就会将把这个形参设置为'dog':
```python
I have a dog.
My dog’s name is willie.
```
## 等效的函数调用
鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式
。请看下面对函数describe_pet() 的定义，其中给一个形参提供了默认值：
```python
def describe_pet(pet_name,animal_type='dog'):
```
基于这种定义，在任何情况下都必须给pet_name 提供实参。指定该实参时可采用
位置方式，也可采用关键字方式。如果要描述的动物不是小狗，还必须在函数调用
中给animal_type 提供实参。同样，指定该实参时可以采用位置方式，也可采用
关键字方式。
下面对这个函数的所有调用都可行：
```python
# 一条名为wille的小狗
descirbe_pet('wille')
descirbe_pet(pet_name='wille')
# 一只名为Harry的仓鼠。
describe_pet('Harry','hamster')
```
