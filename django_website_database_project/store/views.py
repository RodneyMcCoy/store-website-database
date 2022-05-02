from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Customer, Vendor, User, Product, Service

# I added this import to try to impliment forms. Might be useless
from django.http import HttpResponseRedirect
from .forms import ChoosePostTypeForm


# Create your views here.

def home(request):
    p_models = Product.objects.all()
    p_list = {}

    for product in p_models:
        p_type = product.product_type    
        p_list.add( p_type )     

    context = {
        'posts': Post.objects.all(),
        'form': ChooseProduct(),
        'products': p_list
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
        'title': 'View Products / Services',
        'data': f,
        'products': Product.objects.filter(product_type = str(f))
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