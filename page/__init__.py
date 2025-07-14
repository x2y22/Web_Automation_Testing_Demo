"""
    测试网页元素的相关信息
"""
from selenium.webdriver.common.by import By

# ------------路径配置-------------
# 浏览器驱动路径
driver_file = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
# 测试网址
url = 'https://www.qunar.com/'
# 用户登录数据   放一组真实数据
login_json = "....../data/login.json"
# 用户写游记数据
publish_json = "....../data/publish_travel_notes.json"
# 用户购票数据
buyTicket_json = "....../data/buy_tickets.json"
# 日志路径
log_file = "....../log/log"
# 报告路径
report_file = "....../reports/TestReport.html"
# 测试脚本路径
test_scripts = "....../scripts"


# ------------测试登录功能-------------
# 请求进入登录页面元素信息
login_please_login = By.XPATH, "//div[contains(text(), '关于去哪儿')]"
# 登录链接
login_login_link = By.XPATH, "//a[text()='登录']"
# 密码登录按钮
login_password_login = By.XPATH, "//*[@class='passwordTab']"
# 账户输入
login_input_username = By.CSS_SELECTOR, "#username"
# 密码输入
login_input_password = By.CSS_SELECTOR, "#password"
# 接受协议
login_click_agreement = By.CSS_SELECTOR, "#agreement"
# 登录按钮
login_login_btn = By.XPATH, "//div[@class='button' and @role='button']/span[text()='登录']"
# 登录滑动校验滑块
login_drag_slider = By.CSS_SELECTOR, ".OQphwVk_QrhLuedI5-Jme"
# 滑动校验轨道
login_drag_track = By.CSS_SELECTOR, ".NrgjHeg7YBdiFd3U9T_j_"
# 错误信息：错误用户名或密码
login_get_info = By.XPATH, "//div[@class='wrongDesc']/div/span"
# 退出
login_logout = By.CSS_SELECTOR, "#__loginInfo_r__"


# ------------测试购票功能-------------
# 火车票
buy_train_ticket = By.XPATH, "//li[@class='qhf_train']//span/b[text()='火车票']"
# 出发站
buy_begin_station = By.XPATH, "//input[@name='fromStation']"
# 到达站
buy_terminal_station = By.XPATH, "//input[@name='toStation']"
# 出发日期
buy_begin_time = By.XPATH, "//input[@class='cinput textbox js-sts-travelDate']"
# 搜索
buy_find = By.XPATH, "//span[@class='p_btn']/button[@name='stsSearch']"
# 购买
buy_buy = By.XPATH,"//span[text()='购\u00A0\u00A0买']"
# 购票人姓名
buy_input_buy_name = By.XPATH, "//input[@name='pName_0']"
# 购票人身份证号
buy_input_buy_id = By.XPATH, "//input[@name='pCertNo_0']"
# 取票人姓名
buy_input_contact_name = By.XPATH, "//input[@name='contact_name']"
# 取票人电话
buy_input_contact_phone = By.XPATH, "//input[@name='contact_phone']"
# 提交订单
buy_submit = By.XPATH, "/html/body/form/div[2]/div[2]/div[4]/div[2]/div[3]/button"
# 提交订单成功
buy_submit_success = By.XPATH, "//div[@class='title_nm' and text()='订单信息']"
# 提交订单失败
buy_submit_fail_info = By.XPATH, "//div[@class='retitle'][text() = '请正确填写所有内容']"
# 错误信息确认按钮
buy_submit_click_OK = By.XPATH, "//b[text()='确定']"


# ---------------发表旅行日记-----------------
# 攻略
publish_strategy = By.XPATH, "//span/b[text() = '攻略']"
# 发表游记
publish_publish_notes = By.XPATH, "//li[@class='notes']//b[@class='icon_create']"
# 新建游记
publish_new_notes = By.XPATH, "//div[@class='btns']/a"
# 游记标题
publish_notes_tit_before = By.XPATH, "//a[@class='tit' and text()='为游记起一个拉轰的名字']"
publish_notes_tit = By.CSS_SELECTOR, ".e_note_tit_edit .title_input"
# 前言
publish_preface_before = By.CSS_SELECTOR, "div.memo_node textarea"
publish_preface = By.CSS_SELECTOR, "div.memo_node textarea"
# 游记内容
publish_notes_content = By.CSS_SELECTOR, "div[data-uniquekey='memo_node_2'] textarea"
# 游记点击发表
publish_publish = By.XPATH, "//div[@class='b_note_ft']/a[text() = '发表游记']"
# 游记发表成功
publish_success = By.CSS_SELECTOR, "div.b_dialog div.e-submit-dialog div.title p.text"
# 点击确定
publish_ok_btn = By.XPATH, "//div[@class='content']/a[@class = 'submit-btn' and text()='确定']"
# 错误信息
publish_error_info = By.CSS_SELECTOR, "div.tit_tip > span"







