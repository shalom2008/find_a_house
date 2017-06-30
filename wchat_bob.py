from wxpy import *
from wechat_sender import *
import cx_Oracle

bot = Bot()

@bot.register(Friend, TEXT)
def auto_reply(msg):
    if msg.text == '帮助':
        return "发送‘考勤’，以获取你的考勤信息"

embed()

