"""
    提供driver的类，采用单例设计模式，直接通过类访问，避免实例干扰
"""
from selenium import webdriver
import page

class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if(not cls.driver):
            cls.driver = webdriver.Chrome()
            cls.driver.get(page.url)
            cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 注意一定要将driver置为None
            cls.driver = None