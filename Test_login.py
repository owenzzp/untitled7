# coding=utf-8

import unittest, time
from selenium import webdriver



# 创建浏览器
class Test_Login(unittest.TestCase):
    # 初始化
    def setUp(self):
        #创建浏览器
        self.driver = webdriver.Chrome()
        #窗口最大化
        self.driver.maximize_window()
        #操作的地址
        url = 'http://localhost/Home/user/login.html'
        #打开地址网页
        self.driver.get(url)
    # UI定位
    def login(self, name, password, verify):
        driver = self.driver
        driver.find_element_by_id("username").send_keys(name)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("verify_code").send_keys(verify)
        time.sleep(3)
        driver.find_element_by_name("sbtbutton").click()
        time.sleep(10)

    # 用户名，密码正确
    def test_LoginSccess1(self):
        '''用户名，密码都正确'''
        self.login('15299999999', '123456', '8888')
        asser = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/a[2]').text
        self.assertEqual(asser, '安全退出')

    # 用户名空
    def test_LoginSccess2(self):
        '''用户名为空，密码正确'''
        self.login('', '123456', '8888')
        asser = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
        self.assertEqual(asser, '用户名不能为空!')

    # 密码空
    def test_LoginSccess3(self):
        '''输入正确用户名，密码为空'''
        self.login('15299999999', '', '8888')
        # all_handles = self.driver.window_handles
        # print(all_handles)
        # # 切换到新的handle上
        # self.driver.switch_to.window(all_handles[1])
        asser = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
        self.assertEqual(asser, '密码不能为空!')

        # 结束函数

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
