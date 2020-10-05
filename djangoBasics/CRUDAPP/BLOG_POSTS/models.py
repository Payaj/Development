from django.db import models

# Create your models here.
class Property_Info(models.Model):
    street_address = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    bed = models.IntegerField()
    bath = models.FloatField()
    sqft = models.FloatField()
    price = models.BigIntegerField()

    def __str__(self):
        return self.street_address
    # below meta class is to remove an extra s after table's name on admin dashboard. (admin dashboard adds an extra s after the class/table name.)
    class Meta:
        verbose_name_plural = "Property_Info"
