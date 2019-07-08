# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from  blog.models  import  Post
from  django import  forms

class Comment(models.Model):
    STATUS_ITEMS= (
        (1,'正常'),
        (2,'删除'),
    )
    post= models.ForeignKey(Post,verbose_name= "文章")
    content= models.CharField(max_length=2000,verbose_name="内容")
    nickname= models.CharField(max_length=50,verbose_name="昵称")
    website= models.URLField(verbose_name="网站")  #django自己URL的验证
    email= models.EmailField(verbose_name="邮箱")
    status= models.PositiveIntegerField(default=1,choices=STATUS_ITEMS,verbose_name='状态')
    created_time= models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def  __str__(self):
        return  self.content
    def  __unicode__(self):
        return  self.content


    #配置model
    class Meta:
        verbose_name= verbose_name_plural= "评论"
        #也可在此配置组合索引、联合索引、排序







