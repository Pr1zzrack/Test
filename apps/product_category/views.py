from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .filters import ProductFilter, ConnectionFilters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter


@extend_schema_view(
    list=extend_schema(
        summary="Retrieve a list of categories",
        description="Get a list of all available product categories.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a single category",
        description="Get details of a specific category by its ID.",
    ),
    create=extend_schema(
        summary="Create a new category",
        description="Add a new category to the database.",
    ),
    update=extend_schema(
        summary="Update an existing category",
        description="Update the details of an existing category by its ID.",
    ),
    destroy=extend_schema(
        summary="Delete a category",
        description="Remove a category from the database.",
    ),
)
@extend_schema(tags=["Category"])
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


@extend_schema_view(
    list=extend_schema(
        summary="Retrieve a list of products",
        description="Get a paginated list of products with optional filtering by category or price.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a single product",
        description="Get details of a specific product by its ID.",
    ),
    create=extend_schema(
        summary="Create a new product",
        description="Add a new product to the database.",
    ),
    update=extend_schema(
        summary="Update an existing product",
        description="Update the details of an existing product by its ID.",
    ),
    destroy=extend_schema(
        summary="Delete a product",
        description="Remove a product from the database.",
    ),
)
@extend_schema(tags=["Product"])
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    search_fields = ["name", "description"]
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ["price", "name", "created_at"]

    @action(detail=False, methods=["get"], url_path="filters")
    def available_filters(self, request):
        active_filters = ConnectionFilters.objects.filter(
            active_status="on"
        ).values_list("filter_value", flat=True)
        return Response({"active_filters": list(active_filters)})
