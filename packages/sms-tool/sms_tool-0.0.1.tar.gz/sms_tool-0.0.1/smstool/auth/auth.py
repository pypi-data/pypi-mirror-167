"""
token获取和过期处理
"""

import time
from smstool.utils.logger import Logger
from smstool.https.api_request import request_for_token
from smstool.utils.exceptions import SMSServiceException

logger = Logger('auth.py')
# 存放token
token = ''
# 当前token下次过期时间
next_expire_time = 0


def get_token(account: str, password: str):
    """
    返回一个必定有效的token
    zgl/2022.09.08
    :param: account 账号
    :param: password 密码
    :return: token
    """
    if not account or type(account) is not str or str.strip(account) == '':
        raise SMSServiceException(f'[auth:get_token()]入参account不存在，account:{account}')
    if not password or type(password) is not str or str.strip(password) == '':
        raise SMSServiceException(f'[auth:get_token()]入参password不存在，password:{password}')
    global token
    global next_expire_time
    # token不存在则获取
    if not token or str.strip(token) == '':
        try:
            token, next_expire_time = request_for_token(account, password)
        except SMSServiceException as e:
            raise e
    # 已存在的token
    else:
        current_time = time.time()
        current_timestamp = int(round(current_time * 1000))
        # 已过期则重新获取
        if current_timestamp >= next_expire_time:
            try:
                token, next_expire_time = request_for_token(account, password)
            except SMSServiceException as e:
                raise e
    return token
