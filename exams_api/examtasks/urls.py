from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from examtasks import views


urlpatterns = [
    url(r'^examtasks/$', views.ExamtaskListAll.as_view(), name='examtasks-list'),
    url(r'^examtasks/(?P<pk>[0-9]+)/createnew/$', views.ExamtaskAdd.as_view(), name='examtask-add'),
    url(r'^examtasks/(?P<pk>[0-9]+)/edit/$', views.ExamtaskEdit.as_view(), name='examtask-edit'),
]



