from django.shortcuts import render

# Create your views here.

from exams.models import Exam
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from exams.serializers import ExamSerializer


class ExamList(generics.ListCreateAPIView):
    """
    API endpoint that allows exams to be viewed or edited. It is possible to post new exam with "post" button on the bottom. By clicking on the URI adress of already exsting exams we proceed to the place when they can be deleted or modified (by sending "post" request again)
    """
    queryset = Exam.objects.all()  #all().order_by('-id')
    serializer_class = ExamSerializer
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class ExamDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Here is the place when one can delete or modify the exam (by sending "put" request)
    """
    serializer_class = ExamSerializer
 
    def get_queryset(self):
        return Exam.objects.all().filter(user=self.request.user)
