from django.urls import path
from .views import *
from . import views



urlpatterns = [
    # path('', PostListView.as_view(), name='store-home'),
    path('', views.home, name='store-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView, name='post-create'),
    #path('post/new/create_choice/', views.PostCreateView, name='create_choice'),
    path('create_product', PostCreateProductView.as_view(), name='create_product'),
    path('create_service', PostCreateServiceView.as_view(), name='create_service'),
    path('create_bundle', PostCreateBundleView.as_view(), name='create_bundle'),
    # path('add_to_bundle', PostAddToBundleView.as_view(), name='add_to_bundle'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='store-about'),
    path('wishlist/', views.wishlist, name='store-wishlist'),
    path('listings/', views.listings, name='store-listings'),
    path('bundles/', views.bundles, name='store-bundles'),
    path('search/', views.show_listings, name='store-search'),
    path('search/', views.add_to_wishlist, name='store-add-to-wishlist'),
    # path('search/bundles/', views.show_bundles, name='store-search-bundle'),
    path('superuser/', views.superuser, name='superuser'),

    # path('/search/bundle/<str:type>', views.show_bundles, name='store-bundlesservices'),

]
