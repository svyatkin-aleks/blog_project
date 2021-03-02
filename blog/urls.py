from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('product/create', ProductCreateView.as_view()),
    path('product/delete/<str:pk>', ProductDeleteView.as_view()),
    path('product/update/<str:pk>', ProductUpdateView.as_view()),
    path('product/list', ProductListView.as_view()),
    path('product/list/detail', ProductListDetailView.as_view()),
    path('product/update/name/<str:pk>', ProductNameUpdate.as_view()),
    path('product/update/name/v2/<str:pk>', ProductUpdate.as_view())
]