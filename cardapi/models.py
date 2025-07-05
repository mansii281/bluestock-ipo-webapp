from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Add more fields here if needed

    def __str__(self):
        return self.title


class IPO(models.Model):
    company_name = models.CharField(max_length=255)
    open_date = models.DateField()
    close_date = models.DateField()
    price_band = models.CharField(max_length=100)
    listing_date = models.DateField()
    logo = models.ImageField(upload_to='logos/')
    rhp_drhp = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.company_name
