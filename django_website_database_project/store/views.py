from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Customer, Vendor, User, Product, Service
from django.db import models

# I added this import to try to impliment forms. Might be useless
from django.http import HttpResponseRedirect
from .forms import ChoosePostTypeForm, ChooseProduct

# Create your views here.

def home(request):
    p_list = set()
    for product in Product.objects.all():
        p_type = product.product_type    
        p_list.add( (str(p_type), str(p_type)) ) 

    for service in Service.objects.all():
        p_type = service.service_type
        p_list.add( (str(p_type), str(p_type)) ) 

    if(len(p_list) > 0):
        p_list.add( ("", ""))
    
    action = request.POST
    form = ChooseProduct(action, p_list)

    context = {
        'posts': Post.objects.all(),
        'form': form,
    }
    return render(request, 'store/home.html', context)


# class PostListView(ListView):
#     model = Product
#     template_name = 'store/home.html'
#     context_object_name = 'products'
#     paginate_by = 10


class PostListView(ListView):
    model = Post
    template_name = 'store/home.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


# class UserPostListView(ListView):
#     model = Product
#     template_name = 'store/user_posts.html'
#     context_object_name = 'products'
#     paginate_by = 10

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Product.objects.filter(vendor_id = Vendor.objects.filter(user = user))


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


def PostCreateView(request):
    if request.method == 'POST':
        form = ChoosePostTypeForm(request.POST)
        action = request.POST
        if action.get('choice') == 'Product':
            return redirect('create_product')
        elif action.get('choice') == 'Service':
            return redirect('create_service')
    else:
        form = ChoosePostTypeForm()
        action = request.GET
    context = {
        'form': form
    }
    return render(request, 'store/create_choice.html', context)


class PostCreateProductView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'store/create_product.html'
    fields = ['product_type', 'product_name', 'price', 'details', 'bundle_id']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.vendor_id = Vendor.objects.get(name=f'{self.request.user.username}')
        return super().form_valid(form)


class PostCreateServiceView(LoginRequiredMixin, CreateView):
    model = Service
    template_name = 'store/create_service.html'
    fields = ['service_type', 'service_name', 'price', 'details', 'bundle_id']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.vendor_id = Vendor.objects.get(name=f'{self.request.user.username}')
        return super().form_valid(form)


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


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
    model = Post
    template_name = 'store/listings.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10
    
    cur_user = request.user.id
  
    context = {
        'title': 'Listings',
        'listings': Product.objects.filter(vendor_id = str(cur_user) ).union(Service.objects.filter(vendor_id = str(cur_user) ))
    }
    return render(request, 'store/listings.html', context)


def show_listings(request):
    if request.method == 'POST':
        data = request.POST.get('choice', None)
    else:
        data = "None"

    context = {
        'title': 'View Products or Services',
        'data': data,
        'products': Product.objects.filter(product_type = str(data))
    }

    return render(request, 'store/search_listings.html', context)


def show_bundles(request):
    if request.method == 'POST':
        data = request.POST.get('search', None)

    else:
        data = ""

    context = {
        "title": "View Bundles",
        "data": data
    }
    return render(request, 'store/search_listings.html', context)