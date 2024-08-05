from rest_framework import generics
from .models import Products, Manufactures
from .serializers import ProductSerializer, ManufacturesSerializer


class ProductListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):

        name = self.request.query_params.get('name', None)
        queryset = Products.objects.all()
        if name is not None:
            queryset = Products.objects.filter(name__icontains=name)
        if not queryset:
            queryset = Products.objects.all()
        return queryset


class ProductSortView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Products.objects.all()
        sort_by =self.request.query_params.get('sorted', None)
        type_sort_by = self.request.query_params.get('type_sorred', None)
        if type_sort_by == 'DESC':
            queryset = queryset.order_by(f'-{sort_by}')
        elif sort_by:
            queryset = queryset.order_by(sort_by)
        return queryset


class ManufacturesView(generics.ListAPIView):
    serializer_class = ManufacturesSerializer

    def get_queryset(self):
        queryset = Manufactures.objects.all()
        return queryset

