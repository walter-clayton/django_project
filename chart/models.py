from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Chart(models.Model):
    chart_id = models.AutoField(primary_key=True)
    date_posted = models.DateField(default=timezone.now)
    chart_assets = models.DecimalField(max_digits=19, decimal_places=10)
    chart_liabilities = models.DecimalField(max_digits=19, decimal_places=10)
    chart_networth = models.DecimalField(max_digits=19, decimal_places=10)

