# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from  .models import  Link,SiderBar
from  typeidea.custom_site import  custom_site


# Register your models here.


@admin.register(Link,site=custom_site)
class LinkAdmin(admin.ModelAdmin):
    list_display =[
                   'title','href','status','weight',
                  'owner','created_time']

@admin.register(SiderBar,site=custom_site)
class SiderBarAdmin(admin.ModelAdmin):

    list_display = ['title','display_type',
                    'content','owner','created_time']

