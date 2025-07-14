import logging.handlers
import threading
import page

""" 单例实现logger """
class GetLogger:
    logger = None
    _lock = threading.Lock()  # 线程安全
    # classmethod 是设置类方法，可以不用类实例化即可调用里面的方法，实例化也能
    @classmethod
    def getLogger(cls):
        if not cls.logger:
            # 获取日志器
            with cls._lock:  # 加锁防止多线程竞争
                if cls.logger is None:  # 双重检查锁定
                    logger = logging.getLogger("admin")

                    # 设置日志器的级别
                    logger.setLevel(logging.INFO)

                    # 清理现有处理器（防止重复添加）
                    logger.handlers.clear()

                    # 获取控制台的处理器
                    sh = logging.StreamHandler()

                    # 获取文件处理器，以时间分割
                    th = logging.handlers.TimedRotatingFileHandler(filename=page.log_file, when="M", interval=1,
                                                                   backupCount=3, encoding="utf-8", delay=True)

                    # 设置格式器
                    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s] (%(funcName)s:%(lineno)d) - %(message)s"
                    fm = logging.Formatter(fmt)

                    # 将格式器加入处理器中
                    sh.setFormatter(fm)
                    th.setFormatter(fm)

                    # 将处理器添加到日志器中
                    logger.addHandler(sh)
                    logger.addHandler(th)
        return logger

