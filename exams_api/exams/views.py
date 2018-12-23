from django.shortcuts import render

# Create your views here.

from exams.models import Exam
from examtasks.models import Examtask
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from exams.serializers import ExamSerializer
from exams.serializers import ExamtaskSerializer
from rest_framework.filters import OrderingFilter

class AllTaskFromExamList(generics.ListAPIView):
    """
    API endpoint that lists all examtasks to resolve, from the provided exam.
    """
    serializer_class = ExamtaskSerializer

    def get_queryset(self, **kwargs):
        myexam=Exam.objects.get(id=self.kwargs.get('pk', ''))
        return Examtask.objects.values('taskname','taskdescription','rightanswer','id').filter(exam=myexam)


class ExamList(generics.ListCreateAPIView):
    """
    API endpoint that allows exams to be viewed or edited. It is possible to post new exam with "post" button on the bottom. By clicking on the URI adress of already exsting exams we proceed to the place when they can be deleted or modified (by sending "post" request again)
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    filter_backends = (OrderingFilter,)
    ordering_fields = ('name', 'created', 'id', )
    ordering = ('created',)
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class ExamDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Here is the place when one can delete or modify the exam (by sending "post" request again)
    """
    serializer_class = ExamSerializer
 
    def get_queryset(self):
        return Exam.objects.all().filter(user=self.request.user)
