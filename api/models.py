from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=255)  # Increased length for name
    description = models.TextField()  # Added description field
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200, null=True, blank=True)  # Added image_url as optional

    def __str__(self):
        return self.name
