# 确定用户库
bank = {
    "123456789": {
        "username": "李三",
        "password": "123",
        "country": "中国",
        "province": "北京",
        "street": "回龙观",
        "door": "S005",
        "money": 5000,
        "bank_name": "中国工商银行昌平区回龙观支行"
    },
    "987654321": {
        "username": "王五",
        "password": "456",
        "country": "中国",
        "province": "北京",
        "street": "回龙观",
        "door": "S005",
        "money": 6000,
        "bank_name": "中国工商银行昌平区回龙观支行"
    },
}
# 确定银行的开户名称
bank_name = "中国工商银行昌平区回龙观支行"

info = '''
    *********************************
    *    中国工商银行账户管理系统     *
    *********************************
    *   1.开户                      *
    *   2.存款                      *
    *   3.取款                      *
    *   4.转账                      *
    *   5.查询账户                  *
    *   6.Bye！                     *
    ********************************
'''
import random

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door,money):
    # 判断用户库是否已满
    if len(bank) >= 100:
        return 3

    # 判断是否存在
    # 获取所有键，然后在判断是否有
    keys = bank.keys()
    if account in keys:
        return 2
    # 正常开户
    bank[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    return 1

# 开户逻辑
def addUser():
    # 生成账号：  8位随机
    string = ""  # 随机数缓冲
    for i in range(8):  # 循环8次取字符

        string = string + "1234567890"[random.randint(0,9)]  # 拼接

    account = string
    print("账号为：",account)
    username = input("请输入姓名：")
    password  = input("请输入密码：")
    print("接下来输入地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street = input("\t输入街道：")
    door = input("\t输入门牌号：")
    money = int(input("请初始化您的余额："))

    # 调用银行的开户方法
    s = bank_addUser(account,username,password,country,province,street,door,money)

    if s == 1:
        print("开户成功！")
        print("以下是您的开户个人信息：")
        print("***********************")
        print("账号：",account)
        print("用户名：", username)
        print("密码：******")
        print("国家：", country)
        print("省份：", province)
        print("街道：", street)
        print("门牌号：", door)
        print("账户余额：", money)
        print("******************开户行地址：", bank_name)

    elif s == 2:
        print("该用户已存在！")
    elif s ==  3:
        print("对不起，该银行已满！请携带证件到其他银行办理！")

#银行的转账逻辑
def bank_transfer(out_account,in_account):
    keys = bank.keys()
    if out_account in keys and in_account in keys:
        password = input("请输入密码：")
        if password == bank[out_account]["password"]:
            money = int(input("请输入金额："))
            if money <= bank[out_account]["money"]:
                bank[out_account]["money"] = bank[out_account]["money"] - money
                bank[in_account]["money"] = bank[in_account]["money"] + money
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


#转账逻辑
def transfer():
    out_account = input("请输入转出的账号：")
    in_account = input("请输入转入的账号：")

    s = bank_transfer(out_account,in_account)
    if s == 0:
        print("转账成功")
        print("转出账号剩余：",bank[out_account]["money"])
        print("转入账号剩余：", bank[in_account]["money"])
    elif s == 1:
        print("转出或转入账号不存在")
    elif s == 2:
        print("密码不正确")
    elif s == 3:
        print("金额不足")



while True:  # 一直循环的进入选项
    print(info)
    chose = input("请输入您的选项：")
    if chose == "1": # 判断是否是1
        addUser()
    elif chose == "2": # 判断是否是2
        print("存款！")
    elif chose == "3":  # 判断是否是3
        print("取款！")
    elif chose == "4":  # 判断输入的是否是4
        transfer()
    elif chose == "5": # 判断输入的是否是5
        print("查询账户！")
    elif chose == "6":   # 判断输入的是否是6，若是6则需要退出 break
        print("拜拜了您嘞！")
        break
    else:
        print("输入非法！重新输入！")



