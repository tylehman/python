from django.conf.urls import url
from django.views.generic import ListView, DetailView
from jobs.models import JobInfo
from jobs.views import JobsTemplate, EachJobTemplate

urlpatterns = [
                url(r'^$', JobsTemplate.as_view(),
                    ),
                url(r'^(?P<pk>\d+)$', EachJobTemplate.as_view()
                    ),
            ]
