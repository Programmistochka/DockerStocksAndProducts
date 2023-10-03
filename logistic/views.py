from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # параметры фильтрации 
    # для реализации выборки по названию и описанию
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', ]
    search_fields = ['title', 'description']
    pagination_class = LimitOffsetPagination

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    # для реализации поиска склала с определенным продуктом
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products']
    pagination_class = LimitOffsetPagination
    