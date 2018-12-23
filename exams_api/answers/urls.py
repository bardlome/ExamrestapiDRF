from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from answers import views

urlpatterns = [
    url(r'^answers/$', views.AnswersList.as_view(), name='answers-list'),
    url(r'^answers/(?P<pk>[0-9]+)/createnew/$', views.AnswerPost.as_view(), name='answer-posting'),
    url(r'^answers/(?P<pk>[0-9]+)/edit/$', views.AnswerEdit.as_view(), name='answer-editing'),
]

