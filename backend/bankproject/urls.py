from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from bankapp import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'products', views.ProductListViewSet)
router.register(r'manage/add', views.ProductCreateViewSet)
router.register(r'manage', views.ProductDetailViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls'))
]
