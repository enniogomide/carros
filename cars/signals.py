from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **Kwargs):
    if not instance.bio:
        instance.bio = 'Bio gerada automaticamente.'
    # sender -> módulo
    # instance -> tabela

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **Kwargs):
    car_inventory_update()


# @receiver(pre_delete, sender=Car)
# def car_pre_delete(sender, instance, **Kwargs):
#     print('### PRE DELETE ###')
#     print(instance.model, instance.brand, instance.value)
#     # sender -> módulo
#     # instance -> tabela

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **Kwargs):
    car_inventory_update()
