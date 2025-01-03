# Generated by Django 4.2.5 on 2024-12-09 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product_category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("phone", models.CharField(max_length=20)),
                ("address_and_comment", models.TextField()),
                (
                    "delivery_method",
                    models.CharField(
                        choices=[
                            ("яндекс такси", "Яндекс Такси"),
                            ("самовывоз", "Самовывоз"),
                        ],
                        max_length=13,
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("банковская карта", "Банковская карта"),
                            ("наличные", "Наличные"),
                        ],
                        max_length=16,
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product_category.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
            },
        ),
    ]
