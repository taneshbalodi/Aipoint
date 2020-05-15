from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from .models import posts
from marketing.models import ignups
# Create your views here.


def home(request):
    featured = posts.objects.filter(featured=True)
    latest = posts.objects.order_by('-timestamp')[0:6]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = ignups()
        new_signup.email = email
        new_signup.save()
    context = {
    'object_list':featured,
    'latest': latest
    }

    return render(request,'jobs/home.html', context)



def about(request):
    return render(request, 'jobs/about.html', {})

def ourservice(request):
    return render(request, 'jobs/ourservice.html', {})


def privacy(request):
    return render(request, 'jobs/privacy.html', {})
