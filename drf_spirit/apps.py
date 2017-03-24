from django.apps import AppConfig


class DrfSpiritConfig(AppConfig):
    name = 'drf_spirit'
    verbose_name = "DRF Spirit"

    def ready(self):
        from .signals import send_email_to_topic_people
