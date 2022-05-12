import imp
from django.urls import path,include
from . import views
#from .views import HomeView,BlogView

app_name = "main"
urlpatterns = [
    path("",views.home,name='home'),
    path("blog/<str:slug>",views.blog_details,name='blog_details'),
    path("post_update/<str:slug>",views.post_update,name='post_update'),
    path("post_delete/<str:slug>",views.post_delete,name='post_delete'),
    path('add_post/',views.add_post,name='add_post'),

    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    
    path('search/',views.search,name='search'),
    path('tinymce/',include('tinymce.urls')),
]