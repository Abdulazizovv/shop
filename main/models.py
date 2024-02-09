from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(default='default-product.jpg')
    price = models.PositiveBigIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Mahsulotlar'
    
    def __str__(self) -> str:
        return self.title


class Warehouse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    arrived = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Omborxona'
    
    def __str__(self) -> str:
        return self.product.title
    
    def save(self, *args, **kwargs):
        # Check if the quantity is 0
        if self.quantity == 0:
            self.is_available = False
        else:
            self.is_available = True

        # Call the superclass method to save the object
        super().save(*args, **kwargs)


class SoldProduct(models.Model):
    product = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    sold_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Sotilgan mahsulotlar'
    
    def __str__(self) -> str:
        return self.product.product.title