import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'zoeerispe7@gmail.com'
receiver_email_id = 'thapelo@lifechoices.co.za, terblancheronald@gmail.com'
password = input("Enter your password")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = receiver_email_id
msg['Subject'] = subject
body = "Good afternoon gentlemen.\n"
body = body + "Today is a wonderful day and I hope the weekend goes even better."
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender_email_id, password)
s.sendmail(sender_email_id, receiver_email_id, text)
s.quit()
