from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)

    image = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_liked = models.ManyToManyField(User)
    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return self.event_name