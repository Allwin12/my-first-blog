from django.contrib import admin
from .models import Post

admin.site.register(Post)

list_display = ('author', 'title','text')
# Register your models here.
