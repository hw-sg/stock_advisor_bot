# Generated by Django 3.1.2 on 2021-09-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasa_chatbot', '0008_auto_20210914_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdatabase',
            name='telegram_id',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
