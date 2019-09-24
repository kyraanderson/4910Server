from django.db import models

class Sponsor(models.Model):
    identification = models.CharField(max_length=5)
    companyName = models.CharField(max_length=200)
    emailAddress = models.CharField(max_length=200)

    def __str__(self):
        return self.identification


