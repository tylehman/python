from jobs.models import JobInfo
import django_filters

class JobTitleFilter(django_filters.FilterSet):
    class Meta:
        model = FindJob
        fields = ['job_title',]



