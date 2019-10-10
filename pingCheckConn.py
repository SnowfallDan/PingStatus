#!/usr/bin/python
# coding=utf-8

# MIT License

# Copyright (c) 2019 SnowfallDan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
from alertModule.msgAlert import msg_alert
from pingModule.ping import verbose_ping

# get local IP address
import socket
local_ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))

# ping remote ip or url address
remote_ip = "www.baidu.com"

# connection status
ping_status = "INIT"

# alert phone number
phone_number = 13888888888

if __name__ == '__main__':
    while True:
        # ping once and get result
        status = verbose_ping(remote_ip, 5, 1)  # timeout = 2, count = 1
        print("Ping Result is " + status)
        if status is "DOWN":
            if ping_status is "INIT" or ping_status is "UP":
                Contents = "NetworkFailure"
                Msg = local_ip + " Lost Connection To " + remote_ip
                params = {"ruleName": Contents, "message": Msg}
                print(params)
                alert_res = msg_alert(phone_number, params)
                print(alert_res)

                ping_status = "DOWN"
            else:
                time.sleep(60)
                continue
        elif status is "UP":
            ping_status = "UP"
            time.sleep(60)
            continue
        else:
            print("Please Check Local Network！")
            ping_status = "DOWN"
            time.sleep(60)

        print("Now Status is " + ping_status)
