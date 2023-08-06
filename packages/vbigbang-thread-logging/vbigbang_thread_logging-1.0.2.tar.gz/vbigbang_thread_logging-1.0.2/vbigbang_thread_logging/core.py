import os
import platform
import sys
import threading
import queue
import time
import datetime
import logging

__exit_flag = False
s_dont_thread = False


def get_main_path():
    """
    获取主文件运行的路径
    :return: 结尾带 “/”
    """
    full_path = sys.argv[0]
    end_len = len(full_path.split('/')[-1])
    return full_path[:-end_len]


class LoggerT(threading.Thread):
    AQueue = queue.Queue(100000)
    nPID = os.getpid()
    Adt = datetime.datetime.now().strftime('%Y%m%d')
    nCount = 1

    def __init__(self, threadID, name, module, logLevel, dont_thread: bool = False):

        if not hasattr(LoggerT, "_first_init"):
            LoggerT._first_init = True

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.module = module
        self.dont_thread = dont_thread

        print("set loglevel: [%s]" % logLevel)

        file = time.strftime('%Y%m%d__%H_%M_%S', time.localtime(time.time())) + ".log"

        if platform.system().lower() == 'windows':
            main_path = get_main_path() + 'logs/'

            # 创建日志目录
            if not os.path.exists(main_path):
                os.makedirs(main_path)

            main_path = f'{main_path}{module}{file}'
            fileHandler = logging.FileHandler(main_path, mode='w',
                                              encoding='utf-8')
        elif platform.system().lower() == 'linux':
            fileHandler = logging.FileHandler(f'./log/{module}{file}', mode='w', encoding='utf-8')
        else:
            fileHandler = logging.FileHandler(f'./log/{module}{file}', mode='w', encoding='utf-8')

        formatter = logging.Formatter('[%(asctime)s.%(msecs)03d] [%(filename)s:%(lineno)d] %(levelname)s: %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        self.logger = logging.getLogger(__name__)

        self.rHandler = fileHandler
        self.rHandler.setFormatter(formatter)

        self.console = logging.StreamHandler()
        self.console.setFormatter(formatter)

        if logLevel == 'DEBUG':
            self.logger.setLevel(level=logging.DEBUG)
            self.rHandler.setLevel(logging.DEBUG)
            self.console.setLevel(logging.DEBUG)
        elif logLevel == 'INFO':
            self.logger.setLevel(level=logging.DEBUG)
            self.rHandler.setLevel(logging.DEBUG)
            self.console.setLevel(logging.INFO)
        elif logLevel == 'WARNING':
            self.logger.setLevel(level=logging.DEBUG)
            self.rHandler.setLevel(logging.DEBUG)
            self.console.setLevel(logging.WARN)
        elif logLevel == 'ERROR':
            self.logger.setLevel(level=logging.DEBUG)
            self.rHandler.setLevel(logging.DEBUG)
            self.console.setLevel(logging.ERROR)

        self.logger.addHandler(self.rHandler)
        self.logger.addHandler(self.console)

    def __new__(cls, *args, **kwargs):
        if not hasattr(LoggerT, "_instance"):
            LoggerT._instance = object.__new__(cls)
        return LoggerT._instance

    def run(self):
        global __exit_flag
        print("开启日志线程：" + self.name)
        if self.dont_thread:
            self.logger.info('关闭日志线程,使用同步日志')
            return
        while True:
            # data = "queue test data"
            # debug(data)
            # print("Queuesize: %s" % (logging2.AQueue.qsize()))
            if not LoggerT.AQueue.empty():
                # 从队列获取日志消息
                data = LoggerT.AQueue.get()
                # 解析日志消息，格式：日志级别，内容
                level = list(data.keys())[0]
                content = data.get(level)
                # 把内容按分隔符|解析成list传入参数
                if level == 'DEBUG':
                    self.logger.debug(content)
                elif level == 'INFO':
                    self.logger.info(content)
                elif level == 'WARNING':
                    self.logger.warning(content)
                elif level == 'ERROR':
                    self.logger.error(content)

                if content == 'close':
                    print('日志线程关闭')
                    return
            else:
                time.sleep(0.5)

    def debug(self, content):
        self.logger.debug(content)

    def info(self, content):
        self.logger.info(content)

    def warning(self, content):
        self.logger.warning(content)

    def error(self, content):
        self.logger.error(content)

    def close(self):
        self.logger.info('close')


__thread1: LoggerT


def debug(msg):
    if s_dont_thread:
        __thread1.debug(msg)
    else:
        LoggerT.AQueue.put({'DEBUG': msg})


def info(msg):
    if s_dont_thread:
        __thread1.info(msg)
    else:
        LoggerT.AQueue.put({'INFO': msg})


def warning(msg):
    if s_dont_thread:
        __thread1.warning(msg)
    else:
        LoggerT.AQueue.put({'WARNING': msg})


def error(msg):
    if s_dont_thread:
        __thread1.error(msg)
    else:
        LoggerT.AQueue.put({'ERROR': msg})


def init(module, level, dont_thread: bool = False):
    global __thread1, s_dont_thread
    s_dont_thread = dont_thread
    # 创建新线程
    __thread1 = LoggerT(1, "Thread-log", module, level, dont_thread)
    # 开启新线程
    __thread1.start()
    return __thread1


def close():
    info('close')


#  thread1.join()

def tag(log):
    return f'---->>>>>>>>>>>>>>>>>>{log}'


def init_async_logger(module) -> logging.Logger:
    module = f'{module}_'
    logger = logging.getLogger("asyncio")
    file = time.strftime('%Y%m%d__%H_%M_%S', time.localtime(time.time())) + ".log"
    if platform.system().lower() == 'windows':
        main_path = get_main_path() + 'logs/'

        # 创建日志目录
        if not os.path.exists(main_path):
            os.makedirs(main_path)

        main_path = f'{main_path}{module}{file}'
        fileHandler = logging.FileHandler(main_path, mode='w', encoding='utf-8')
    elif platform.system().lower() == 'linux':
        fileHandler = logging.FileHandler(f'./log/{module}{file}', mode='w', encoding='utf-8')
    else:
        fileHandler = logging.FileHandler(f'./log/{module}{file}', mode='w', encoding='utf-8')

    formatter = logging.Formatter('[%(asctime)s.%(msecs)03d] [%(filename)s:%(lineno)d] %(levelname)s: %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    rHandler = fileHandler
    rHandler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger.addHandler(rHandler)
    logger.addHandler(console)

    logger.setLevel(level=logging.DEBUG)
    rHandler.setLevel(logging.DEBUG)
    console.setLevel(logging.DEBUG)
    return logger
