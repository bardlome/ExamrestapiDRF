from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from exams import views
from examtasks import views as views2

urlpatterns = [
    url(r'^exams/$', views.ExamList.as_view(), name='exams-list'),
    url(r'^exams/(?P<pk>[0-9]+)/$', views.ExamDetail.as_view(), name='exam-detail'),
    url(r'^exams/(?P<pk>[0-9]+)/examtasks/$', views2.ExamtaskList.as_view(), name='examtasks-list'),
    url(r'^exams/(?P<pk>[0-9]+)/examtasks/(?P<examtask_id>[0-9]+)/$', views2.ExamtaskDetail.as_view(), name='examtask-detail'),
]



