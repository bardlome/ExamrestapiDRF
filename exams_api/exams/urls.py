from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from exams import views

urlpatterns = [
    url(r'^exams/$', views.ExamList.as_view(), name='exams-list'),
    url(r'^exams/(?P<pk>[0-9]+)/$', views.ExamDetail.as_view(), name='exam-detail'),
    url(r'^exams/listoftasks/(?P<pk>[0-9]+)/$', views.AllTaskFromExamList.as_view(), name='exam-examtasks'),
]



    
