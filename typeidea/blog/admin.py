# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from  .adminforms import  PostAdminForm
from django.contrib import admin
from .models import  Post,Category,Tags
from  django.urls import  reverse
from  django.utils.html import  format_html
from  typeidea.custom_site import  custom_site


# Register your models here.


@admin.register(Post,site=custom_site)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    list_display = [
        'title','category','status_show','owner',
        'create_time','operator']
    list_display_links = []
    list_filter = ['category']
    search_fields = ['title','category__name','owner__username']
    show_full_result_count = False
    save_on_top = True
    actions_on_bottom = False
    actions_on_top = True


    #编辑页面
    save_on_top = True
    date_hierarchy = 'create_time'
    fieldsets=  (
            ('基础配置',{'fields':(('category','title'),
                               'desc','status','content')
        }
    ),
            ('高级配置',{
                'classes':('collapse','addon'),
                'fields':('tags',)
            })
    )
    filter_horizontal = ('tags',)

    def  operator(self,obj):
        return  format_html(
            '<a  href="{}">编辑</a>',
             reverse('cus_admin:blog_post_change',args=(obj.id,)))
    operator.allow_tags=True

    operator.short_description = '操作'

    def  save_model(self, request, obj, form, change):
        print(self,request, obj, form, change)
        obj.owner= request.user
        super(PostAdmin,self).save_model(request, obj, form, change)



class PostInlineAdmin(admin.StackedInline):
    fields = ('title','status','owner')
    extra = 1
    min_num = 3
    model = Post





@admin.register(Category,site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostInlineAdmin
    ]

@admin.register(Tags,site=custom_site)
class TagsAdmin(admin.ModelAdmin):
    pass