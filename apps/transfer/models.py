from django.db import models


class Transfer(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)
    phone = models.CharField(verbose_name='Номер', max_length=13)
    date =  models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    route = models.CharField(verbose_name='Направление', max_length=255)
    auto = models.ForeignKey(verbose_name='Автомобиль', 
                             to='auto.Auto', 
                             on_delete=models.CASCADE, 
                             related_name='auto_rel')
    place_departure = models.CharField(verbose_name='Место выезда', 
                                       max_length=255, 
                                       blank=True, null=True)

    class Meta:
        verbose_name = 'Заказанный трансфер'
        verbose_name_plural = 'Заказанные трансферы'