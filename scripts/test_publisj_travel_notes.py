from base.get_driver import GetDriver
import unittest
from page.page_publish_travel_notes import PagePublishNotes
from parameterized import parameterized
from tools.read_json import read_json
from page.page_login import PageLogin
from tools.log import GetLogger

logger = GetLogger.getLogger()
global_var = 0
def get_data():
    datas = read_json("publish_travel_notes.json")
    # parameterized要求输入形式：[(a, b ,c, ...), (a, b ,c, ...),(a, b ,c, ...)]
    arrs = []
    for data in datas.values():
       arrs.append((data['name'], data['title'], data['content'], data['success'], data['except_result']))
    return arrs

class TestPublishNote(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()
        cls.publish = PagePublishNotes(cls.driver)
        cls.login = PageLogin(cls.driver)


    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()

    @parameterized.expand(get_data())
    def test_publish_notes(self, tit, preface, content, success, expect_result):
        global global_var
        if global_var == 0:
            self.login.page_login('1314987346', 'wsd20000201')
            global_var = 1
        self.publish.page_publish(tit, preface, content)
        if success:
            try:
                # 判断是否发表成功
                self.assertTrue(self.publish.page_publish_if_success())
                logger.info("发表成功")
                # 退出
                self.publish.page_logout()
                # back三次，回到新建游记部分
                for _ in range(3):
                    self.driver.back()
                try:
                    # 判断是否退出成功:判断是否有新建游记
                    self.publish.page_if_create_new()
                except:
                    # 截图
                    self.publish.base_sceenshot()
                    logger.error("退出失败")
                    raise

            except:
                # 失败截图
                self.publish.base_sceenshot()
                logger.error("发表失败")
                raise

        else:
            msg = self.publish.page_get_info()
            try:
                self.assertEqual(msg, expect_result)
                # 回退一次
                self.driver.back()
                try:
                    self.assertTrue(self.publish.page_if_create_new())
                except:
                    logger.error("退出失败")
                    raise
            except:
                logger.error("信息不匹配，预期结果："+expect_result, "实际结果："+msg)
                raise






