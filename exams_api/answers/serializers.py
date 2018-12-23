from rest_framework import serializers
from answers.models import Answer
 
class AnswerSerializer(serializers.ModelSerializer):

    examtask = serializers.ReadOnlyField(source='examtask.id')
    user = serializers.ReadOnlyField(source='user.username')

 
    class Meta:
        model = Answer
        fields = ('id','user', 'examtask', 'provided_answer', 'created','examowner_id',)

