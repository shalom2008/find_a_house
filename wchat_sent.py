from wechat_sender import Sender
import sys

msg = 'it is a bot send message to u'
target = '南飞风'
Sender().send_to(msg, search=target)
