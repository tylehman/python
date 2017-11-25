from jobs.models import JobInfo
from find_job.models import FindJob
import django_filters

class JobTitleFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(lookup_expr='icontains')
    comp_name = django_filters.CharFilter(lookup_expr='icontains')
    job_addr = django_filters.CharFilter(lookup_expr='icontains')
    job_link = django_filters.CharFilter(lookup_expr='icontains')
    job_posted = django_filters.DateFilter(name='job_posted')
    job_search = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = JobInfo
        fields = ['job_title', 'comp_name', 'job_addr', 'job_link', 'job_posted', 'job_search', ]
