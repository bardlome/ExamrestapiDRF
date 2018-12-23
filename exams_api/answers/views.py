from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from answers.serializers import AnswerSerializer

from examtasks.models import Examtask
from exams.models import Exam
from users.models import User
from answers.models import Answer


class AnswersList(generics.ListAPIView):
    """
    API endpoint that lists all answers posted.
    """
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.all()

class AnswerPost(generics.ListCreateAPIView):
    """
    API endpoint that can be used for sending the answer for specific exam tasks, provided by url adress (examtask id = pk).
    """

    serializer_class = AnswerSerializer

    def perform_create(self, serializer, **kwargs):
        myexamtask= Examtask.objects.get(id=self.kwargs.get('pk', ''))
        myexam= Exam.objects.get(examtasks=myexamtask)

        #assuming that we don't want to remember old answers on the same examtask from the same user
        oldanswer = Answer.objects.all().filter(examtask=myexamtask).filter(user=self.request.user)
        oldanswer.delete()
        


        serializer.save( examtask=myexamtask , examowner_id= myexam.user_id , user=self.request.user) 

    def get_queryset(self, **kwargs):
        myexamtask= Examtask.objects.get(id=self.kwargs.get('pk', ''))
        return Answer.objects.all().filter(examtask=myexamtask)
        


class AnswerEdit(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows deleting or modifing the answer (with provided id as pk in URL).
    """
    serializer_class = AnswerSerializer
 
    def get_queryset(self, **kwargs):
        return Answer.objects.all().filter(id=self.kwargs.get('pk', ''))
