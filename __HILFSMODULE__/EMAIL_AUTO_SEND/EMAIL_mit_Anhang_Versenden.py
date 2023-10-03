import smtplib
import mimetypes
from email.message import EmailMessage


# E-Mail-Objekt initialisieren und Nachrichtentext setzen:
msg = EmailMessage()
msg['Subject'] = 'Diese E-mail enthält einen Anhang'
msg['From'] = 'Von Mustermann <danilov.a@gmx.net>'
msg['To'] = 'danilov.a@gmx.net'


# Set text content
msg.set_content('Im Anhang befinden sich der Aktuelle Abfuhrkalender als PDF Datei')


# Funktion: Anhang anhängen
def attach_file_to_email(email, filename):
    """Attach a file identified by filename, to an email message"""
    with open(filename, 'rb') as fp:
        file_data = fp.read()
        maintype, _, subtype = (mimetypes.guess_type(filename)[0] or 'application/octet-stream').partition("/")
        email.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=filename)


# Funktion: E-Mail per SMTP senden
def send_mail_smtp(mail, host, username, password):
    s = smtplib.SMTP(host)
    s.starttls()
    s.login(username, password)
    s.send_message(mail)
    s.quit()


# Funktionsaufruf: Anhang anhängen
attach_file_to_email(msg, "Abfallkalender.pdf")


# Funktionsaufruf: E-Mail per SMTP senden
send_mail_smtp(msg, 'mail.gmx.net', 'danilov.a@gmx.net', '@lfer$A-379-Gmx')
print("Ende")
