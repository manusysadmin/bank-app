from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from bankapp import views
from bankapp.views import TokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', TokenView.as_view()),
    path('api/register', views.UserCreateView.as_view()),
    path('api/refresh_jwt_token', TokenRefreshView.as_view()),
    path('api/manage/products/<slug:slug>', views.ProductDetailView.as_view()),
    path('api/manage/products/add', views.ProductCreateView.as_view()),
    path('api/manage/products', views.ProductListView.as_view()),
    path('api/manage/users/<pk>', views.UserEditView.as_view()),
    path('api/manage/users', views.UserListView.as_view()),
    path('api/products/search', views.ProductListView.as_view()),
]
