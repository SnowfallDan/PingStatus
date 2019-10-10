#!/usr/bin/env python
# coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('xxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'cn-hangzhou')

def send_msg(phone_numbers, sign_name, template_code, template_param=None):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone_numbers)
    request.add_query_param('SignName', sign_name)
    request.add_query_param('TemplateParam', template_param)
    request.add_query_param('TemplateCode', template_code)

    response = client.do_action(request)
    print(str(response))


def msg_alert(PhoneNumbers, params):
    send_msg(PhoneNumbers, "xxxx", "xxxxxxxxx", params)
