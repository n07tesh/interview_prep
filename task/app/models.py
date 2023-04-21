from django.db import models

# Create your models here.
class User(models.Model):
    auto_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20,blank=True)
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=40,blank=True)

    class Meta:
        def __str__(self):
            return self.auto_id + ' ' + self.user_name