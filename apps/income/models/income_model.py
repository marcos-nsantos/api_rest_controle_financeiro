from django.db import models


class Income(models.Model):
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    receipt_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
