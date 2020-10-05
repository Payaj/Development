from django.db import models

# Create your models here.
# your class will be your table and attributes of that class will be fields of your table

class signup(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, primary_key = True) # primary_key=True implies unique=True. setting primary key to other field will remove id (auto-incremented) field.
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    # below meta class is to remove an extra s after table's name on admin dashboard. (admin dashboard adds an extra s after the class/table name.)
    class Meta:
        verbose_name_plural = "signup"

class property_type(models.Model):
    type = models.CharField(max_length=20, unique=True, ) # unique means this field can only have unique value, so no duplicate entry in the table.
    #type_description = models.TextField(Blank = True, help_text="Please decribe the property type here. Example: CONDO type is condominium or MULTI-3 is a 3 family house.")

    def __str__(self):
        return self.type

    # below meta class is to remove an extra s after table's name on admin dashboard. (admin dashboard adds an extra s after the class/table name.)
    class Meta:
        verbose_name_plural = "property_type"

class address(models.Model):
    street_address = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    zip = models.CharField(max_length=10)
    type = models.ForeignKey("property_type", on_delete=models.PROTECT) # adding a foreign key here, which will map to the "property_type" table.

    # below meta class is to remove an extra s after table's name on admin dashboard. (admin dashboard adds an extra s after the class/table name.)
    class Meta:
        verbose_name_plural = "address"


class Register(models.Model):
    first_name = models.CharField(max_length=20) # This is one field you have created for your registration form, which will show "Enter Your First Name" on the webpage
    last_name = models.CharField(max_length=20) # This is one field you have created for your registration form, which will show "Enter Your Last Name" on the webpage
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    vpassword = models.CharField(max_length=50)
    prop_type = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
    # below meta class is to remove an extra s after table's name on admin dashboard. (admin dashboard adds an extra s after the class/table name.)
    class Meta:
        verbose_name_plural = "Register"


# class unit_detail(models.Model):
#     sqft = models.IntegerField(Null=True, Default = 0)
