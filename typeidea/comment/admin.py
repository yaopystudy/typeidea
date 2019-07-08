# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import  Comment

from  typeidea.custom_site import  custom_site
from  .adminforms import CommentAdminForms
# Register your models here.


@admin.register(Comment,site=custom_site)
class CommentAdmin(admin.ModelAdmin):
     form = CommentAdminForms


     list_display = ['post','content',
                     'nickname','website' ,
                     'email','created_time']

     list_filter = ['post']
     search_fields = ['post','content',
                     'nickname']
     show_full_result_count = False
     date_hierarchy = 'created_time'  #时间检索
     # save_on_top = True
     # actions_on_bottom = False
     # actions_on_top = True

