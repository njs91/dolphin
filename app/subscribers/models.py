from django.db import models
from accounts.models import Account


class Subscriber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True)
    # tags = _________________ many to many field, with later option of users being able to define custom tags
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    verified = models.BooleanField(default=False)
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    list_display = ('first_name', 'email', 'date_joined', 'verified')
