from django.db import models

# Create your models here.
class tdl(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    writtendate = models.DateField(auto_now_add=True)
    is_end = models.BooleanField(default=False)
    is_priority = models.BooleanField(default=False)
