from django.urls import path
from .views import ProductListView, ProductDetailView, ProductSearchView, ProductSortView, ManufacturesView

urlpatterns = [
    path('', ProductListView.as_view(), name='products-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('search/', ProductSearchView.as_view(), name='product-search'),
    path('sorted/', ProductSortView.as_view(), name='product-sorted'),
    path('manufactures/', ManufacturesView.as_view(), name='manufactures-list'),
]
