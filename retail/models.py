from django.db import models
from django.urls import reverse

from config.services import NULLABLE


class Network(models.Model):
    """Модель торговой сети"""
    title = models.CharField(max_length=255, verbose_name='Наименование')
    factory = models.ForeignKey('Trader', on_delete=models.SET_NULL, related_name='factory',
                                verbose_name='Производитель', **NULLABLE)
    provider = models.ForeignKey('Trader', on_delete=models.SET_NULL, related_name='provider', verbose_name='Поставщик',
                                 **NULLABLE)
    trader = models.ForeignKey('Trader', on_delete=models.SET_NULL, related_name='trade', verbose_name='Продавец',
                               **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Торговая сеть"
        verbose_name_plural = "Торговые сети"


class Product(models.Model):
    """Модель продукта"""

    title = models.CharField(max_length=200, verbose_name='Название')
    mod = models.CharField(max_length=50, verbose_name='модель')
    released_at = models.DateField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Trader(models.Model):
    """Модель звена торговой сети:
    Уровень объекта - выбор из иерархии: 0(производитель), 1(поставщик), 2(продавец).
    Тип объекта - выбор из вариантов: завод, розничная сеть или индивидуальный предприниматель.
    Контактные данные объекта - полный адрес и эл почта.
    Ссылка на поставщика - при наличии.
    Задолженность перед поставщиком - по умолчанию = 0.
    Дата добавления в систему - автоматически, текущая"""

    LEVEL_CHOICES = [
        ('0', 'производитель'), ('1', 'поставщик'), ('2', 'продавец')
    ]

    TYPE_CHOICES = [
        ('ЗАВОД', 'завод'), ('РОЗНИЦА', 'розничная сеть'), ('ИП', 'индивидуальный предприниматель')
    ]

    trader_level = models.CharField(choices=LEVEL_CHOICES, verbose_name='Уровень звена в иерархии торговой сети',
                                    default='0')
    trader_type = models.CharField(choices=TYPE_CHOICES, verbose_name='Тип звена торговой сети', default='ЗАВОД')

    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Почта', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house = models.CharField(max_length=50, verbose_name='Дом(номер, литера, помещение)')
    supplier = models.ForeignKey('Trader', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=20, decimal_places=2, default=0,
                               verbose_name='Задолженность перед поставщиком')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата добавления в систему')

    products = models.ManyToManyField(Product, verbose_name='Продукты')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"
