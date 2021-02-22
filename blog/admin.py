from django.contrib import admin
from .models import Post, Comment, Admin_Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Admin_Comment)
# Register your models here.
