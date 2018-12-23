from django.db import models

# Create your models here.
import uuid
 
class Examtask(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    exam = models.ForeignKey('exams.Exam', related_name='examtasks', on_delete=models.CASCADE, null=False)
    taskname = models.CharField(max_length=100, unique=False, blank=False, null=False)
    examtask_id = models.UUIDField( default=uuid.uuid4, auto_created=True, editable=False, unique=True )
    taskdescription = models.CharField(max_length=1000, unique=False, blank=False, null=False)
    points = models.IntegerField( default=1)
    rightanswer = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)

