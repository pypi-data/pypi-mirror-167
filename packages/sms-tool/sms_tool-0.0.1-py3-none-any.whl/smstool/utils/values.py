"""
一些常量
"""


""" 请求地址 """
URLS = {
    'TOKEN': 'https://gateway.dev.codebetterlife.com/api/v2/auth',
    'BATCH_SMS': 'https://gateway.dev.codebetterlife.com/api/v2/send',
    'P2P_SMS': 'https://gateway.dev.codebetterlife.com/api/v2/p2p'
}

""" 后台统一http响应相关信息 """
RESPONSE_INFO = {
    'CODE_OBJ': 'resultCode',
    'DATA': 'data',
    'RESPONSE_CODE': 'code',
    'RESPONSE_MESSAGE': 'message',
    'SUCCESS_CODE': 0,
    'AUTH_NAME': 'Authorization'
}

""" 后台api固定headers """
STABLE_HEADERS = {
    'CONTENT_TYPE': 'application/json;charset=utf-8'
}

""" 正则 """
REGEX = {
    'MOBILE_PHONE': '^1(3\\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\\d|9[0-35-9])\\d{8}$'
}
