import os
import sys
from tornado.web import Application

RESPONSE_OK = 0  # 请求正常
RESPONSE_NO_METHOD_ERROR = -1  # 微服务异常
RESPONSE_SERVICE_ERROR = -2  # 微服务异常
RESPONSE_VALIDATE_ERROR = -3  # 返回结果参数校验失败
RESPONSE_SQL_ERROR = -4  # 数据库操作异常
RESPONSE_THIRD_ERROR = -5  # 第三方服务调用异常
RESPONSE_SYS_BUSY = -5  # 系统繁忙，微事务同步
TRANS_TASK_FAIL = -7  # 微事务 task 同步失败
PARSE_ERROR_REQ_P = -8  # 参数格式不正确
SESS_DEBUG = ('ss_debug' in sys.argv)  # db直接崩溃好找问题
UNITTEST = 'un_debug' in sys.argv  # 单元测试 debug 区分于使用微服务debug


def sh_application(path_api, server_name, debug, autoreload):
    """
    将sh_routers 注册到Tornado框架中
    """
    from magpielib.handler.patchhandler import TaskHandler
    from magpielib.parse import parse_apis
    routers = []
    _handler_map = {}  # 单纯的校验 handler 是否有重复
    _url_map = {}  # 单纯的校验 uri 是否有重复
    sh_routers = parse_apis(path_api, server_name)
    if not sh_routers:
        raise Exception("请配置apis yaml 文件！")
    for sh_router in sh_routers:
        if sh_router.handler in _handler_map and sh_router.handler != TaskHandler:
            raise Exception("不同的uri 不能注册到同一个handler上->%s" % sh_router.handler)
        if sh_router.uri in _url_map:
            raise Exception("uri不能重复 ->%s" % sh_router.uri)
        _handler_map[sh_router.handler] = ''
        _url_map[sh_router.uri] = ''
        routers.append((sh_router.uri, sh_router.handler))
    app = Application(routers, debug=debug, autoreload=autoreload, gzip=True)
    return app


def parse_env():
    """
    解析全局的环境变量
    """
    _ServiceConst = type('__SERVICES__', (object,), dict())()
    env = os.environ
    for k, v in env.items():
        _ServiceConst.__setattr__(k, v)
    return _ServiceConst


# 服务地址发现，每个服务都需要维护，从本地环境变量中获取
ServiceConst = parse_env()
