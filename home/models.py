from django.db import models

# Create your models here.
class CRUD(models.Model):

    title = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
        return f'{self.title}'
    