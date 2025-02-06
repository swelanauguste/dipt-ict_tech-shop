from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    description = models.TextField()
    image = models.URLField()
    category = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('category',)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
