from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from multiselectfield import MultiSelectField

AGE_CHOICES = [
    ('JUNIOR', '0-17'),
    ('ADULT', '18-64'),
    ('SENIOR', '64+')
]

INCOME_CHOICES = [
    ('NO_INCOME', '0'),
    ('LOW_INCOME', '1-12000'),
    ('MEDIUM_INCOME', '12001-40000'),
    ('HIGH_INCOME', '40000+')
]

class AgeBracket(models.Model):
    AGE_CHOICES = [
        ('JUNIOR', '0-17'),
        ('ADULT', '18-64'),
        ('SENIOR', '64+')
    ]
    age = models.CharField(max_length=300, choices=AGE_CHOICES)

    def __str__(self):
        return f"{self.age} ({self.get_age_display()})"


class IncomeBracket(models.Model):
    INCOME_BRACKET_CHOICES = [
        ('NO_INCOME', '0'),
        ('LOW_INCOME', '1-12000'),
        ('MEDIUM_INCOME', '12001-40000'),
        ('HIGH_INCOME', '40000+')
    ]
    income = models.CharField(max_length=300, choices=INCOME_BRACKET_CHOICES)

    def __str__(self):
        return f"{self.income} ({self.get_income_display()})"


class Product(models.Model):
    name = models.CharField(blank=False, max_length=120, unique=True)
    age = MultiSelectField(choices=AGE_CHOICES, default='')
    student = models.BooleanField(blank=False)
    income = MultiSelectField(choices=INCOME_CHOICES, default='')
    slug = models.SlugField(default='', editable=False, max_length=120)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
