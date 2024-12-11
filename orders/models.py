from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=1024)

    class Meta:
        db_table = 'food_order_fooditem'

    def __str__(self):
        return self.name
