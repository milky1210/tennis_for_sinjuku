import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

def send():
    FROM_ADRESS = "mitukifukumoto@gmail.com"
    PASSWORD = "momoclo3150"
    TO_ADRESS = "mitukifukumoto@gmail.com"
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADRESS, PASSWORD)

    #メールの内容を記述
    msg = MIMEText('アクセスに成功しました。')
    msg['Subject'] = 'MACPCからの送信テスト'
    msg['From'] = FROM_ADRESS
    msg['To'] = TO_ADRESS
    msg['Date'] = formatdate()
    smtpobj.sendmail(FROM_ADRESS,TO_ADRESS,msg.as_string())
    smtpobj.close()
