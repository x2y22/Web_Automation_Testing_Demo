"""
    基类文件实现所有基本的元素操作，封装使用
        1.元素定位
        2.点击元素
        3.获取元素文本

"""

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from tools.log import GetLogger
from selenium.common.exceptions import StaleElementReferenceException
logger = GetLogger.getLogger()

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def base_find_element(self, loc, timeout=10, poll=0.5):
        """
        定位元素
        :param loc: type为元组，包括元素的定位方式与元素信息
        :param timeout: 显示等待，默认10s
        :param poll: 检测的间隔时间，默认0.5s
        """
        try:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))
        except:
            logger.error("定位元素" + loc[1] + "超时")
            raise

    def base_click_element(self, loc):
        """
        点击元素
        :param loc: 元组，包括元素定位方式与元素信息
        """
        try:
            self.base_find_element(loc).click()
            logger.info("点击元素" + loc[1])
        except:
            logger.error("点击元素" + loc[1] + "失败")
            raise

    def base_get_text(self, loc):
        """
        获取元素的文本
        :param loc: 元组，包括元素的定位方式与元素信息
        """
        try:
            return self.base_find_element(loc).text
        except:
            logger.error("获取" + loc[1] + "文本失败")
            raise

    def base_input_element(self, loc, val):
        """
        对元素进行输入，输入前先清空
        :param loc: 元组，包括元素的定位方式与元素信息
        :param val: 输入的内容
        """
        try:
            el = self.base_find_element(loc)
            el.clear()
            el.send_keys(val)
            logger.info("向元素"+loc[1]+"输入"+val)
        except:
            logger.error("向元素" + loc[1] + "输入" + val + "失败")
            raise

    def base_sceenshot(self):
        """
        截图并保存至文件
        """
        try:
            self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
        except:
            logger.error("截图失败")
            raise

    def base_change_window(self, driver):
        """
        切换窗口
        :param driver: 驱动
        """
        try:
            cur_window = driver.current_window_handle
            driver.switch_to.window(cur_window)
            handles = driver.window_handles
            if len(handles) > 1:
                for handle in handles:
                    if handle != cur_window:
                        driver.switch_to.window(handles[0])
                        driver.close()
                        # 获取不是当前窗口的句柄，并切换
                        driver.switch_to.window(handle)
                        break
            logger.info("切换窗口成功")
        except:
            logger.error("切换窗口失败！")
            raise

    def base_drag(self, loca, locb):
        """
        滑动滑块
        :param loca: 元组，包括滑块元素的定位方式与元素信息
        :param locb: 元组，包括滑框元素的定位方式与元素信息
        :return:
        """
        try:
            # 动态滑动
            loc1 = self.base_find_element(loca)
            loc2 = self.base_find_element(locb)
            self.action.drag_and_drop_by_offset(loc1, loc2.size['width'], -loc2.size['height'])
            self.action.move_by_offset(10, 10)
            self.action.perform()
            time.sleep(1)
            logger.info("滑动模块成功")
        except StaleElementReferenceException:
            logger.info("滑动模块失败")

    def base_if_exist(self, loc):
        """
        判断元素是否存在
        """
        try:
            self.base_find_element(loc)
            logger.info("元素" + loc[1] + "存在")
            return True
        except:
            logger.info("元素" + loc[1] + "不存在")
            return False