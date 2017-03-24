from django.core import mail


def send_mass_mail(messages):
    connection = mail.get_connection()
    connection.send_messages(messages)
