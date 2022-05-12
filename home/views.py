

from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import BlogModel,Author,PostView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from marketing.models import Signup
from django.db.models import Count,Q
from django.contrib.auth.models import User
from .forms import CommentForm,PostForm,ContactForm
from django.contrib.auth import get_user
from django.contrib import messages






def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None



def get_category_count():
    queryset = BlogModel.objects.values('category__title').annotate(Count('category__title'))
    return queryset

# Create your views here.
def home(request):
    category_count = get_category_count()
    
    article = BlogModel.objects.all().order_by('-created_at')
    paginator = Paginator(article,4)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    try:
        paginated_queryset = paginator.page(page_num)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    aside = BlogModel.objects.all().order_by('-created_at')[0:2]


    if request.method == "POST":
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        messages.success(request,"Thaks for subscribing to our newletter!")


    return render(request,"main/home.html",{
        'article':article,
        'aside':aside,
        'page':page,
        'post_list':paginated_queryset,
        'category_count':category_count
    })

def blog_details(request,slug):
    article = BlogModel.objects.get(slug = slug)

    PostView.objects.get_or_create(user=get_user(request),post=article)

    aside = BlogModel.objects.all().order_by('-created_at')[0:1]
    latest = BlogModel.objects.all().order_by('-created_at')[0:5]

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = article
            form.save()
            messages.success(request,"Comment submitted successfully!")
            def get_absolute_url(article):
                return reverse('blog_details', kwargs={
                    'pk': article.pk
                })
    return render(request,"main/blog.html",{
        'article':article,
        'aside':aside,
        'latest':latest,
        'form':form
    })

def search(request):
    queryset = BlogModel.objects.all()
    query = request.GET.get('search')
    if query:
        queryset = queryset.filter(
            Q(title__icontains = query)|Q(content__icontains = query)
        ).distinct()

    aside = BlogModel.objects.all().order_by('-created_at')[0:2]
    category_count =get_category_count()
    return render(request,"main/search-result-page.html",{
        'queryset':queryset,
        'aside':aside,
        'category_count':category_count
    })

def about(request):
    about_aside = BlogModel.objects.all().order_by('-created_at')[0:5]
    return render(request,'main/about.html',{
        'about_aside':about_aside
    })


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your form have been submitted successfully, Thank you for your response")
            return redirect("/contact")
    else:
        form = ContactForm()
    return render(request,'main/contact.html',{
        'form':form
    })



def add_post(request):
    title = 'Create'

    form = PostForm(request.POST or None, request.FILES or None)
    author = get_user(request)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect("/")
    context = {
        'title': title,
        'form': form
    }
    return render(request, "main/add_post.html", context)


def post_update(request,slug):
    title = 'Update'
    post = get_object_or_404(BlogModel, slug=slug)
    form = PostForm(
        request.POST or None,
        request.FILES or None,
        instance=post)
    author = get_user(request)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect("/")
    context = {
        'title': title,
        'form': form
    }
    return render(request, "main/add_post.html", context)


def post_delete(request,slug):
    post = get_object_or_404(BlogModel,slug = slug)
    post.delete()
    return redirect("/")

#NOT NULL constraint failed: home_blogmodel.author_id
#Cannot assign "<Author: toaibrahim>": "BlogModel.author" must be a "User" instance.



