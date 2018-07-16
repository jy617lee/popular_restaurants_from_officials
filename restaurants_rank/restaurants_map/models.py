from django.db import models
from django.utils import timezone

# Create your models here.
class Email(models.Model):
    email_addr = models.EmailField(max_length=70, blank=True, null=True)
    register_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.email_addr
