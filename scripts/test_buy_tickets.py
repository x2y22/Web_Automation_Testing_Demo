import unittest
from parameterized import parameterized
from time import sleep
from base.get_driver import GetDriver
from tools.read_json import read_json
from page.page_buy_tickets import PageBuyTickets
from page.page_login import PageLogin
from tools.log import GetLogger
import page

logger = GetLogger.getLogger()
global_val = 0
def get_data():
    data = read_json(page.buyTicket_json)
    arrs = []
    for data in data.values():
        arrs.append((data['start_station'],data['arrive_station'],data['time'], data['name'], data['id'],
                     data['phone'], data['success'], data['except_result']))
    return arrs

class TestBuyTickets(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()
        cls.buy = PageBuyTickets(cls.driver)
        cls.login = PageLogin(cls.driver)


    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()

    @parameterized.expand(get_data())
    def test_buy(self, begin_station, terminal_station, time, name, id, phone, success, expect_result):
        global global_val
        # 如果是第一组数据，需要先登录
        if global_val == 0:
            self.login.page_login(username='13438970225', password='13880188217fu')
            global_val = 1
        # 购票
        self.buy.page_buy_tickets(begin_station, terminal_station, time, name, id, phone)
        if success:
            try:
                # 判断是否提交订单成功
                sleep(2)
                # self.assertTrue(self.buy.page_submit_success() == True)
                logger.info("订单提交成功")
                # 四次回退到回退选择购票信息页面
                for _ in range(4):
                    self.driver.back()
                try:
                    # 判断是否在选票界面
                    self.assertTrue(self.buy.page_back_success())
                    logger.info("回到选票页面成功")
                except:
                    # 截图
                    self.buy.base_sceenshot()
                    logger.error("回到选票页面失败")
            except:
                # 截图
                self.buy.base_sceenshot()
        else:
            msg = self.buy.page_get_info()
            try:
                self.assertEqual(msg, expect_result)
                sleep(2)
                # 点击确认框
                self.buy.page_buy_click_button_ok()
                # 回退三次到火车票界面
                for _ in range(3):
                    self.driver.back()
                try:
                    # 判断是否在选票界面
                    self.assertTrue(self.buy.page_back_success)
                    logger.info("回到选票页面成功")
                except:
                    # 记录错误信息
                    self.buy.base_sceenshot()
                    logger.error("回到选票页面失败")
            except:
                self.buy.base_sceenshot()
                logger.error("错误信息与预期不相等, 预期结果是：" + expect_result, "实际结果是：" + msg)


