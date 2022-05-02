from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostCreateProductView,PostCreateServiceView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    # path('', PostListView.as_view(), name='store-home'),
    path('', views.home, name='store-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView, name='post-create'),
    #path('post/new/create_choice/', views.PostCreateView, name='create_choice'),
    path('post/new/create_product', PostCreateProductView.as_view(), name='create_product'),
    path('post/new/create_service', PostCreateServiceView.as_view(), name='create_service'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='store-about'),
    path('wishlist/', views.wishlist, name='store-wishlist'),
    path('listings/', views.listings, name='store-listings'),
    path('search/', views.show_listings, name='store-search'),
    path('search/bundles/', views.show_bundles, name='store-search-bundle'),

    # path('/search/bundle/<str:type>', views.show_bundles, name='store-bundlesservices'),

]
