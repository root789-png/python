import yagmail

yag = yagmail.SMTP(user='2840178334@qq.com',
                   # 输入你的账号，注意引号
                   password='88756797918934',
                   # 输入你的密码（如果开启了授权码，只能填授权码）
                   host='smtp.qq.com'
                   # 域名，QQ邮箱填这个域名就可以了
                   )

yag.send(to='2431320433@qq.com',
        subject='计算器的测试报告.html',
             contents='详见附件',
             attachments="C:\\Users\\86187\\PycharmProjects\\pythonProject2\\day13\\testSuite.py")
yag.close
