from django.contrib import admin

from retail.models import Network, Trader, Product


@admin.action(description='Удaлить задолженность перед поставщиком')
def debt_clear(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Trader)
class TraderAdmin(admin.ModelAdmin):
    list_display = ['city', 'title', 'trader_type', 'debt', 'supplier_url']
    ordering = ('title', 'created_at')
    list_filter = ('city',)
    actions = ['debt_clear']

    def supplier_url(self, obj):
        if obj.supplier:
            return obj.supplier.get_absolute_url()

    supplier_url.short_description = 'Ссылка на поставщика'

    @admin.action(description='Удaлить задолженность перед поставщиком')
    def debt_clear(self, request, queryset):
        queryset.update(debt=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'mod', 'released_at')
    ordering = ('title', 'mod')
