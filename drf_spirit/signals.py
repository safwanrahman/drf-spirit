from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

from .emails import send_mass_mail
from .models import Comment


# @receiver(post_save, sender=Comment)
# def send_email_to_topic_people(sender, instance, created, **kwargs):
#     emails = list(instance.topic.comments.exclude(user=instance.user)
#                           .values_list("user__email", flat=True).distinct().iterator())
#     # append the topic creator email
#     emails.append(instance.topic.user.email)
#     # remove duplicates if the topic creator also comments
#     emails = set(emails)
#     subject = _("A new comment has been made")
#     html_template = "drf_spirit/new_comment.html"
#     html_message = render_to_string(html_template)
#     messages = []
#     for email in emails:
#         msg = EmailMultiAlternatives(subject=subject, to=[email])
#         msg.attach_alternative(html_message, "text/html")
#         messages.append(msg)
#
#     send_mass_mail(messages)
