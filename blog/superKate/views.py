
from django.shortcuts import render
from django.http import HttpResponse
from .models import Page, Review, Post, Posts
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


def hello(request):
    return HttpResponse("Hello")

def page_view(request):
    context = {}
    context["all_pages"] = Page.objects.all()
    return render(request, "all_pages_func.html", context)

def review_view(request):
    context = {}
    context["all_reviews"] = Review.objects.all()
    return render(request, "all_preview_func.html", context)

#$$$$$$$$$$$$$$****************$$$$$$$$$$$$$$$$$$$$$$$$$$$

class PageListView(ListView):
    model = Page
    template_name = "all_pages_class.html"


class PostListView(ListView):
    model = Post
    template_name = "all_post_class.html"


class PostsListView(ListView):
    model = Posts
    template_name = "all_posts_class.html"


class ReviewListView(ListView):
    model = Review
    template_name = "all_review_class.html"

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###################

class PageCreateView(CreateView):
    model = Page
    template_name = "create_page.html"
    fields = "__all__"
    success_url = "/superKate/all_pages_class/"

class PostCreateView(CreateView):
    model = Post
    template_name = "create_post.html"
    fields = "__all__"
    success_url = "/superKate/all_pages_class/"

class PostsCreateView(CreateView):
    model = Posts
    template_name = "create_posts.html"
    fields = "__all__"
    success_url = "/superKate/all_pages_class/"

class ReviewCreateView(CreateView):
    model = Review
    template_name = "create_review.html"
    fields = "__all__"
    success_url = "/superKate/all_review_class/"

#$$$$$$$$$$$$$$((((((((((((((((((((&&&&&&&&&&&&&&&&&&&&&&&&&&&


class PageDetailView(DetailView):
    model = Page
    template_name = "detail_page_class.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "detail_post_class.html"

class PostsDetailView(DetailView):
    model = Posts
    template_name = "detail_posts_class.html"

class ReviewDetailView(DetailView):
    model = Review
    template_name = "detail_review_class.html"

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class PageUpdateView(UpdateView):
    model = Page
    fields = ("title", "description")
    template_name = "update_page.html"
    success_url = "/superKate/all_pages_class/"

class PostUpdateView(UpdateView):
    model = Post
    fields = ("title", "description")
    template_name = "update_post.html"
    success_url = "/superKate/all_pages_class/"

class PostsUpdateView(UpdateView):
    model = Posts
    fields = ("title", "description")
    template_name = "update_posts.html"
    success_url = "/superKate/all_pages_class/"

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ("name", "description")
    template_name = "update_review.html"
    success_url = "/superKate/all_review_class/"

#!!!!!!!!!!!!!!****************!!!!!!!!!!!!!!!!!!!*************
class PageDeleteView(DeleteView):
    model = Page
    template_name = "delete_view.html"
    success_url = "/superKate/all_pages_class/"

class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_view.html"
    success_url = "/superKate/all_pages_class/"

class PostsDeleteView(DeleteView):
    model = Posts
    template_name = "delete_view.html"
    success_url = "/superKate/all_pages_class/"

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "delete_view.html"
    success_url = "/superKate/all_review_class/"





