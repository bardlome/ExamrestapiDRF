from rest_framework import serializers
 
from examtasks.models import Examtask
from exams.models import Exam

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
class ExamtaskSerializer(serializers.HyperlinkedModelSerializer):
    examinstance = ExamSerializer()
    user = serializers.ReadOnlyField(source='users.User')

    def create(self, validated_data):
        examtask = Examtask(
            examinstance=validated_data.get('exams.Exam')#, None)
        )
        examtask.save()
        return user
 
    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
 
    class Meta:
        model = Examtask
        fields = ('url', 'examtask_id', 'created','user', 'examinstance','taskname', 'taskdescription','points','rightanswer')#(__all__)#
        extra_kwargs = {
            'url': {
                'view_name': 'examtasks:examtask-detail',
            }
	}

