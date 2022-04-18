from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# I added this import to try to impliment forms. Might be useless
from django.http import HttpResponseRedirect
from .forms import *

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'store/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'store/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


class UserPostListView(ListView):
    model = Post
    template_name = 'store/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.authorr = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'store/about.html', context)


def wishlist(request):
    context = {
        'title': 'Wishlist'
    }
    return render(request, 'store/wishlist.html', context)


def listings(request):
    context = {
        'title': 'Listings'
    }
    return render(request, 'store/listings.html', context)


def show_listings(request):
    if request.method == 'POST':
        # f = SearchListings(request.POST)
        f = request.POST.get('search', None)
        # if f.is_valid():
        #     return HttpResponseRedirect('/thanks/')

    else:
        f = ""

    context = {
        "title": "View Products / Services",
        "data": f
    }
    return render(request, 'store/search_listings.html', context)

def show_bundles(request):
    if request.method == 'POST':
        f = request.POST.get('search', None)

    else:
        f = ""

    context = {
        "title": "View Bundles",
        "data": f
    }
    return render(request, 'store/search_listings.html', context)