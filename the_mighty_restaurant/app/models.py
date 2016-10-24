from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime, timedelta
# Create your models here.

ACCESS_LEVELS = [
    ('s', 'Server'),
    ('o', 'Owner'),
    ('c', 'Chef'),
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)

    def __str__(self):
        return self.access_level

    @property
    def is_owner(self):
        return self.access_level == 'o'

    @property
    def is_chef(self):
        return self.access_level == 'c'

    @property
    def is_server(self):
        return self.access_level == 's'


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.FloatField()

    def __str__(self):
        return self.name


TABLE_NUMBERS = [
    ('a1', 'a1'),
    ('a2', 'a2'),
    ('a3', 'a3'),
    ('a4', 'a4'),
    ('b1', 'b1'),
    ('b2', 'b2'),
    ('b3', 'b3'),
    ('b4', 'b4'),
    ('c1', 'c1'),
    ('c2', 'c2'),
    ('c3', 'c3'),
    ('c4', 'c4'),
    ('d1', 'd1'),
    ('d2', 'd2'),
    ('d3', 'd3'),
    ('d4', 'd4')
]


class Table(models.Model):
    paid = models.BooleanField(default=False)
    table_number = models.CharField(max_length=2, choices=TABLE_NUMBERS)

    def __str__(self):
        return str(self.id)

    @property
    def is_paid(self):
        return self.paid


BOOL_CHOICES = ((True, "Completed"), (False, "Incomplete"))


class Order(models.Model):
    server = models.ForeignKey("auth.User")
    table = models.ForeignKey(Table)
    item = models.ForeignKey(MenuItem)
    drink = models.CharField(max_length=20)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, choices=BOOL_CHOICES)

    def __str__(self):
        return str(self.item)

    def is_recent(self):
        hrs24 = datetime.now() - timedelta(days=1)
        if Order.objects.filter(creation_time__gte=hrs24):
            return True
        else:
            return False

    @property
    def order_profits(self):
        return self.item.price

    @property
    def is_completed(self):
        return self.completed
