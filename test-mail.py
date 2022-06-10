import imaplib
import base64, re, email
import base64
def getcodeoutlook():
    try:
        email_user = "g9Hl8Pj3Qx6A@hotmail.com"
        email_pass = "d6X*t5F<e0Z)z4O!"
        mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
        mail.login(email_user, email_pass)
        mail.list()
        mail.select('Inbox')
        for num in range(1, 4):
            ty, data = mail.fetch(str(num), '(RFC822)')
            k = re.findall('To verify your account, enter this code in TikTok:.*?Verification codes expire after 48 hours.', str(data))
            if k != []:
                code = re.findall('\d{6}', k[0])[0]
                return code
            else:
                return ""
        mail.close()
        mail.logout()
    except imaplib.IMAP4.error:
        return "loginfail"
print(getcodeoutlook())
