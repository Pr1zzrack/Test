from rest_framework import viewsets
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUpEyeTest
from .serializers import SignUpEyeTestSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import AllowAny


@extend_schema_view(
    list=extend_schema(
        summary="Получение списка записей",
        description="Возвращает список всех записей",
        responses={200: SignUpEyeTestSerializer(many=True)}
    ),
    retrieve=extend_schema(
        summary="Получение одной записи",
        description="Возвращает конкретную запись по её id",
        responses={200: SignUpEyeTestSerializer}
    ),
    create=extend_schema(
        summary="Создание новой записи",
        description="Создаёт новую запись с предоставленными данными. После создания отправляется email.",
        request=SignUpEyeTestSerializer,
        responses={201: SignUpEyeTestSerializer},
    ),
    update=extend_schema(
        summary="Обновление существующей записи",
        description="Обновляет существующую запись с предоставленными данными",
        request=SignUpEyeTestSerializer,
        responses={200: SignUpEyeTestSerializer}
    ),
    partial_update=extend_schema(
        summary="Частичное обновление записи",
        description="Обновляет определённые поля записи",
        request=SignUpEyeTestSerializer,
        responses={200: SignUpEyeTestSerializer}
    ),
    destroy=extend_schema(
        summary="Удаление записи",
        description="Удаляет конкретную запись по её id",
        responses={204: "Запись успешно удалена"}
    )
)
@extend_schema(tags=['Eye-Test-Signup'])
class SignUpEyeTestViewSet(viewsets.ModelViewSet):
    queryset = SignUpEyeTest.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SignUpEyeTestSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        new_record_id = response.data.get('id')

        send_mail(
            'Новая запись на тестирование',
            f'Запись №{new_record_id}:\n   Имя: {request.data.get("first_name", "Не указано")}\n   Номер телефона: {request.data.get("phone_number", "Не указан")}\n   Электронная почта: {request.data.get("email", "Не указано")}\n   Комментарий: {request.data.get("comment", "Не указан")}',
            settings.DEFAULT_FROM_EMAIL,
            ['aktanarynov566@gmail.com'],
            fail_silently=False,
        )

        return response
