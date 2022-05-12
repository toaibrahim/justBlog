from django.contrib import admin
from .models import BlogModel,Author,Category,Comment,PostView

# Register your models here.

admin.site.register(BlogModel)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostView)
