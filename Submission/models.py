from django.conf import settings
from django.db import models
from Rooms.models import room


# Create your models here.
class Submission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # used in django
    assignment = models.ForeignKey(room, on_delete=models.CASCADE)

    date = models.DateField()


