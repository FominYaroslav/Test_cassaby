from django.db import models

# Create your models here.


class TestModel(models.Model):
    is_test = models.fields.BooleanField(default=True)