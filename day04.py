# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
# i=0
# # sum = 0
# names = [
#     ["曹操",56,"男","106","IBM", 500 ,"50"],
#     ["大乔",19,"女","230","微软", 501 ,"60"],
#     ["小乔", 19, "女", "210", "Oracle", 600, "60"],
#     ["许褚", 45, "男", "230", "Tencent", 700 , "10"]
# ]
# #1.统计每个人的平均薪资
# while i < 4:
#     sum = sum + names[i][5]
#     i = i + 1
# print("每个人的平均薪资")
# print(sum/4)

#2.统计每个人的平均年龄
# i=0
# sum = 0
# while i < 4:
#     sum = sum + names[i][1]
#     i = i + 1
# print("每个人的平均年龄")
# print(sum/4)

#公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
# names.append(["刘备",45,"男",220,"alibaba",500,30])
# print("添加后为：  ")
# print(names)

#4.统计公司男女人数
# i=0
# a=0
# b=0
# while i<4:
#     if  names[i][2]=="男":
#         a = a + 1
#     else:
#         b=b+1
#
#     i=i+1
#
# print("男生人数",a,"----","女生人数",b)

#5.每个部门的人数
# i = 0
# sum=0
# B=0
# b=0
# c=0
# d=0
# e=0
# while i<4:
#     if "50"==names[i][6]:
#         b=b+1
#     elif "60" == names[i][6]:
#         c=c+1
#     elif "10"==names[i][6]:
#         d=d+1
#     else:
#         e=e+1
#     i=i+1
#
# print("部门编号50部门人数数为：",b,"部门编号60人数为：",c,"部门编号10人数为：",d,"其他部门编号人数为：",e)
#
# [罗恩, 23 ,35 ,44]
# [哈利 ,60, 77 ,68 ,88, 90]
# [赫敏, 97 ,99 ,89 ,91, 95, 90]
# [马尔福 ,100, 85 ,90]
# 求每个人的总成绩？
# x = input("请输入姓名：   ")
# a=["罗恩", 23 ,35 ,44]
# b=["哈利" ,60, 77 ,68 ,88, 90]
# c=["赫敏", 97 ,99 ,89 ,91, 95, 90]
# d=["马尔福" ,100, 85 ,90]
# sum1=0
# sum2=0
# sum3=0
# sum4=0
# i=0
# e=[a,b,c,d]
# if x==e[0][0]:
#     sum1=e[0][1]+e[0][2]+e[0][3]
#     print(sum1)
# elif x==e[1][0]:
#     sum2=e[1][1]+e[1][2]+e[1][3]+e[1][4]+e[1][5]
#     print(sum2)
# elif x==e[2][0]:
#     sum3=e[2][1]+e[2][2]+e[2][3]+e[2][4]+e[2][5]+e[2][6]
#     print(sum3)
# else:
#     sum4=e[3][1]+e[3][2]+e[3][3]
#     print(sum4)

#对购物车系统进行改造：
# （1）添加登陆功能，登陆后才能进行购物操作。
# （2）添加结算积分添加功能。
# （3）登陆成功后系统随机分发一张优惠券（免单券6张，免半券3张，满600减100券50张，满10000减1000券10张，无券）前提是优惠券存在列表中。
# import random
# name="sa"
# password="123456"
# i=1
# sum=0
# while True:
#     if i ==4:
#         print("系统已锁定")
#         break
#     uname = input("请输入用户名：")
#     upassword = input("请输入密码")
#     if(name!=uname) or(password!=upassword):
#         print("请重新输入")
#     else:
#         print("成功登录！")
#         num = random.randint(0, 6)
#         print("恭喜您获得免拼单劵", num, "张！")
#         break
#     i = i +1
# shop = [
#     ["Iphone 6x",6000],
#     ["HUAWEI watch",2000],
#     ["lenovo Pc",4500],
#     ["Mac Pc",12000],
#     ["卫龙辣条",5],
#     ["老干妈",7.5]
# ]
# salary = int(input("请输入您的初始资金："))
# mycat = []
# while True:
#     for index, value in enumerate(shop):
#         print(index, value)
#     num = input("亲输入您要的商品编号：")
#     if num.isdigit():
#         num = int(num)
#         if num in range(len(shop)):
#             if salary >= shop[num][1]:
#                 mycat.append(shop[num])
#                 salary = salary - shop[num][1]
#                 print("\033[32;20;1m购买成功！您的余额为：",salary,"￥！\033[0m")
#                 sum=sum+5
#                 print("您获得的购买积分为：  ",sum)
#             else:
#                 print("\033[41;20;1m对不起，您的余额不支持买改商品！穷鬼！\033[0m")
#         else:
#             print("该商品不存在！别瞎弄！")
#     elif num == "Q" or num == "q":
#         print("欢迎下次光临！")
#         break
#     else:
#         print("输入非法，请重新输入！")
# print("您的购买内容为：")
# for index,value in enumerate(mycat):
#     print(index,":",value)
# print("------------您的余额：",salary,"￥！------------------")

#当输出54321时，写出下面的执行结果
# num = int (input("请输入一个： "))
# while num !=0:
#     print(num%10)
#     num=num//10
#请对下列列表进行冒泡排序（网易测试开发笔试题）
# def bubbleSort(list):
#     for i in range(len(list) - 2):
#         for j in range(len(list) - 1 - i):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#     print(list)
#
#
# if __name__ == '__main__':
#     a = [5,2,4,7,9,1,3,5,4,0,6,1,3]
#     bubbleSort(a)
