# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from  django.contrib.auth.models import User
from  django.db import  connection

from django.test import TestCase
from  .models import  Category

# Create your tests here.


class TestCategory(TestCase):

    def setUp(self):
        user= User.objects.create_user('chuan','1222@qq.com','12345')
        for i in range(10):
            category_name= 'cate_%s'%i
            Category.objects.create(name= category_name,owner=user)

    def  test_file(self):
        categories= Category.objects.all()

        print(categories.query)
        categories= categories.filter(status=1)
        print(categories.query)
        print('-------------------------')

        print(connection.queries)
        print('-------------------------')
        print(len(categories))


