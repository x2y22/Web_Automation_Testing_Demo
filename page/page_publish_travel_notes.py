from time import sleep
import page
from base.base import Base

global_var = 0
class PagePublishNotes(Base):

    def page_click_strategy(self):
        """
        点击攻略
        """
        self.base_click_element(page.publish_strategy)

    def page_click_publish_notes(self):
        """
        点击发表游记
        """
        self.base_click_element(page.publish_publish_notes)

    def page_switch_window(self, driver):
        """
        切换窗口
        """
        self.base_change_window(driver)

    def page_if_create_new(self):
        """
        判断是否有新建游记按钮
        """
        return self.base_if_exist(page.publish_new_notes)

    def page_click_create_new(self):
        """
        点击新建游记
        """
        self.base_click_element(page.publish_new_notes)

    def page_input_notes_tit(self, tit):
        """
        输入游记标题
        """
        self.base_click_element(page.publish_notes_tit_before)
        self.base_input_element(page.publish_notes_tit, tit)

    def page_input_preface(self, preface):
        """
        输入前言
        :param preface: 前言内容
        """
        self.base_click_element(page.publish_preface_before)
        self.base_input_element(page.publish_preface, preface)

    def page_input_content(self, content):
        """
        输入游记内容
        :param content: 内容
        """
        self.base_click_element(page.publish_notes_content)
        self.base_input_element(page.publish_notes_content, content)

    def page_click_publish(self):
        """
        点击发表
        """
        self.base_click_element(page.publish_publish)

    def page_publish_if_success(self):
        """
        判断是否发表成功
        """
        return self.base_if_exist(page.publish_success)

    def page_get_info(self):
        """
        获取错误信息
        """
        return self.base_get_text(page.publish_error_info)

    def page_logout(self):
        """
        退出
        """
        self.base_click_element(page.publish_ok_btn)

    def page_publish(self, tit, preface, content):
        """
        总体流程
        :param tit:
        :param preface:
        :param content:
        """
        global global_var
        if global_var == 0:
            # 点击攻略
            self.page_click_strategy()
            # 点击发表游记
            self.page_click_publish_notes()
            # 切换窗口
            self.page_switch_window(self.driver)
            global_var = 1
        # 判断是否有新建游记按钮
        if self.page_if_create_new():
            # 有就点击进入
            self.page_click_create_new()
        # 添加标题
        self.page_input_notes_tit(tit)
        sleep(1)
        # 添加前言
        self.page_input_preface(preface)
        sleep(1)
        # 添加内容
        self.page_input_content(content)
        sleep(1)
        # 点击发表
        self.page_click_publish()





