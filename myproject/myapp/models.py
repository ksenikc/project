from django.db import models


class Stat(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Category(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Application(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True,
                                null=True)
    description = models.CharField(verbose_name='Описание', max_length=60)
    owner = models.ForeignKey('auth.User', verbose_name='Автор', related_name='orders_user',
                              on_delete=models.CASCADE,
                              null=True)
    categor = models.ForeignKey('Category', verbose_name='Категория', related_name='applic_cat',
                                on_delete=models.CASCADE,
                                null=True)
    stat = models.ForeignKey('Stat', verbose_name='Статус', related_name='applic_stat',
                                on_delete=models.CASCADE,
                                null=True,default='1')
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото ДО")
    image_after = models.ImageField(upload_to='photos', null=True, blank=True, verbose_name="Фото ПОСЛЕ")
    rejection_reason = models.TextField(null=True, blank=True, verbose_name="Причина отказа")
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['title']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
