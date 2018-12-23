from django.shortcuts import render

# Create your views here.

from examtasks.models import Examtask
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from examtasks.serializers import ExamtaskSerializer
from exams.models import Exam

class ExamtaskListAll(generics.ListAPIView):
    """
    API endpoint that lists all exam tasks.
    """
    serializer_class = ExamtaskSerializer

    def get_queryset(self):
        return Examtask.objects.all()


class ExamtaskAdd(generics.ListCreateAPIView):
    """
    API endpoint that lists exam tasks from specific exam, provided by url adress (exam id = pk). Here one can also allows add new examtask to this specified exam.
    """
    serializer_class = ExamtaskSerializer
 
    def perform_create(self, serializer, **kwargs):
        myexam= Exam.objects.get(id=self.kwargs.get('pk', ''))
        serializer.save(exam=myexam)

    def get_queryset(self, **kwargs):
        myexam= Exam.objects.get(id=self.kwargs.get('pk', ''))
        return Examtask.objects.all().filter(exam=myexam)


class ExamtaskEdit(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows deleting or modifing the exam tasks.
    """
    serializer_class = ExamtaskSerializer
 
    def get_queryset(self, **kwargs):
        return Examtask.objects.all().filter(id=self.kwargs.get('pk', ''))
