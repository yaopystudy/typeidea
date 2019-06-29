# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import  Post,Category,Tags
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass