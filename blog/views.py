from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import blog
from jobs.models import posts
from django.db.models import Count, Q

# Create your views here


def search(request):
    queryset = posts.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
        Q(title__icontains=query) |
        Q(overview__icontains=query)
        ).distinct()

    context = {
    'queryset': queryset
    }

    return render(request, 'blog/search_results.html', context)



def get_category_count():
    queryset = posts.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset


def allblogs(request):
    category_count = get_category_count()
    most_recent = posts.objects.order_by('-timestamp')[:6]
    post_list = posts.objects.all()
    paginator = Paginator(post_list , 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)

    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)

    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
    'queryset' : paginated_queryset,
    'most_recent' : most_recent ,
    'page_request_var' : page_request_var,
    'category_count': category_count
    }

    return render(request,'blog/allblogs.html',  context)

def detail(request, id):
    category_count = get_category_count()
    most_recent = posts.objects.order_by('-timestamp')[:6]
    detail = get_object_or_404(posts , id=id)
    forms = CommentForm(request.POST or None)
    if request.method == "POST":
        if forms.is_valid():
            forms.user = request.user
            forms.post = detail

            forms.save()
            return redirect(reverse("post-detail", kwargs = {
                'id' : detail.pk
            }))



    context = {
    'detail':detail,
    'forms':forms,
    'most_recent' : most_recent ,
    'category_count': category_count

    }
    return render(request,'blog/detail.html', context)

def about(request):
    return render(request,'blog/about.html')
