from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render
from django.views.generic.base import View, TemplateView
from rest_framework import viewsets, permissions, mixins

from bankapp.models import Product
from bankapp.serializers import UserSerializer, GroupSerializer, ProductSerializer


class ProductCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows products to be created.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductDetailViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for viewing and editing products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'


class ProductListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class FrontEndRenderView(TemplateView):
    template_name = 'bankapp/index.html'


