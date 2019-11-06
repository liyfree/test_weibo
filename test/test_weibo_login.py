import HTMLTestRunner
import os
import time
import unittest
from os.path import dirname, abspath
from time import sleep
from selenium import webdriver
from page.weibo_login_page import WeiboLoginPage
from base.readTxtUtil import ReadTxtUtil

class TestWeiboLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome()
        # 读取txt文件中的测试用例
        cls.datas = ReadTxtUtil.readTxt("./test_case.txt")
        print(cls.datas)

    @classmethod
    def tearDownClass(cls) :
        cls.driver.quit()

    def test_weibo_login_case1(self):
        """微博登录,账号正确，密码错误"""
        page = WeiboLoginPage(self.driver)
        page.open_page()
        page.login(self.datas[0][0],self.datas[0][1])
        sleep(3)
        title = page.get_title()
        self.assertEqual(title, "微博-随时随地发现新鲜事")

    def test_weibo_login_case2(self):
        """微博登录，账号、密码都错误"""
        page = WeiboLoginPage(self.driver)
        page.open_page()
        page.login(self.datas[1][0],self.datas[1][1])
        sleep(3)
        title = page.get_title()
        self.assertEqual(title, "微博-随时随地发现新鲜事")

    def test_weibo_login_case3(self):
        """微博登录，账号密码正确"""
        page = WeiboLoginPage(self.driver)
        page.login(self.datas[2][0],self.datas[2][1])
        sleep(10)
        url = page.get_url()
        self.assertIn("https://weibo.com/724973851",url)

if __name__ == '__main__':

    print("开始测试")
    # 创建测试套件
    suit = unittest.TestSuite()
    # 添加测试用例
    suit.addTest(TestWeiboLogin("test_weibo_login_case1"))
    suit.addTest(TestWeiboLogin("test_weibo_login_case2"))
    suit.addTest(TestWeiboLogin("test_weibo_login_case3"))
    # 获取当前文件的上级目录的上级目录D:\py_project\test_weibo
    project_path = dirname(dirname(abspath(__file__)))
    print("project_path=" + project_path)
    # 自动查找测试用例
    # suit = unittest.defaultTestLoader.discover(project_path+"/test",pattern="test*.py")
    # 获取当前时间
    cur_time = time.strftime('%Y-%m-%d %H%M%S')
    # 打开文件，如果不存在会自动创建
    file_name = open(project_path+"/report/weibo_login_test_report_"+cur_time+".html","wb")
    # stream 打开文件名称， verbosity 日期级别默认1,2更详细
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=file_name,
        verbosity=2,
        title="微博登录测试报告",
        description="测试环境，win7，chrome"
    )
    runner.run(suit)
    # 关闭文件
    file_name.close()
    print()
    print("结束测试")


