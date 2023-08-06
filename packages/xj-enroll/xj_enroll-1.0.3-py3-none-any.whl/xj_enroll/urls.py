from django.urls import re_path

from .api.enroll_list import EnrollAPIView

urlpatterns = [
    re_path(r'^list/?$', EnrollAPIView.list),
    re_path(r'^detail/?(?P<enroll_id>\d+)?$', EnrollAPIView.detail),
    re_path(r'^edit/?(?P<enroll_id>\d+)?$', EnrollAPIView.detail),
    re_path(r'^delete/?(?P<enroll_id>\d+)?$', EnrollAPIView.detail),
    re_path(r'^add/?$', EnrollAPIView.detail),
]
