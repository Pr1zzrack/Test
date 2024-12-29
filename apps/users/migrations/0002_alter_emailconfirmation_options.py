from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailconfirmation',
            options={'verbose_name': 'Код активации Аккаунта', 'verbose_name_plural': 'Коды активации Аккаунта'},
        ),
    ]
