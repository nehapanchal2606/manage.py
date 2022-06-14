from django.contrib import admin
from django.shortcuts import render

from .models import user, blog


# Register your models here.


admin.site.register(user)
admin.site.register(blog)
