# 字典的应用
alie_0 = {'color':'green','points':5 }#其中color的键值为green，points的键值为5
#访问字典里的键值
print(alie_0['color'])
print(alie_0['points'])
#添加键值对
alie_0['x_zhou'] = 0
alie_0['y_zhou'] = 25
print(alie_0)
alien={}
alien['color'] = 'blue'
alien['porint']=5
print(alien)
#字典的修改
alien_1 = {'color':'green'}
print(f"the alien_1 color is:{alien_1['color']}")
alien_1['color'] = 'blue'
print(f"the alien_1 new color is : {alien_1['color']}")
#字典的修改的实际应用
alien_2 = {'x_zhou':0,'y_zhou':25,'speed':'medium'}
print(f"Original position: {alien_2['x_zhou']}")
if alien_2['speed'] == 'slow':
    x_zhouspeed = 1
elif alien_2['speed'] == 'meddium':
    x_zhouspeed =2
else:
    x_zhouspeed =3
alien_2['x_zhou'] = alien_2['x_zhou'] + x_zhouspeed
print(f"the new position:{alien_2['x_zhou']}")
#删除字典中的键值
alien_3 = {'color':'green','priont':5}
print(alien_3)
del alien_3['color']
print(alien_3)
#由类似对象组成的字典
favourite_languages = {
    'jun':'python',
    'chen':'c',
    'dunck':'java',
    'junke':'php',
}
languages = favourite_languages['chen'].title()
print(f"chen's favourite languages is {languages}")
favourite_languages1 = {
    'jen':'python',
    'sarah':'c',
    'phll':'python',
}
for name in favourite_languages1.keys():
    print(name.title())


favourite_languages2 = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
 }
friends = ['jen','phil','sarah']#创建了一个列表，其中包含收到打印消息的朋友。
for name in favourite_languages2.keys():#在循环中，打印每个人的名字，并检查当前的名字是否在列表friend中
    print(f"Hi {name.title()}.")
    if name in friends:#如果在，就打印一句特殊的问候语，其中包含这位朋友的语言。为获悉朋友喜欢的语言，我们使用了字典名，并将 变量name的当前值作为键
        languages = favourite_languages2[name].title()
        print(f"\t{name.title()},I see you love {languages}!")



favourite_languages3 = {
    'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
}
if 'phil' not in favourite_languages3.keys():
    print("phil,please take our poll!")
else:
    print("good job");

favourite_languages4 ={
    'jen':'python',
    'sarah':'c',
    'phil':'python'
}
friends2 = {'jen','phil'}
for name in favourite_languages4.keys():
    if name not in friends2:
        print(f"{name.title()},what you favourite language?");
favourite_languages5 = {
    'jen':'python',
    'sarach':'c',
    'phil':'python'
}
for name in sorted(favourite_languages5.keys()):
    print(f"{name.title()},thank you takling the poll.");
favourite_languages6 = {
    'jen':'python',
    'sarah':'c',
    'phil':'python'
}
print("the following languages have been mentioned:")
for language in favourite_languages6.values():
    print(language.title());


favourite_languages7 = {
    'jen':'python',
    'sarah':'c',
    'phil':'python'
}
print("the following languageas have been mentiond:")
for languages7 in set(favourite_languages7.values()):
    print(languages7.title());
#创建一个应该接受调查的人员名单，其中有些人已经包含在字典中，而其他人未包含在字典中。
#遍历这个人员名单，对于已经参加调查的人，打印一条消息表示感谢；对于还未参加的人，打印一条消息邀请他参加。
favourite_languages8 = {
    'jen':'python',
    'sarah':'c',
    'phil':'python',
}
name3 = {
    'jen','sarah','phil','ren',
}
for names in name3:
    if names in favourite_languages8:
        print(f"{names.title()},thank you did this activity")
    else:
        print (f"{names.title()},place do it");


# 嵌套
#one please
aliens_0 ={'color':'green','points':5}
aliens_1 = {'color':'red','points':5}
aliens_2 = {'color':'yellow','points':5}
aliens_plus =[aliens_1,aliens_0,aliens_2]
for alien in aliens_plus:
    print(alien);


#创造多个字典
alien_sd = []
for alien_number in range(30):
    new_aliens = {'color':'green','points':5,'speed':'slow'}
    alien_sd.append(new_aliens)
for alien in alien_sd[:5]:
    print(alien)
print('...')
print(f"total number of aliens:{len(new_aliens)}")

#进阶版其中有些外星人改变了自身字典的元素
aliensx = []
for alien_num in range(20):
    xin_alien = {'color':'green','points':5,'speed':'slow'}
    aliensx.append(xin_alien);
for alienx in aliensx[:3]:
    if alienx['color'] == 'green':
        alienx['color'] = 'yellow'
        alienx['points'] = 10
        alienx['speed'] = 'fast'
for alien in aliensx[:3]:
    print(alien);

print('................................................................')
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


