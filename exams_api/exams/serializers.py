from rest_framework import serializers
 
from exams.models import Exam
from examtasks.serializers import ExamtaskSerializer
 
class ExamSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    examtasks = ExamtaskSerializer(
        many=True,
        read_only=True
    )
 
    class Meta:
        model = Exam
        fields = ('url', 'id','exam_id',  'created', 'name', 'user', 'examtasks')
        extra_kwargs = {
            'url': {
                'view_name': 'exams:exam-detail',
            }
	}


