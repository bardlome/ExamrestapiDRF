from django.db import models

# Create your models here.
from exams.models import Exam
from users.models import User
 
 
class Examtask(models.Model):
    #user = models.ForeignKey('users.User', related_name='exams', on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_now_add=True)
    examtask_id = models.IntegerField( default=1,unique=True)
    taskname = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    examinstance = models.ForeignKey('exams.Exam', related_name='examtasks', on_delete=models.CASCADE, null=False)
    taskdescription = models.CharField(max_length=1000, unique=True, blank=False, null=False)
    points = models.IntegerField( default=1,)
    rightanswer = models.CharField(max_length=100, unique=False, blank=False, null=False)
    """
    def save(self, *args, **kwargs):
        #self.exam.save()
        self.examinstance.save()
        super(Examtask, self).save(*args, **kwargs)
    """
 
    class Meta:
        ordering = ('created',)
