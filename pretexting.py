import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_pretexting_email(target_email, sender_email, sender_password, fake_name):
    # Saxta e-poçt mövzusu və məzmunu
    subject = "Hesabinizi Təhlükəsizləşdirmək üçün Təcililədilmiş Dəstək"
    body = f"""
    Salam,

    Mən {fake_name}-dən {fake_name} şirkətinin təhlükəsizlik bölməsindənəm. Hesabinizin təhlükəsizliyini artirmaq üçün bir neçə dəyişikliyə ehtiyac var. 
    Zəhmət olmasa, aşaği+daki linki izləyərək öz məlumatlarinizi yeniləyin:

    http://fake-phishing-link.com

    Diqqətinizə görə təşəkkür edirik!
    """

    # MIME mesajını qururuq
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = target_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # SMTP serverinə qoşuluruq və e-poçtu göndəririk
    try:
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # TLS ilə əlaqə qururuq
        server.login(sender_email, sender_password)  # Gmail hesabına daxil oluruq
        text = msg.as_string()
        server.sendmail(sender_email, target_email, text)  # E-poçtu göndəririk
        server.quit()
        print("E-poçt göndərildi!")
    except Exception as e:
        print(f"E-poçt göndərərkən xəta baş verdi: {e}")

# İstifadə:
send_pretexting_email("target@example.com", "your_email@gmail.com", "your_password", "John Doe")
