def input_info():
    infile_info = open('infile.txt','a')
    flag = 'y'
    while flag == 'y' or flag == 'Y':
        stu_id = input("请输入学生学号:")
        stu_name = input("请输入学生姓名:")
        stu_eng = input("请输入学生英语成绩:")
        stu_py = input("请输入学生python成绩:")
        stu_math = input("请输入学生数学成绩：")
        stu_sum_score = int(stu_eng) + int(stu_py) + int(stu_math)        
        stu_info = stu_id + '\t' + stu_name  + '\t' + stu_eng + '\t' +stu_py + '\t' + \
        infile_info.write(stu_info)
        flag = input("是否继续添加学生信息？y/n")
        print("信息录入完毕！！！")
        infile_info.close()
#查询学生信息： 查询时分为按学号和姓名查询两种
def find_info():
    flag = 'y'
    while flag == 'y'  or  flag  == 'Y':
        n=0
        m=0    #定义吗m,n是为了用作判断文件是否有此人的信息的标记
        findfile_info = open ('infile.txt','r') #以可访读方式打开文件
        line_info = findfile_info.readline()
        find_nid = input("按学号查询请输入1,按姓名查找请输入2:")
        #查询方式分为按学号和姓名
        if find_nid == '1':
            find_id = input("请输入学生学号：")
            for line in line_info:
                if find_id in line:
                    print(line)
                    n = n+1
            if n == 0:
                print("没有查询到学生信息，无数据显示！！！")
            if find_nid == "2":
                find_name = input("请输入学生姓名：")
                for line in line_info:
                    if find_name in line:
                        print(line)
                        m = m+1
                if m == 0:
                    print("没有查询到学生信息，无数据显示！！！")
            findfile_info.close()
            flag = input("是否继续查询学生信息?y/n")
# 删除学生信息：输入学号进行查询，查到学生信息之后，对学生信息之后，对学生信息进行删除
def del_info():
    flag = 'y' or flag=='Y'; 
    n = 0 #用以查无此人时的标记
    defile_info1 = open('infile.txt','+r') #以可读方式打开文件
    line_info = defile_info1.readlines()
    #将文件的信息按行全部读取出来，此时line_info是一个列表，每一行是一个元素
    defile_info2 = open('infile.txt','w')
    del_id = input('请输入要删除的学生的学号：')
    for line in line_info:
        continue
    defile_info2.write(line)
    n = n + 1
if n == len(line_info):
     print("无此学生信息，请核对后再操作！！！")
else:
    print("学号{0}的学生信息已被删除！！！".format(del_id))
    defile_info1.close()
    defile_info2.close()
    flag = input("是否继续删除学生信息?y/n")

#修改学生信息：输入学号，查询学生信息后，对学生信息进行修改
def mod_info():
    flag = 'y'
    while flag == 'y' or flag == 'Y':
        n=0 #用以查无此人时的标记
        mod_id = input ('请输入要修改的学生学号；')
        modfile_file1 = open('infile.txt','+r')
        line_info = open('infile.txt','+r')
        line_info = modfile_file1.readlines()
        modfile_file2 = open("infile.txt",'+w')
        for line in line_info:
            if mod_id in line:
                print("已找到学生，请修改信息！")

