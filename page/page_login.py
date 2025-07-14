"""
    对登录页面进行测试
        正例：登录成功
        反例：用户名或密码错误，登录失败
"""
from time import sleep
import page
from base.base import Base


class PageLogin(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.global_variable = 0
    def page_click_please_login(self):
        """
        点击进有登录按钮的界面
        """
        self.base_click_element(page.login_please_login)

    def page_change_window(self, driver):
        """
        切换主窗口到登录界面
        :param driver:
        :return:
        """
        self.base_change_window(driver)

    def page_click_login_link(self):
        """
        点击登录
        """
        self.base_click_element(page.login_login_link)

    def page_click_password_login(self):
        """
        点击密码登陆
        """
        self.base_click_element(page.login_password_login)

    def page_input_username(self, username):
        """
        输入用户名
        """
        self.base_input_element(page.login_input_username, username)

    def page_input_password(self, password):
        """
        输入密码
        """
        self.base_input_element(page.login_input_password, password)

    def page_click_agreement(self):
        """
        点击接受协议
        """
        self.base_click_element(page.login_click_agreement)

    def page_click_login_btn(self):
        """
        点击登录按钮
        """
        self.base_click_element(page.login_login_btn)

    def page_drag_slider(self):
        """
        滑动滑块
        """
        self.base_drag(page.login_drag_slider, page.login_drag_track)

    def page_get_info(self):
        """
        获取登录的错误或成功提示文本
        """
        return self.base_get_text(page.login_get_info)

    def page_screenshot(self):
        """
        截屏
        """
        self.base_sceenshot()

    def page_click_logout_btn(self):
        """
        点击退出按钮
        """
        self.base_click_element(page.login_logout)

    def page_if_login_success(self):
        """
        判断是否登录成功
        """
        return self.base_if_exist(page.login_logout)

    def page_login(self, username, password):
        """
        登录页面测试全部流程
        """
        if self.global_variable == 0:
            # 点击有登录按钮的界面
            self.page_click_please_login()
            # 切换窗口
            self.page_change_window(self.driver)
            # 点击登录链接
            self.page_click_login_link()
            # 点击密码登录
            self.page_click_password_login()
            self.global_variable = 1
        # 输入用户名与密码
        self.page_input_username(username)
        self.page_input_password(password)
        # 点击接受协议
        self.page_click_agreement()
        # 点击登录按钮
        self.page_click_login_btn()
        # 滑动滑块
        self.page_drag_slider()
