import unittest
from time import sleep, time
import page

import page
from base.get_driver import GetDriver
from page.page_login import PageLogin
from parameterized import parameterized
from tools.read_json import read_json
from tools.log import GetLogger

logger = GetLogger.getLogger()
def get_data_login():
    datas = read_json(page.login_json)
    # parameterized要求输入形式：[(a, b ,c, ...), (a, b ,c, ...),(a, b ,c, ...)]
    arrs = []
    for data in datas.values():
       arrs.append((data['username'],data['password'],data['success'],data['expect_result']))
    return arrs

class TestLogin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()
        cls.login = PageLogin(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()

    @parameterized.expand(get_data_login())
    def test_login(self, username, password, success, expect_result):
        # 进入登录页面
        logger.info("测试登录页面")
        self.login.page_login(username, password)
        if success:
            try:
                # 判断安全退出是否存在
                self.assertTrue(self.login.page_if_login_success)
                # 点击退出
                self.login.page_click_logout_btn()

                # 判断是否退出成功
                try:
                    self.assertTrue(self.login.page_if_login_success())
                except:
                    # 截图
                    self.login.page_screenshot()

                # 退出成功为下一次数据组做准备
                # 点击登录
                self.login.page_click_login_link()
                # 点击账号密码登录
                self.login.page_click_password_login()
            except:
                # 截图
                self.login.page_screenshot()

        else:
            try:
                msg = self.login.page_get_info()
            except:
                logger.error("没有获取到元素的文本")
                raise
            if(type(msg)==str):
                try:
                    assert msg == expect_result
                    logger.info("文本提示与预期结果匹配")
                except AssertionError:
                    logger.error(
                            "文本提示与预期结果不匹配, " + "预期结果是:" + expect_result + ", " + "实际结果是:" + msg)
                    # 截图
                    self.login.page_screenshot()
                    raise
            self.driver.refresh()
            # # 点击 账号密码登录
            self.login.page_click_password_login()
            # self.login.page_click_agreement()













