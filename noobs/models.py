from django.db import models

# Create your models here.
class Query(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Message = models.CharField(max_length=100)

    def __str__(self):
        return self.Name 