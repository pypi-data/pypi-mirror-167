#!/usr/bin/python
# coding:utf-8
#
# e-mail sender
#
# ::
#     # Send e-mail example
#
#     from net import Mail
#
#     # Set parameters
#     username = 'xxxxxxx@host.com'  # username to login SMTP server
#     password = 'xxxxxxxxxx'      # password to login SMTP server
#     receiver = 'xxxxxxxx@host.com'  # receiver e-mail address
#
#     mail = Mail(username, password)  # Create mail object
#
#     # Send mail with attachment file '1.jpg'
#     mail.send([receiver], 'My Subject', "This is body", ['1.jpg'])
#
#

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.header import Header
import os


class Mail:

    __version__ = '1.0.0'
    """
    A class to send e-mail.

    :Chinese: 发送邮件的类

    ------------------

    # Usage Example:


    # create object

    mail = Mail('sender@host.com', passwd, host='smtp.host.com', sender='sender@host.com')

    # send

    mail.send(['receiver@some.com'], 'the title', 'content text', [filename1, filename2])

    """

    def __init__(self, user, passwd, sender=None, host=None):
        """
        create instance of Mail

        :param user:   username to login SMTP server
        :param passwd: password to login SMTP server
        :param host:   (optional) SMTP server. if empty, detect host by the user parameter.
        :param sender: (optional) sender of the mail. if empty, use the user parameter
        """

        self.user = user      # username to login host
        self.passwd = passwd  # password to login host
        self.host = host      # SMTP server
        self.sender = sender  # sender of the mail

        if sender is None or sender == '':
            self.sender = self.user

        if (host is None or host == '') and user.find('@') > 0:
            host = 'smtp.' + user[user.find('@') + 1:]
            self.host = host

    def send(self, receivers: list, subject: str, body: str, attach_filenames: list = None):
        """
        send a mail

        :param receivers:  list of the e-mail addresses of receivers
        :param subject:    title of the mail
        :param body:    content of the mail
        :param attach_filenames:      (optional) attachment file name list
        
        :return: return True if success, return SMTPException object if failed.
        """
        # SEE: https://www.code-learner.com/python-send-html-image-and-attachment-email-example/

        # validate params
        if isinstance(receivers, str):
            receivers = [receivers]
        if isinstance(receivers, list):
            receivers = '; '.join(receivers)
        else:
            raise ValueError('argument receiver invalid')

        if attach_filenames is None:
            attach_filenames = []

        if isinstance(attach_filenames, str):
            attach_filenames = [attach_filenames]

        if not isinstance(attach_filenames, list):
            raise smtplib.SMTPException('Mail.send() parameter attach_filenames must be a list of filenames')

        # compose mail message
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = receivers
        msg['Subject'] = str(subject)
        msg.attach(MIMEText(str(body), 'html'))

        # add attachment files
        if isinstance(attach_filenames, list):
            count = 0
            for file in attach_filenames:
                file = file.strip(' ')
                if os.path.exists(file):
                    # set attachment mime type
                    mime = MIMEBase("application", "octet-stream")
                    # another example: mime = MIMEBase('image', 'png', filename='img1.png')

                    # read attachment file content into the MIMEBase object
                    mime.set_payload(open(file, "rb").read())

                    # add required header data
                    mime.add_header("Content-Disposition", "attachment",
                                    filename=Header(os.path.basename(file), "utf-8").encode())
                    mime.add_header('X-Attachment-Id', str(count))
                    mime.add_header('Content-ID', '<' + str(count) + '>')  # cid

                    # encode with base64
                    encoders.encode_base64(mime)

                    # add MIMEBase object to MIMEMultipart object
                    msg.attach(mime)

                    count += 1
                else:
                    raise smtplib.SMTPException('Mail.send() attachment file ' + str(file) + ' do not exists')

        smtp_obj = smtplib.SMTP(self.host)
        smtp_obj.login(self.user, self.passwd)
        smtp_obj.sendmail(self.sender, receivers, msg.as_string())
        return True

