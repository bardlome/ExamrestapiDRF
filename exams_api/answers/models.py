from django.db import models

# Create your models here.
from users.models import User
from examtasks.models import Examtask
import uuid
 
class Answer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('users.User', related_name='asnwering_user', on_delete=models.CASCADE, null=False, default='')
    examtask = models.ForeignKey('examtasks.Examtask', related_name='task_name', on_delete=models.CASCADE, null=False, default='')
    examowner_id = models.IntegerField(editable=False)
    provided_answer = models.CharField(max_length=1000)

    class Meta:
        ordering = ('created',)

