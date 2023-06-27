from django.db import models


class Route(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    photo = models.ImageField(verbose_name='Изображение', upload_to='route_img')
    promotion = models.BooleanField(verbose_name='Акция', default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'