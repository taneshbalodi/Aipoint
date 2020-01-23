from django.shortcuts import render
from .models import jobs
# Create your views here.
def home(request):
    job = jobs.objects
    return render(request,'jobs/home.html', {'job': job})
