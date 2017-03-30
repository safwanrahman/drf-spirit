from django.db.models.signals import post_save
from django.dispatch import receiver

from .emails import send_email_to_topic_people
from .models import Comment


@receiver(post_save, sender=Comment)
def post_comment_save(sender, instance, created, **kwargs):
    # Need to send emails to topic people
    send_email_to_topic_people(instance, created)

    # need to update *comment_count of topic if the comment is created
    if created:
        instance.topic.increase_comment_count()
