# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from  django.contrib.auth.models import User
from  django.db import  connection
from django.test import TestCase
from  django.test.utils import  override_settings
from  .models import  Category,Post
from  pprint import  pprint as pp
# Create your tests here.


class TestCategory(TestCase):
    @override_settings(DEBUG=True)
    def setUp(self):
        self.user= user= User.objects.create_user('chuan','1222@qq.com','12345')
        # for i in range(10):
        #     category_name= 'cate_%s'% i
        #     # import pdb;pdb.set_trace()
        #     Category.objects.create(name= category_name,owner=user)

        Category.objects.bulk_create([
            Category(name='cate_bulk_%s' %  i,owner=user)
            for i in range(10)
        ])

    @override_settings(DEBUG=True)
    def  test_file(self):
        categories = Category.objects.values('name')

        print(categories)

        categories= Category.objects.values_list('name')
        print(categories)

        categories = Category.objects.values_list('name',flat='True'
                                                  )
        pp(categories)


