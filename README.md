## 使用Selenium+UnitTest+PO模式搭建基于linux的网页自动化测试框架
使用前需完善data文件夹内的json文件以及page文件夹下__init__.py的路径
1. Base/base.py为web基本操作封装（元素定位、元素点击、多表单切换、截屏、获取文本信息等方法）
2. page为多页面对象封装，将登录、购票和写游记页面各自封装为单独的对象
3. test封装每个页面的功能测试
###  1、登录
![[test_login.png]]
#### 滑动校验功能实现

![[test_trag.png]]
#### 发表游记
![[test_publish.png]]
#### 购票页面
![[test_buyticket.png]]
