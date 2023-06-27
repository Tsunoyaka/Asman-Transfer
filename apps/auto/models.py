from django.db import models


class Auto(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, primary_key=True)
    price = models.IntegerField(verbose_name='Цена', default=0)
    contract_price = models.BooleanField(verbose_name='Договорная цена', default=False)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    capacity = models.SmallIntegerField(verbose_name='Вместимость')
    photo = models.ImageField(verbose_name='Изображение', upload_to='auto_img')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def save(self, *args, **kwargs):
        if self.price == 0:
            self.contract_price = True
        else:
            self.contract_price = False
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Driver(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)
    experience = models.SmallIntegerField(verbose_name='Стаж')
    photo = models.ImageField(verbose_name='Фото', upload_to='driver_img')

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'