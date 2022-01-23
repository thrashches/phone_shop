from django.db import models
from slugify import slugify
from transliterate import translit
from django.urls import reverse


class Phone(models.Model):
    class Meta:
        verbose_name = 'телефон'
        verbose_name_plural = 'телефоны'

    # TODO: Добавьте требуемые поля
    # id, name, price, image, release_date, lte_exists и slug

    name = models.CharField(max_length=255, unique=True, verbose_name='название')
    price = models.IntegerField(verbose_name='цена')
    image = models.URLField(verbose_name='изображение')
    release_date = models.DateField(verbose_name='дата релиза')
    lte_exists = models.BooleanField(verbose_name='LTE')
    slug = models.SlugField(max_length=255, null=True, blank=True, verbose_name='SLUG')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phone', args=[self.slug])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = slugify(translit(self.name, 'ru', reversed=True), separator='_')
        return super().save()
