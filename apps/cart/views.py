from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Basket, BasketItem
from .serializers import BasketSerializer, BasketItemSerializer
from ..product_category.models import Product
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse


@extend_schema_view(
    list=extend_schema(
        summary="Получить список товаров в корзине",
        description="Возвращает список всех товаров в корзине текущего пользователя",
        responses={200: BasketSerializer},
    ),
    create=extend_schema(
        summary="Добавить товар в корзину",
        description="Добавляет товар в корзину текущего пользователя по его id",
        request=BasketItemSerializer,
        responses={
            201: OpenApiResponse(description="Товар успешно добавлен в корзину"),
            404: OpenApiResponse(description="Товар не найден"),
            400: OpenApiResponse(description="Некорректные данные или превышение доступного количества"),
        },
    ),
    destroy=extend_schema(
        summary="Удалить товар из корзины",
        description="Удаляет товар из корзины по его id",
        responses={
            204: OpenApiResponse(description="Товар успешно удалён из корзины"),
            404: OpenApiResponse(description="Товар не найден в корзине"),
        },
    ),
)
@extend_schema(tags=['Basket'])
class BasketViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        cart, _ = Basket.objects.get_or_create(user=request.user)
        serializer = BasketSerializer(cart)
        return Response(serializer.data)

    def create(self, request):
        cart, _ = Basket.objects.get_or_create(user=request.user)
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity"))

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Товар не найден"}, status=status.HTTP_404_NOT_FOUND)

        if quantity > product.stock:
            return Response({"error": "Количество товаров превышает доступное количество"}, status=status.HTTP_400_BAD_REQUEST)

        cart_item, created = BasketItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()

        return Response({"message": "Товар добавлен в корзину"}, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        try:
            cart = Basket.objects.get(user=request.user)
            item = BasketItem.objects.get(cart=cart, id=pk)
            item.delete()
            return Response({"message": "Товар удалён из корзины"}, status=status.HTTP_204_NO_CONTENT)
        except BasketItem.DoesNotExist:
            return Response({"error": "Товар не найден в корзине"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=["post"])
    @extend_schema(
        summary="Уменьшить количество товара в корзине",
        description="Уменьшает количество указанного товара в корзине пользователя. Если количество становится 0, товар удаляется",
        request=BasketItemSerializer,
        responses={
            200: OpenApiResponse(description="Количество товара уменьшено"),
            204: OpenApiResponse(description="Товар удалён из корзины"),
            404: OpenApiResponse(description="Товар не найден в корзине"),
        },
    )
    def reduce_quantity(self, request, pk=None):
        try:
            cart = Basket.objects.get(user=request.user)
            item = BasketItem.objects.get(cart=cart, id=pk)

            decrease_by = int(request.data.get('quantity', 1))
            item.quantity -= decrease_by

            if item.quantity <= 0:
                item.delete()
                return Response({'message': 'Товар удалён из корзины'})
            
            item.save()
            return Response({'message': 'Количество товара уменьшено', 'quantity': item.quantity})
        except BasketItem.DoesNotExist:
            return Response({'error': 'Товар не найден в корзине'}, status=status.HTTP_404_NOT_FOUND)
