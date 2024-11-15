from django.contrib import admin
from cars.models import Car, Brand

# ************************************************************
# * MODELO PARA MARCA(BRAND) - Admin
# ************************************************************
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



# ************************************************************
# * MODELO PARA CARROS (CAR)
# ************************************************************
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

admin.site.register(Brand, BrandAdmin) # registra o modelo
admin.site.register(Car, CarAdmin) # registra o modelo
