import sqlite3
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
class verifyEmailModel:
    def __init__(self):
        self.connectDatabase()

    def connectDatabase(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)

    def set_email(self, email):
        self.cursor.execute('''SELECT email_address FROM employees WHERE email_address = ?''', (email,))
        result = self.cursor.fetchone()
        if result is None:
            messagebox.showerror('Warning', 'Email Address does not exist')
            return False
        if result:
            return self.send_email(result[0])

    def _generate_otp(self):
        length = 6
        self.otp = ''
        for _ in range(length):
            self.otp += str(random.randint(0, 9))
        return self.otp

    def send_email(self, email):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login('salongamusic40@gmail.com', 'ebef pjjt eovv dkwe')
        # 'ykqz ccoh cmpa rrii' - kurt app password

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = 'salongamusic40@gmail.com'
        msg['To'] = email
        msg['Subject'] = 'Your OTP Code'

        body = self._generate_otp()
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        self.server.send_message(msg)

    def get_otp(self):
        return self.otp