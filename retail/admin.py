from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from retail.models import Network, Trader, Product


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """Отображение торговой сети в панели администратора"""
    list_display = ('title', 'factory', 'provider', 'trader')


@admin.register(Trader)
class TraderAdmin(admin.ModelAdmin):
    """Отображение звена торговой сети в панели администратора"""
    list_display = ['city', 'title', 'trader_type', 'debt', 'supplier_url']
    list_display_links = ('title',)
    ordering = ('title', 'created_at')
    list_filter = ('city',)
    actions = ['debt_clear']

    def supplier_url(self, obj):
        if obj.supplier:
            url = reverse('admin:retail_trader_change', args=[obj.supplier.id])
            link = '<a href="{}">посмотреть карточку поставщика</a>'.format(url)
            return mark_safe(link)
        return 'Поставщик не указан'
    supplier_url.short_description = 'Ссылка на поставщика'

    @admin.action(description='Удaлить задолженность перед поставщиком')
    def debt_clear(self, request, queryset):
        queryset.update(debt=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение продукта в панели администратора"""
    list_display = ('title', 'mod', 'released_at')
    ordering = ('title', 'mod')
