"""
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
print (d.values())
sum = 0.0
for score in d.values():
    sum = sum(score)
print (sum)
"""

# 2020/06/18
#def toUppers(L):
#   return[x.upper() for x in L if isinstance(x,str)]

#print (toUppers(['Hello','world',101]))


#print ([x*100+y*10+x for x in range(1,10) for y in range(0,10)])

#def add(x,y,f):
#    return f(x)+f(y)
#add(-5,9,abs)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Sean_Yao
"""工资管理系统作业"""
import  sys
with open("info.txt", 'r', encoding="utf-8") as f:
    file = list(f)
msg = '''
1. 查询员工工资
2. 修改员工工资
3. 增加新员工记录
4. 退出
'''
exit_flag = False
while not exit_flag:
    print(msg)
    index_user_choice = input('>>:')
    if index_user_choice == '1':
        with open("info.txt", 'r', encoding="utf-8") as f:
            user_salary = f.readlines()
        username = input("请输入要查询的员工姓名（例如：Alex）：")
        for user_line in user_salary:
            (user,salary) = user_line.strip('\n').split()
            if username == user:
                print('%s 的工资是：%s ' % (username,salary))
                pass

    elif index_user_choice == '2':
            old_user = input("输入员工姓名（例如：Alex）：").strip()
            for i in file:
                file = i.strip().split()
                if old_user in file:
                    old_salary = file[1]
                    new_user,new_salary = input("请输入更改后员工姓名和工资，用空格分隔（例如：Alex 10）：").strip().split()
                    with open("info.txt", "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    with open("info.txt", "w", encoding="utf-8") as f_a:
                        for line in lines:
                            if old_user in line:
                                line = line.replace(old_user,new_user)
                            f_a.write(line)
                        f_a.close()
                    with open("info.txt", "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    with open("info.txt", "w", encoding="utf-8") as f_b:
                        for line in lines:
                            if new_user in line:
                                line = line.replace(old_salary,new_salary)
                            f_b.write(line)
                        f_b.close()
                        print("修改成功")

    elif index_user_choice == '3':
        f = open('info.txt', 'r+', encoding='utf-8')
        user_salary = f.readlines()
        new_user_new_salary = input("请输入要增加的员工姓名和工资，共空格分割（例如：Eric 100000）：")
        f.write(new_user_new_salary + '\n')
        f.close()
    elif index_user_choice == '4':
        sys.exit("再见")
    else:
        print('输入操作无效！')