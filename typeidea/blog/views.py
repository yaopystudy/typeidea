# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import   Paginator,EmptyPage
from django.shortcuts import render
#listview是多个对象展示如列表展示，detailview是单个对象
from  django.views.generic import ListView,DetailView

from  .models import  Post,Tags,Category
from  config.models import  SiderBar
# from  django.db import  connection
# from  django.http import  Http404
from  comment.models import  Comment


# Create your views here.
class  CommonMinxin(object):
    #返回模板前渲染之前从get_context_data拿数据

    def get_context_data(self):

        categories = Category.objects.filter(status=1)  # TODO: fix magic number
        # 是否是导航，是导航展示在上面，不是显示在下面
        nav_cates = []
        cates = []
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)
        side_bars = SiderBar.objects.filter(status=1)
        # 最近评论
        recently_post = Post.objects.filter(status=1)[:10]
        # hot_post= Post.objects.filter(status=1).order_by('views')[:10]
        recently_comments = Comment.objects.filter(status=1)[:10]

        exta_context = {
            'nav_cates': nav_cates,
            'cates': cates,
            'side_bars': side_bars,
            'recently_post': recently_post,
            'recently_comments': recently_comments,
        }

        return super(CommonMinxin,self).get_context_data(**exta_context)







class BasePostView(CommonMinxin,ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = "posts"
    #展示分页
    paginate_by = 3

class  IndexView(BasePostView):

        pass
#渲染基础数据
class  CategoryView(BasePostView):
    def  get_queryset(self):
        qs =super(CategoryView,self).get_queryset()
        #通过self.kwargs接口，get获取url中category_id的参数，查出cate_id
        cate_id= self.kwargs.get("category_id")
        qs= qs.filter(category_id=cate_id)

        return  qs
class   TagView(BasePostView):
    def  get_queryset(self):
        tag_id= self.kwargs('tag_id')
        try:
            tag = Tags.objects.get(id=tag_id)
        except Tags.DoesNotExist:
            return  []

        posts= tag.posts.all()
        return  posts


class  PostView(CommonMinxin,DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = "post"

# #可以复用的函数
# def  get_common_context():
#     categories = Category.objects.filter(status=1)  # TODO: fix magic number
#     # 是否是导航，是导航展示在上面，不是显示在下面
#     nav_cates = []
#     cates = []
#     for cate in categories:
#         if cate.is_nav:
#             nav_cates.append(cate)
#         else:
#             cates.append(cate)
#     side_bars = SiderBar.objects.filter(status=1)
#     # 最近评论
#     recently_post = Post.objects.filter(status=1)[:10]
#     # hot_post= Post.objects.filter(status=1).order_by('views')[:10]
#     recently_comments = Comment.objects.filter(status=1)[:10]
#
#     context = {
#         'nav_cates': nav_cates,
#         'cates': cates,
#         'side_bars': side_bars,
#         'recently_post': recently_post,
#         'recently_comments': recently_comments,
#     }
#
#     return  context




# def  post_list(request,category_id=None,tag_id=None):
#
#
#     #接受参数
#     page= request.GET.get('page',1)
#     page_size= 3
#     try:
#         page= int(page)
#
#     except TypeError:
#         page =1
#
#     queryset = Post.objects.all()
#     # # if category_id:
#     # #     #分类页面
#     # #     queryset= queryset.filter(category_id=category_id)
#     # elif tag_id:
#     #     #标签页面
#     #     #多对多获取方法
#     #     try:
#     #         tags= Tags.objects.get(id=tag_id)
#     #
#     #     except Tags.DoesNotExist:
#     #         queryset=[]
#     #
#     #     else:
#     #         queryset =tags.post_set.all()
#
#     paginator= Paginator(queryset,page_size)
#     try:
#         posts= paginator.page(page)
#     except EmptyPage:
#         posts= paginator.page(paginator.num_pages)
#
#
#     context= {
#         'posts':posts,
#     }
#     common_context= get_common_context()
#     context.update(common_context)
#
#
#     return  render(request,'blog/list.html',context=context)
#
#
#
# def  post_detail(request,pk=None):
#     try:
#         post= Post.objects.get(pk=pk)
#
#     except  Post.DoesnotExist:
#         raise Http404("Post is not exist")
#
#     categories = Category.objects.filter(status=1)  # TODO: fix magic number
#     # 是否是导航，是导航展示在上面，不是显示在下面
#     nav_cates = []
#     cates = []
#     for cate in categories:
#         if cate.is_nav:
#             nav_cates.append(cate)
#         else:
#             cates.append(cate)
#     side_bars = SiderBar.objects.filter(status=1)
#     # 最近评论
#     recently_post = Post.objects.filter(status=1)[:10]
#     # hot_post= Post.objects.filter(status=1).order_by('views')[:10]
#     recently_comments = Comment.objects.filter(status=1)[:10]
#
#     context = {
#         'posts': post,
#         'nav_cates': nav_cates,
#         'cates': cates,
#         'side_bars': side_bars,
#         'recently_post': recently_post,
#         'recently_comments': recently_comments,
#     }
#
#
#
#     return render(request,'blog/detail.html',context=context)