# Generated by Django 4.2.5 on 2024-12-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eye_test_signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupeyetest',
            name='status',
            field=models.CharField(choices=[('pending', 'Запись не выполнена'), ('completed', 'Запись выполнена')], default='pending', max_length=10),
        ),
    ]