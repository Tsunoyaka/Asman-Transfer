# Generated by Django 4.2.2 on 2023-06-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Название')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('contract_price', models.BooleanField(default=False, verbose_name='Договорная цена')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('capacity', models.SmallIntegerField(verbose_name='Вместимость')),
                ('photo', models.ImageField(upload_to='auto_img', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('experience', models.SmallIntegerField(verbose_name='Стаж')),
                ('photo', models.ImageField(upload_to='driver_img', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Водитель',
                'verbose_name_plural': 'Водители',
            },
        ),
    ]
