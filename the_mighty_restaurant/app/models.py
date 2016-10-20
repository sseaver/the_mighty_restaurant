from django.db import models
# Create your models here.

ACCESS_LEVELS = [
    ('s', 'Server'),
    ('o', 'Owner'),
    ('c', 'Chef'),
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)

    @property
    def is_owner(self):
        return self.access_level == 'o'


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    drink = models.CharField(max_length=20)


class Order(models.Model):
    item = models.ForeignKey(Menu)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Table(models.Model):
    order = models.ForeignKey(Order)
    table_number = models.IntegerField()
    seat = models.CharField(max_length=2)
