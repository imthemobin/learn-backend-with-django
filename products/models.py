from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as postgresFields

# Create your models here.
class ProductsCategory(models.Model):
    name = models.CharField(max_length=256)
    Icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_category = models.ForeignKey(
        'self',
        blank=True,
        null= True,
        related_name='children_category',
        on_delete=models.CASCADE

    )
    def __str__(self):
        return self.name

class Maker(models.Model):
    name = models.CharField(max_length=512)
    def __str__(self):
        return self.name

class Product(models.Model):

    class Currency(models.TextChoices):
        SWEDISH_CROWM = ("SEK",_("Swedish Crown"))
        AMERICAN_DOLLAR = ("USD",_("American Dollar"))
        EURO = ("EUR",("Euro"))
        POUND_STERLING =("GBP",("Pound sterling"))
        YEN = ("JPY", "Yen")
        AUSTRALIAN_DOLLAR=("AUD",("Australian Dollar"))
    
    name = models.CharField(max_length=512)
    subtitle = models.CharField(max_length=512)
    maker = models.ForeignKey(
        Maker,
        on_delete=models.CASCADE,
        blank=True,
        null= True,
        related_name="products"
    )

    image1_url = models.URLField(blank=True,null=True)
    image2_url = models.URLField(blank=True,null=True)
    image3_url = models.URLField(blank=True,null=True)
    image4_url = models.URLField(blank=True,null=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    currency = models.CharField(
        max_length=3,
        choices= Currency.choices,
        default=Currency.AMERICAN_DOLLAR
    )

    variation_product_ids = postgresFields.ArrayField(
        models.IntegerField(null=True,blank=True),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} - {self.subtitle} - {self.maker}"