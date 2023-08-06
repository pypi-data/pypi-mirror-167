"""
封装http请求函数
"""

import requests
from smstool.utils.exceptions import SMSServiceException
from smstool.utils.logger import Logger

logger = Logger('abstract_func.py')
# 隐藏跳过ssl证书验证的警告
requests.packages.urllib3.disable_warnings()


def get(url: str, query_params: dict = None, headers: dict = None):
    """
    get请求
    :param url: 请求地址
    :param query_params: query参数
    :param headers: header参数
    :return: Object
    zgl/2022.09.08
    """
    # url校验
    if not url or type(url) is not str or str.strip(url) == '':
        raise SMSServiceException(f'[abstract_func:get()]请求地址url有误，url:{url}')
    # 拼接真实url
    true_url = url
    if query_params:
        if type(query_params) is not dict:  # 对于集合类型，if val的结果：{}、[]、()都为False，故此处不需验证元素是否为空
            raise SMSServiceException(f'[abstract_func:get()]函数收到了query_params，但其值有误，query_params:{query_params}')
        else:
            true_url += '?'
            for one_key in query_params.keys():
                true_url = true_url + str(one_key) + '=' + str(query_params[one_key]) + '&'
            # 去掉末尾多于的'&'
            true_url = true_url[:-1]
    # headers校验
    if headers and type(headers) is not dict:
        raise SMSServiceException(f'[abstract_func:get()]函数收到了headers，但其值有误，headers:{headers}')
    # 发起请求
    try:
        if headers:
            response = requests.get(url=true_url, headers=headers, verify=False)
        else:
            response = requests.get(url=true_url, verify=False)
    except Exception as e:
        logger.exception(f'[abstract_func:get()]请求{true_url}异常', e)
        raise SMSServiceException(f'[abstract_func:get()]请求{true_url}异常')
    # 解析响应
    try:
        return response.text
    except Exception as e:
        logger.exception(f'[abstract_func:get()]解析{true_url}的响应结果异常', e)
        raise SMSServiceException(f'[abstract_func:get()]解析{true_url}的响应结果异常')


def post(url: str, query_params: dict = None, body_params: any = None, headers: dict = None):
    """
    post请求
    zgl/2022.09.08
    :param url: 请求地址
    :param query_params: query参数
    :param body_params: body参数
    :param headers: header参数
    :return: Object
    """
    # url校验
    if not url or type(url) is not str or str.strip(url) == '':
        raise SMSServiceException(f'[abstract_func:post()]请求地址url有误，url:{url}')
    # 拼接真实url
    true_url = url
    if query_params:
        if type(query_params) is not dict:  # 对于集合类型，if val的结果：{}、[]、()都为False，故此处不需验证元素是否为空
            raise SMSServiceException(f'[abstract_func:post()]函数收到了query_params，但其值有误，query_params:{query_params}')
        else:
            true_url += '?'
            for one_key in query_params.keys():
                true_url = true_url + str(one_key) + '=' + str(query_params[one_key]) + '&'
            # 去掉末尾多于的'&'
            true_url = true_url[:-1]
    # body校验
    if not body_params or (type(body_params) is not dict and type(body_params) is not list):
        raise SMSServiceException(f'[abstract_func:post()]函数收到了body_params，但其值有误，body_params:{body_params}')
    # headers校验
    if headers and type(headers) is not dict:
        raise SMSServiceException(f'[abstract_func:post()]函数收到了headers，但其值有误，headers:{headers}')
    # 发起请求
    try:
        if headers:
            if body_params:
                response = requests.post(url=true_url, json=body_params, headers=headers, verify=False)
            else:
                response = requests.post(url=true_url, headers=headers, verify=False)
        else:
            if body_params:
                response = requests.post(url=true_url, json=body_params, verify=False)
            else:
                response = requests.post(url=true_url, verify=False)
    except Exception as e:
        logger.exception(f'[abstract_func:post()]请求{true_url}异常', e)
        raise SMSServiceException(f'[abstract_func:post()]请求{true_url}异常')
    # 解析响应
    try:
        return response.text
    except Exception as e:
        logger.exception(f'[abstract_func:post()]解析{true_url}的响应结果异常', e)
        raise SMSServiceException(f'[abstract_func:post()]解析{true_url}的响应结果异常')
