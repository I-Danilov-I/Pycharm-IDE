import smtplib
import time
from email.mime.text import MIMEText


def email_versenden(text, betreff):
    MEINE_ADRESSE = 'danilov.a@gmx.net'
    PASSWORT = '$kylinE-3#gm'

    mail = MIMEText(text)
    mail["From"] = "   Selection of girls for your taste <danilov.a@gmx.net>"
    mail["To"] = "y.baver@appos.com.ua"
    mail["Subject"] = betreff

    sender = smtplib.SMTP("mail.gmx.net", 587)
    sender.ehlo()
    sender.starttls()
    sender.ehlo()

    sender.login(MEINE_ADRESSE, PASSWORT)
    sender.send_message(mail)
    sender.close()


TEXT = "Registration takes place in a couple of stages, indicate your gender, age, location and your sexual interests."


i = 0
while True:
    i += 1
    email_versenden(TEXT, "Betreff")
    if i < 1000:
        print("Versende zum", i, "Mal")
        print("Email:", i, "versendet")
        time.sleep(1)

    else:
        print(i, "Wurden erfolgreich versendet!")
        break
