"""
请求http接口
"""

from smstool.utils.values import URLS, RESPONSE_INFO, STABLE_HEADERS
from smstool.utils.exceptions import SMSServiceException
from smstool.https.abstract_func import post
import json


def request_for_token(account: str, password: str):
    """
    请求获取token
    zgl/2022.09.08
    :return: token, expireTime
    """

    # 参数校验
    if not account or type(account) is not str or str.strip(account) == '':
        raise SMSServiceException(f'[api_request:request_for_token()]入参account有误，account:{account}')
    if not password or type(password) is not str or str.strip(password) == '':
        raise SMSServiceException(f'[api_request:request_for_token()]入参password有误，password:{password}')

    # body
    body = {
        'account': account,
        'password': password
    }
    # headers
    headers = {'Content-Type': STABLE_HEADERS['CONTENT_TYPE']}

    # 请求接口
    try:
        response = post(url=URLS['TOKEN'], body_params=body, headers=headers)
        json_res = json.loads(response)
    except SMSServiceException as e:
        raise e

    # 解析响应
    code_obj = json_res[RESPONSE_INFO['CODE_OBJ']]
    code = code_obj[RESPONSE_INFO['RESPONSE_CODE']]
    if code != RESPONSE_INFO['SUCCESS_CODE']:
        message = code_obj[RESPONSE_INFO['RESPONSE_MESSAGE']]
        raise SMSServiceException(f'[api_request:request_for_token()]请求成功，但未取得预期结果，code:{code}，message:{message}')
    else:
        data = json_res[RESPONSE_INFO['DATA']]
        # expireTime为ms级时间戳
        return data['authenticationToken'], data['expireTime']


def request_for_batch_sms(token: str, phone_numbers: list, message_content: str, access_number: str = None):
    """
    发送短信（可一对多群发）
    zgl/2022.09.08
    :param token: token凭证
    :param phone_numbers: 目标电话号码
    :param message_content: 短信内容
    :param access_number: 虚拟接入码
    :return: 短信发送记录，[{'phoneNumber': str, 'msgId': str, 'code': int}, ...]
    """
    # 参数校验
    if not token or type(token) is not str or str.strip(token) == '':
        raise SMSServiceException(f'[api_request:request_for_batch_sms()]token有误，token:{token}')
    if not phone_numbers or type(phone_numbers) is not list:
        raise SMSServiceException(f'[api_request:request_for_batch_sms()]phone_numbers有误，phone_numbers:{phone_numbers}')
    if not message_content or type(message_content) is not str or str.strip(message_content) == '':
        raise SMSServiceException(f'[api_request:request_for_batch_sms()]message_content有误，'
                                  f'message_content:{message_content}')

    # 封装headers
    headers = {
        RESPONSE_INFO['AUTH_NAME']: token,
        'Content-Type': STABLE_HEADERS['CONTENT_TYPE']
    }
    # 封装body
    body = {'phoneNumbers': phone_numbers, 'messageContent': message_content, 'accessNumber': access_number}

    # 请求接口
    try:
        response = post(url=URLS['BATCH_SMS'], body_params=body, headers=headers)
        json_res = json.loads(response)
    except SMSServiceException as e:
        raise e

    # 解析响应
    code_obj = json_res[RESPONSE_INFO['CODE_OBJ']]
    code = code_obj[RESPONSE_INFO['RESPONSE_CODE']]
    if code != RESPONSE_INFO['SUCCESS_CODE']:
        message = code_obj[RESPONSE_INFO['RESPONSE_MESSAGE']]
        raise SMSServiceException(f'[api_request:request_for_batch_sms()]请求成功，但未取得预期结果，code:{code}，message:{message}')
    else:
        data = json_res[RESPONSE_INFO['DATA']]
        return data


def request_for_p2p_sms(token: str, params_list: list):
    """
    发送短信（批量点对点单发）
    zgl/2022.09.08
    :param token: token凭证
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
    # 参数校验
    if not token or type(token) is not str or str.strip(token) == '':
        raise SMSServiceException(f'[api_request:request_for_p2p_sms()]token有误，token:{token}')
    if not params_list or type(params_list) is not list:
        raise SMSServiceException(f'[api_request:request_for_p2p_sms()]params_list有误，params_list:{params_list}')
    else:
        for x in params_list:
            if not x['phoneNumber'] or type(x['phoneNumber']) is not str or str.strip(x['phoneNumber']) == '':
                raise SMSServiceException(f"[api_request:request_for_p2p_sms()]params_list存在某元素的phoneNumber有误, "
                                          f"phoneNumber:{x['phoneNumber']}")
            if not x['messageContent'] or type(x['messageContent']) is not str or str.strip(x['messageContent']) == '':
                raise SMSServiceException(f"[api_request:request_for_p2p_sms()]params_list存在某元素的messageContent有误, "
                                          f"messageContent:{x['messageContent']}")

    # 封装headers
    headers = {
        RESPONSE_INFO['AUTH_NAME']: token,
        'Content-Type': STABLE_HEADERS['CONTENT_TYPE']
    }

    # 请求接口
    try:
        response = post(url=URLS['P2P_SMS'], body_params=params_list, headers=headers)
        json_res = json.loads(response)
    except SMSServiceException as e:
        raise e

    # 解析响应
    code_obj = json_res[RESPONSE_INFO['CODE_OBJ']]
    code = code_obj[RESPONSE_INFO['RESPONSE_CODE']]
    if code != RESPONSE_INFO['SUCCESS_CODE']:
        message = code_obj[RESPONSE_INFO['RESPONSE_MESSAGE']]
        raise SMSServiceException(f'[api_request:request_for_p2p_sms()]请求成功，但未取得预期结果，code:{code}，message:{message}')
    else:
        data = json_res[RESPONSE_INFO['DATA']]
        return data
