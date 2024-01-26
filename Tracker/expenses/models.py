from django.db import models


class Expense(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    published_date = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    distribution_expense = models.FloatField()

    def __str__(self):
        return self.title
