from django.urls import path

from . import views

urlpatterns = [
  path('search', views.ProductSearchListView.as_view(), name='search'),
]