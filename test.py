import os
import unittest
from tools.log import GetLogger
import HTMLTestRunner
logger = GetLogger.getLogger()

if __name__ == '__main__':
    try:
        # 加载测试用例
        suite = unittest.defaultTestLoader.discover(
            'D:/PyCharm Community Edition 2023.2.2/project/Web-Auto-Testing/scripts/', pattern="test_*.py")

        # 配置HTML报告路径
        report_dir = os.path.join('E:/ZXY/Web-Auto-Testing/', "reports")
        report_path = 'E:/ZXY/Web-Auto-Testing/reports/TestReport.html'
        with open(report_path, 'wb') as f:  # 注意是二进制写入模式
            runner = HTMLTestRunner.HTMLTestRunner(
                stream=f,  # 必须参数
                title='自动化测试报告',
                description='测试执行详情'
            )
            runner.run(suite)

        logger.info("测试执行成功")
    except:
        logger.error("测试执行失败")
        raise
