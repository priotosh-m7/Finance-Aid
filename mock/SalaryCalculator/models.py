from django.db import models

# Create your models here.

class SalaryCalculator(models.Model):
    ctc_c = models.CharField(max_length=200)
    inhand = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.ctc_c, self.inhand)