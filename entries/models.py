from django.db import models # gets model class to inherit for our models
from django.utils import timezone # timezone is a datafield used to mark time of creation

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    # equivalent of to_string()
    def __str__(self): 
        return self.title
    
    class Meta:
        verbose_name_plural = "Entries"
