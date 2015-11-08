from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^students/$', views.studentList.as_view()),
    url(r'^students/(?P<pk>[0-9]+)/$', views.studentDetail.as_view()),
]