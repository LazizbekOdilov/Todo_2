from django.db import models
from django.contrib.auth.models import  User

class Reja(models.Model):
    t_name = models.CharField(max_length=30)
    t_datail = models.TextField()
    sana = models.DateField()
    t_status = models.CharField(max_length=30)
    egasi = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.t_name}"