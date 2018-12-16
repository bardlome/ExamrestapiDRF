from rest_framework import serializers
 
from exams.models import Exam
from examtasks.models import Examtask
#from examtasks.serializers import ExamtaskSerializer
 
class ExamSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
   
    class Meta:
        model = Exam
        fields = ('url', 'id', 'created', 'examname', 'user', 'examtasks')
        if Exam.examtasks==True:
                extra_kwargs = {
                    'url': {
                        'view_name': 'exams:exam-detail',
                    },            
                    'examtasks': {
                        'view_name': 'examtasks:examtask-detail',
                    }
	        }
        else:
                extra_kwargs = {
                    'url': {
                        'view_name': 'exams:exam-detail',
                    }
	        }
