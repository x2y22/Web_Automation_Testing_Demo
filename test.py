import os
import unittest
from tools.log import GetLogger
# import HTMLTestRunner
from HtmlTestRunner import HTMLTestRunner
import page

logger = GetLogger.getLogger()
if __name__ == '__main__':
    try:
        # 加载测试用例
        suite = unittest.defaultTestLoader.discover(page.test_scripts, pattern="test_*.py")

        # 配置HTML报告路径
        report_path = page.report_file
        with open(report_path, 'wb') as f:  # 注意是二进制写入模式
            stream = f,
            runner = HTMLTestRunner(
                report_title='Web去哪儿订票自动化测试报告',
                descriptions=True,
            )
            runner.run(suite)

        logger.info("测试执行成功")
    except:
        logger.error("测试执行失败")
        raise
