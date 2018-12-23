from rest_framework import serializers
 
from examtasks.models import Examtask
 
class ExamtaskSerializer(serializers.ModelSerializer):
    exam = serializers.ReadOnlyField(source='exam.name')


 
    class Meta:
        model = Examtask
        fields = ( 'id', 'examtask_id', 'exam','created', 'taskname', 'taskdescription', 'points', 'rightanswer')

