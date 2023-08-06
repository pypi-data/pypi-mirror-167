"""
自定义异常
"""


class SMSServiceException(Exception):
    def __init__(self, message):
        self.message = message
