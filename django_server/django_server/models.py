from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# The model for storing user information
# It includes fields for name, age, title, and hometown
# Name and title are required fields, while age and hometown are optional
# Age has validation to ensure it is a non-negative integer and does not exceed 150 (a reasonable upper limit for human age)
class UserInfoModel(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(150)])
    title = models.CharField(max_length=200, blank=False)
    hometown = models.CharField(max_length=100, blank=True)