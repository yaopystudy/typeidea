# -*- coding: utf-8 -*-

from django.contrib.admin import AdminSite

class  CustomSite(AdminSite):

    site_header = 'Type'
    site_title = 'Type管理后台'
    index_title = '首页'

custom_site= CustomSite(name= 'cus_admin')