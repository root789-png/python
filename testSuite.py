'''
    测试集：
        testsuite



'''

import unittest
from HTMLTestRunner import HTMLTestRunner  # 没有这个模块就安装这个模块
# 创建测试集
suite = unittest.TestSuite()
# 加载所有测试用例
# 使用加载器集中加载用例
loader = unittest.defaultTestLoader
# 使用测试加载器加载用例（路径就是测试文件所在的路径，pattern匹配的规则）
tests = loader.discover("C:\\Users\\86187\\PycharmProjects\\pythonProject2\\day13",pattern="*Test.py")
# 将用例添加到测试集里
suite.addTest(tests)
# 生成一份html界面版的测试报告
f = open("计算器的测试报告.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f, # 将结果写入到计算器的测试报告.html里
    verbosity = 1, # 详细程度
    title="这是一份计算器的测试报告--jason版权所有" # 测试标题
)
# 让运行器开始运行测试集里的所有用例
runner.run(suite)
