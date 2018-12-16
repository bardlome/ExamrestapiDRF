from django.db import models

# Create your models here.
from users.models import User
 
class Exam(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    examname = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey('users.User', related_name='exams', on_delete=models.CASCADE, null=False)
    examtasks = None# models.AutoField()
    id= models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),

    class Meta:
        ordering = ('created',)
