from drf_spectacular.contrib import django_filters
from drf_spectacular.contrib.django_filters import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, GenericAPIView
)
from rest_framework.pagination import PageNumberPagination

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer, ProductNameSerialazier


class UpdateNameAPIView(mixins.UpdateModelMixin, GenericAPIView):

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class MyPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPagination


class ProductListDetailView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class ProductNameUpdate(UpdateNameAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductNameSerialazier


class ProductUpdate(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductNameSerialazier
    http_method_names = ['patch']



