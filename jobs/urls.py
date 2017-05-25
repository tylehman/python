from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from jobs.models import JobInfo

urlpatterns = [
                url(r'^$', ListView.as_view(
                    queryset=JobInfo.objects.all().order_by('-id')[:25],
                    template_name = "jobs/jobs.html")
                    ),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(
                    model = JobInfo,
                    template_name = "jobs/jobinfo.html")
                    ),
            ]
