from django.contrib import admin
from blog.models import Post,Comment #그냥 model은 error

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
