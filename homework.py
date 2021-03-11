#实现输入10个数字，并打印10个数的求和结果
# lista=[]
# a=0
# sum=0
# while a<10:
#     numa = int(input("请输入数字："))
#     lista.append(numa)
#     a+=1
#     sum = sum + numa
# print("求和结果：")
# print(sum)
# print("--------------------------")
# print("--------------------------")


# #从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# lista=[]
# n=0
# sum=0
# while n<10:
#     numa = int(input("请输入数字："))
#     lista.append(numa)
#     n+=1
#     sum= sum + numa
# max=0
# for a in lista:
#     if max<a:
#         max=a
# average = sum/n
# print("最大值是：{}".format(max))
# print("----------------------")
# print("10个数的和：")
# print(sum)
# print("----------------------")
# print(average)
#使用random模块，如何产生 50~150之间的数？
# import random
# a = random.randint(50,150)
# print(a)
#
# # 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# a = int(input("请输入数据"))
# b = int(input("请输入数据"))
# c = int(input("请输入数据"))
# if a + b > c and b + c > a and a + c > b:
#     print("可以构成三角形")
#     if a == b == c:
#         ("等边三角形")
#     elif (a == b != c) or (a == c != b) or (b == c != a):
#         ("等腰三角形")
#     elif (a * a + b * b == c * c) or (b * b + c * c == a * a) or (a * a + c * c == b * b):
#         print("直角三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不能构成三角形")

# #有以下两个数，使用+，-号实现两个数的调换。
# a=1
# b=2
# c=a+b
# b=c-b
# a=c-b
# print(a,b)

# #实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# name="sa"
# password="123456"
# i=1
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
#         break
#     i = i +1

#编程实现下列图形的打印
# a = int(input("请输入层数："))
# i = 1
# while i <= a:
#     c = 1
#     while  c <= (a - i):
#         print(" ",end="")
#         c =  c + 1
#     y= 1
#     while y <= i:
#         print("* ",end="")
#         y = y +1
#     print()
#     i = i +1

# num = int(input("请输入n层："))
# i = 1
# while i <= num:
#     k = 1
#     while k <= i:
#         print(k,"x",i,"=",(i*k),"\t",end="")
#         k = k +1
#     print()
#
#     i = i + 1

# h = 20
# sum = 0
# day = 0
# while True:
#     day = day + 1
#     sum = sum + 3
#     if sum >= h:
#         print("爬出来了")
#         break
#     else:
#         sum = sum  - 2
# print(day)

# i = 1
# sum = 0
# while i <= 6:
#     k = 1
#     s = 1
#     while k <= i:
#         s = s * k
#         k = k + 1
#     sum = sum + s
#     i = i + 1
# print("阶乘和：",sum)
