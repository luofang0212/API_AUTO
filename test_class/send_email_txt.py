#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import smtplib
from email.mime.text import MIMEText
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from util import get_path
from util.do_logs import TestLog

log = TestLog().getlog()

# 纯发发送文字邮件
class SendEmail:

    def send_email(self):

        now = time.strftime('%Y-%m-%d_%H:%M:%S')  # 获取时间戳
        # 设置服务器所需信息
        mail_host = 'smtp.163.com' # 163邮箱服务器地址
        mail_user = 'warm_homel@163.com'  # 163用户名
        mail_pass = 'love920212'  # 密码(部分邮箱为授权码)
        sender = 'warm_homel@163.com'  # 邮件发送方邮箱地址
        receivers = ['272457044@qq.com']   # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发

        # 设置email信息
        content = now + '测试报告，请查收！！！'
        message = MIMEText(content, 'plain', 'utf-8')  # 邮件内容设置
        message['Subject'] = now + '测试报告'  # 邮件主题
        message['From'] = sender   # 发送方信息
        message['To'] = receivers[0]  # 接受方信息


        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(mail_host, 25)
            # 登录到服务器
            smtpObj.login(mail_user, mail_pass)
            # 发送
            smtpObj.sendmail(
                sender, receivers, message.as_string())
            # 退出
            smtpObj.quit()
            log.info('邮件成功发送到：{0}'.format(receivers))

        except smtplib.SMTPException as e:
            log.info('邮件发送失败：{0}'.format(e))
            raise e


if __name__ == '__main__':
    SendEmail().send_email()
