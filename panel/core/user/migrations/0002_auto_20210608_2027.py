# Generated by Django 3.1 on 2021-06-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='default/avatar.png', null=True, upload_to='users/%Y/%m/%d'),
        ),
    ]
