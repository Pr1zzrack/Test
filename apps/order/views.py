from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Order
from .serializers import OrderSerializer
from django.core.mail import send_mail
from django.conf import settings
from ..cart.models import BasketItem, Basket


@extend_schema(tags=['Orders'])
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        try:
            cart = Basket.objects.get(user=request.user)
            product_id = request.data.get('product')
            item = BasketItem.objects.get(cart=cart, product__id=product_id)
        except BasketItem.DoesNotExist:
            return Response({'error': 'Товар не найден в вашей корзине'}, status=status.HTTP_404_NOT_FOUND)
        
        quantity = int(request.data.get('quantity'))
        if quantity > item.quantity:
            return Response({'error': 'В вашей корзине нет такого количества товара'}, status=status.HTTP_400_BAD_REQUEST)

        name = request.data.get('name')
        phone = request.data.get('phone')
        address_and_comment = request.data.get('address_and_comment')
        delivery_method = request.data.get('delivery_method')
        payment_method = request.data.get('payment_method')

        if not all([name, phone, address_and_comment, delivery_method, payment_method, product_id]):
            return Response({'error': 'Отсутствуют обязательные поля'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        order_id = response.data.get('id')
        order_created_at = response.data.get('created_at')

        try:
            send_mail(
                'Новая запись на тестирование',
                f'Запись №{order_id}:\n   Имя: {name}\n   Номер телефона: {phone}\n   Адрес и комментарии: {address_and_comment}\n   Способ доставки: {delivery_method}\n   Способ оплаты: {payment_method}\n   Количество: {quantity}\n   Дата заказа: {order_created_at}',
                settings.DEFAULT_FROM_EMAIL,
                ['aktanarynov566@gmail.com'],
                fail_silently=False,
            )
        except Exception as e:
            return Response({'error': f'Ошибка при отправке почты: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        decrease_by = int(quantity)
        if decrease_by <= 0:
            return Response({'error': 'Количество товара должно быть больше нуля'}, status=status.HTTP_400_BAD_REQUEST)

        item.quantity -= decrease_by
        item.save()

        return Response({'message': 'Заказ оформлен', 'Название товара': item.product.name, 'Количество': quantity})
