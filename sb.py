import smtplib
from email.mime.text import MIMEText

def send_phishing_email(target_email, sender_email, sender_password):
    subject = "Şifrə Yeniləmə Tələb Edilir!"
    body = "Lütfən, aşağidaki linki izləyərək hesabinizi yeniləyin."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = target_email

    # E-poçtu göndərmək
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, target_email, msg.as_string())
    server.quit()

# İstifadə:
send_phishing_email("target@example.com", "your_email@gmail.com", "your_password")


