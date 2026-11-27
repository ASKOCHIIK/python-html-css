from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    # media/categories/
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Lalafo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя Товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
                                #12000,9913
    new_old = models.BooleanField(default=True, verbose_name='Новый / Б/У')
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='lalafo', null=True, blank=True)

    class Meta:
        verbose_name = 'ЛАЛАФО'
        verbose_name_plural = 'ЛАЛАФОЛОР'

    def __str__(self):
        return self.name



