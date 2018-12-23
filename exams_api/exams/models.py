from django.db import models

# Create your models here.
from users.models import User
import uuid
  
 
class Exam(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey('users.User', related_name='exams', on_delete=models.CASCADE, null=False)
    exam_id = models.UUIDField( default=uuid.uuid4, auto_created=True, editable=False, unique=True )
  
    class Meta:
        ordering = ('created',)
