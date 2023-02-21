from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class CallLog(models.Model):
    id = models.AutoField(primary_key=True)
    from_number = models.CharField(max_length=10)
    to_number = models.CharField(max_length=10)
    start_time = models.DateTimeField(auto_now_add=True)
    


