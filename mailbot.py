import smtplib
from email.mime.text import MIMEText
from email.mime.multipart  import MIMEMultipart

# environment variables
username='swamisharanam43@gmail.com'
password='punnu2202'

def mailbot(text='Email Body', subject='Dis E-mail from a bot', to_email=[],html=None,from_email='swamisharanam43@gmail.com'):
    text = ''' If you are recieving this mail you have reached Mr Swami Don,This is a fake account.If You got this email from Psycoder he probably doesn't care for you,So mailing this email is no use.<br>
Now Dis email from a bot.Dont reply and dont expect a different reply.<br>

Peace Loser,<br>
<div style='color:ff0000'>3< 3< Psycoder <3<3</div>'''
    assert isinstance(to_email,list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_email)
    msg['Subject'] = subject

    txt_part = MIMEText(text,'plain')
    msg.attach(txt_part)
    if html!=None:
        html_part = MIMEText("<h1>"+text+"</h1>", 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()
# login to my SMTP server
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_email,msg_str)
    server.quit()
    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass
    return 200


mailbot(to_email=['papparusu10@gmail.com'])
