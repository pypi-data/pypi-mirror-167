"""
sms服务发起
"""

from .auth.auth import get_token
from .https.api_request import request_for_batch_sms, request_for_p2p_sms
from .utils.exceptions import SMSServiceException
from .utils.values import REGEX
import re


def http_batch_sms(account: str, password: str, phone_numbers: list, message_content: str, access_number: str = None):
    """
    调用此函数发起sms批量短信发送服务
    zgl/2022.09.08
    :param account: 客户账号
    :param password: 客户账号密码
    :param phone_numbers: 目标手机号
    :param message_content: 短信内容
    :param access_number: 虚拟接入码。非必填
    :return: 短信发送记录，[{'phoneNumber': str, 'msgId': str, 'code': int}, ...]
    """
    # 入参校验
    if not account or type(account) is not str or str.strip(account) == '':
        raise SMSServiceException(f'[sms_tool:http_batch_sms()]入参account有误，account:{account}')
    if not password or type(password) is not str or str.strip(password) == '':
        raise SMSServiceException(f'[sms_tool:http_batch_sms()]入参password有误，password:{password}')
    if not phone_numbers or type(phone_numbers) is not list:
        raise SMSServiceException(f'[sms_tool:http_batch_sms()]入参phone_numbers有误，phone_numbers:{phone_numbers}')
    else:
        for x in phone_numbers:
            if not x or type(x) is not str or str.strip(x) == '' or not re.search(REGEX['MOBILE_PHONE'], x):
                raise SMSServiceException(f"[api_request:http_batch_sms()]phone_numbers存在某元素有误, phoneNumber:{x}")
    if not message_content or type(message_content) is not str or str.strip(message_content) == '':
        raise SMSServiceException(f'[sms_tool:http_batch_sms()]入参message_content有误，'
                                  f'message_content:{message_content}')
    # 获取token
    token = get_token(account, password)
    # 调用api
    return request_for_batch_sms(token, phone_numbers, message_content, access_number)


def http_p2p_sms(account: str, password: str, params_list: list):
    """
    调用此函数发起sms点对点短信发送服务
    zgl/2022.09.08
    :param account: 客户账号
    :param password: 客户账号密码
    :param params_list: sms参数列表，结构如下：
        [
            {
                'phoneNumber': str,
                'messageContent': str,
                'bizId': str,
                'accessNumber': str
            },
            ...
        ]
    :return: 短信发送记录，[{'phoneNumber': str, 'msgId': str, 'code': int}, ...]
    """
    # 入参校验
    if not account or type(account) is not str or str.strip(account) == '':
        raise SMSServiceException(f'[api_request:http_p2p_sms()]入参account有误，account:{account}')
    if not password or type(password) is not str or str.strip(password) == '':
        raise SMSServiceException(f'[api_request:http_p2p_sms()]入参password有误，password:{password}')
    if not params_list or type(params_list) is not list:
        raise SMSServiceException(f'[api_request:http_p2p_sms()]params_list有误，params_list:{params_list}')
    else:
        for x in params_list:
            if not x['phoneNumber'] or type(x['phoneNumber']) is not str or str.strip(x['phoneNumber']) == '' \
                    or not re.search(REGEX['MOBILE_PHONE'], x['phoneNumber']):
                raise SMSServiceException(f"[api_request:http_p2p_sms()]params_list存在某元素的phoneNumber有误, "
                                          f"phoneNumber:{x['phoneNumber']}")
            if not x['messageContent'] or type(x['messageContent']) is not str or str.strip(x['messageContent']) == '':
                raise SMSServiceException(f"[api_request:http_p2p_sms()]params_list存在某元素的messageContent有误, "
                                          f"messageContent:{x['messageContent']}")
    # 获取token
    token = get_token(account, password)
    # 调用api
    return request_for_p2p_sms(token, params_list)
