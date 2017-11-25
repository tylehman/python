# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from jobs.models import JobInfo
from find_job.models import FindJob
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from filters import JobTitleFilter

class Find_a_job(ListView):
    model = JobInfo
    context_object_name = 'job'
    template_name = 'find_job/find_job.html'
    job_list = JobInfo.objects.all().order_by('-job_posted')
    paginate_by = 10
    job_filter = JobTitleFilter

    def get(self, request, *args, **kwargs):
        job_title_filter = self.job_filter(request.GET, queryset=self.job_list)
        return render(request, self.template_name, {'filter' : job_title_filter, 'paginator' : self.paginate_by})

class Detail_Job_Data(DetailView):
    model = JobInfo
    template_name = "find_job/each_job_info.html"
