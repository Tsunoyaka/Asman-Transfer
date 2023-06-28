from django.db import models
from django.core.exceptions import ValidationError


class Recall(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=55)
    description = models.CharField(verbose_name='Отзыв', max_length=2048, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(verbose_name='Оценка')
    photo = models.ImageField(verbose_name='Фото', upload_to='recall_img', default='/asman_transfer.png')
    created_at = models.DateField(verbose_name='Дата создания', auto_now=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Documentation(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255,blank=True, null=True)
    photo = models.ImageField(verbose_name='Изображение', upload_to='documentation_img')

    class Meta:
        verbose_name = 'Документацию'
        verbose_name_plural = 'Документации'


def count_video(self):
    video_count = Video.objects.count()
    if video_count == 1:
        raise ValidationError('Что бы добавить новое видео, удалите старое. Видео может быть только одно!')

class Video(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, blank=True, null=True)
    video = models.FileField(verbose_name='Видео', upload_to='videos' , validators=[count_video])

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class DefaultUserImage(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, blank=True, null=True)
    image = models.ImageField(verbose_name='Изображение')