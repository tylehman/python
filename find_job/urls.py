from django.conf.urls import url
from django.views.generic import ListView, DetailView
from jobs.models import JobInfo
from find_job.models import FindJob
from views import Detail_Job_Data, Find_a_job
from . import views

urlpatterns = [
                url(r'^$', Find_a_job.as_view(model='JobInfo', paginate_by=10), name='Find_a_job'),
                url(r'^(?P<pk>\d+)$', Detail_Job_Data.as_view()
                    ),
            ]
