from django.shortcuts import render

# Create your views here.

from examtasks.models import Examtask
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from examtasks.serializers import ExamtaskSerializer
from exams.serializers import ExamSerializer

from rest_framework.views import APIView


class ExamtaskList(generics.ListCreateAPIView):
    """
    #API endpoint that allows exams to be viewed or edited. It is possible to post new exam with "post" button on the bottom. By clicking on the URI adress of already exsting exams we proceed to the place when they can be deleted or modified (by sending "post" request again)
    """
    queryset = Examtask.objects.all()
    serializer_class = ExamtaskSerializer
 
    def perform_create(self, serializer):
        serializer.save()#exam=self.request.exam)

 
class ExamtaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows deleting or modifing the exam tasks (by sending "PUT" request down there)
    """
    serializer_class = ExamtaskSerializer
 
    def get_queryset(self):
        return Examtask.objects.all().filter(exam=self.request.exam)

