import logging
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s-%(filename)s [line:%(lineno)d]%(levelname)s: %(message)s')
# 开始使用 log 功能
logging.debug('这是 Loggging debug message')
logging.info('这是 loggging info message')
logging.warning('这是 Loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')
