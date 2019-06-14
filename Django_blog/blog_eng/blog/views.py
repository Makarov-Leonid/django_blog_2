from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import View

from .models import Post, Tag
from .utils import *
from .forms import TagForms as TagForm
from .forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'blog/index.html', context = {'page_obj':page})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', context={'tags':tags})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = "blog/post_detail.html"

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = "blog/tag_detail.html"

class TagCreate(LoginRequiredMixin, ObjCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True

class PostCreate(LoginRequiredMixin, ObjCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True

class TagUpdate(LoginRequiredMixin, ObjUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True

class PostUpdate(LoginRequiredMixin, ObjUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True

class TagDelete(LoginRequiredMixin, ObjDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tag_list_url'
    raise_exception = True

class PostDelete(LoginRequiredMixin, ObjDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True
