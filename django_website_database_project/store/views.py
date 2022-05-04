from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Customer, Vendor, User, Product, Service, Bundle, Wishlist
from django.db import models

# I added this import to try to impliment forms. Might be useless
from django.http import HttpResponseRedirect
from .forms import ChoosePostTypeForm, ChooseProduct

# Create your views here.

def home(request):
    p_list = set()
    for product in Product.objects.all():
        p_type = product.listing_type    
        p_list.add( (str(p_type), str(p_type)) ) 

    for service in Service.objects.all():
        p_type = service.listing_type
        p_list.add( (str(p_type), str(p_type)) ) 

    if(len(p_list) == 0):
        p_list.add( ("No Products Currently in Database", "No Products Currently in Database"))
    
    action = request.POST
    form = ChooseProduct(p_list)

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
    fields = ['listing_type', 'name', 'price', 'binding_contract', 'details']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.vendor_id = Vendor.objects.get(name=f'{self.request.user.username}')
        return super().form_valid(form)


class PostCreateServiceView(LoginRequiredMixin, CreateView):
    model = Service
    template_name = 'store/create_service.html'
    fields = ['listing_type', 'name', 'price', 'binding_contract',  'details']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.vendor_id = Vendor.objects.get(name=f'{self.request.user.username}')
        return super().form_valid(form)


class PostCreateBundleView(LoginRequiredMixin, CreateView):
    model = Bundle
    template_name = 'store/create_bundle.html'
    fields = ['price']
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

    cur_user = request.user.id

    context = {
        'title': 'Wishlist',
        'wishlist': Wishlist.objects.filter(customer_id=str(cur_user))
    }
    return render(request, 'store/wishlist.html', context)


def superuser(request):
    context = {

    }
    return render(request, 'store/superuser.html', context)


def listings(request):
    model = Post
    template_name = 'store/listings.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10
    
    cur_user = request.user.id
  
    context = {
        'title': 'Listings',
        'listings': Product.objects.filter(vendor_id = str(cur_user) ).union(Service.objects.filter(vendor_id = str(cur_user) )),
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
        'listings': Product.objects.filter(listing_type = str(data)).union(Service.objects.filter(listing_type = str(data))),
        'is_customer': request.user.is_customer
    }

    return render(request, 'store/search_listings.html', context)


def add_to_wishlist(request):
    user = request.user

    if request.method == 'POST':
        data = request.POST.get('choice', None)
    else:
        data = "None"

    add_this = request.POST

    data = "yee"

    context = {
        'title': 'View Products or Services',
        'data': data,
        'listings': Product.objects.filter(listing_type = str(data)).union(Service.objects.filter(listing_type = str(data))),
        'is_customer': request.user.is_customer,
        'add_this': add_this
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