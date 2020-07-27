from django.db import models

# Create your models here.
class room(models.Model):
    Address=models.CharField(max_length=100)
    NumberOfRooms=models.IntegerField()
    price=models.FloatField()
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
    date = models.DateField(blank=True, null=True)
>>>>>>> final
>>>>>>> final
=======
>>>>>>> 8ec0bb0a8aadbc8d50544daee769579f9b28d94b
    im2 = models.ImageField(upload_to="site_media", blank="true")
    im3 = models.ImageField(upload_to="site_media", blank="true")
    im4 = models.ImageField(upload_to="site_media", blank="true")
    lender_contact=models.CharField(max_length=100)


<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
    def __str__(self):
        return self.Address

>>>>>>> final
>>>>>>> final
=======
>>>>>>> 8ec0bb0a8aadbc8d50544daee769579f9b28d94b
