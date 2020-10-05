from django.db import models

# Create your models here.
class People(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "People"

class ContactInfo(models.Model):
    email = models.ForeignKey(People, on_delete=models.PROTECT)
    phone_number = models.BigIntegerField()

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        verbose_name_plural = "ContactInfo"

class CallInfo(models.Model):
    phone_number = models.ForeignKey(ContactInfo, on_delete=models.PROTECT)
    call_Time = models.DateTimeField()
    call_duration_minute = models.IntegerField()

    class Meta:
        verbose_name_plural = "CallInfo"