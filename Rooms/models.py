from django.db import models

# Create your models here.
class room(models.Model):
    Address=models.CharField(max_length=100)
    NumberOfRooms=models.IntegerField()
    price=models.FloatField()
    date = models.DateField(blank=True, null=True)
    im2 = models.ImageField(upload_to="site_media", blank="true")
    im3 = models.ImageField(upload_to="site_media", blank="true")
    im4 = models.ImageField(upload_to="site_media", blank="true")
    lender_contact=models.CharField(max_length=100)


    def __str__(self):
        return self.Address

