import page
from base.base import Base
from  time import  sleep

class PageBuyTickets(Base):
    def page_click_train_tickets(self):
        """
        点击火车票
        """
        self.base_click_element(page.buy_train_ticket)

    def page_choose_begin_station(self, begin_station):
        """
        选择出发站
        :param begin_station: 输入出发站点
        """
        self.base_input_element(page.buy_begin_station, begin_station)

    def page_choose_terminal_station(self, terminal_station):
        """
        选择终点站
        :param terminal_station: 输入终点站点
        """
        self.base_input_element(page.buy_terminal_station, terminal_station)

    def page_choose_time(self, time):
        """
        选择出发时间
        """
        date_input = self.base_find_element(page.buy_begin_time)
        self.driver.execute_script("arguments[0].value = arguments[1];", date_input, time)

    def page_click_find(self):
        """
        点击搜索
        """
        self.base_click_element(page.buy_find)

    def page_click_buy(self):
        """
        点击购买
        """
        self.base_click_element(page.buy_buy)

    def page_input_buy_name(self, name):
        """
        输入姓名
        :param name: 购票人姓名
        """
        self.base_input_element(page.buy_input_buy_name, name)

    def page_input_buy_id(self, id):
        """
        输入购票人id
        :param id: 购票人id
        """
        self.base_input_element(page.buy_input_buy_id, id)

    def page_input_contact_name(self, name):
        """
        输入取票人姓名
        :param name: 取票人姓名
        """
        self.base_input_element(page.buy_input_contact_name, name)

    def page_input_contact_phone(self, phone):
        """
        输入取票人电话
        :param name: 取票人电话
        """
        self.base_input_element(page.buy_input_contact_phone, phone)

    def page_click_submit(self):
        """
        点击提交订单
        """
        self.base_click_element(page.buy_submit)

    def page_submit_success(self):
        """
        判断提交是否成功
        """
        return self.base_if_exist(page.buy_submit_success)

    def page_get_info(self):
        """
        获取错误信息:请正确填写正确内容
        """
        return self.base_get_text(page.buy_submit_fail_info)

    def page_buy_click_button_ok(self):
        """
        点击错误提示信息确认按钮
        """
        self.base_click_element(page.buy_submit_click_OK)

    def page_back_success(self):
        """
        判断是否回退四次成功
        """
        self.base_if_exist(page.buy_train_ticket)


    def page_buy_tickets(self, begin_station, terminal_station, time, name, id, phone):
        # 点击火车票
        self.page_click_train_tickets()
        # 选择出发站和终点站
        self.page_choose_begin_station(begin_station)
        self.page_choose_terminal_station(terminal_station)
        # 选择处出发时间
        self.page_choose_time(time)
        # 点击搜索
        self.page_click_find()
        # 点击购买
        self.page_click_buy()
        # 输入购票人姓名
        self.page_input_buy_name(name)
        # 输入购票人id
        self.page_input_buy_id(id)
        # 输入取票人姓名
        self.page_input_contact_name(name)
        # 输入取票人电话
        self.page_input_contact_phone(phone)
        # 点击提交订单
        self.page_click_submit()




