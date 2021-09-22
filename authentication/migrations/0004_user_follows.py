# Generated by Django 3.2.7 on 2021-09-22 12:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210922_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(limit_choices_to={'role': 'CREATOR'}, to=settings.AUTH_USER_MODEL),
        ),
    ]
