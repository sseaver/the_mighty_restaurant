from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
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
    description = models.CharField(max_length=100)
    price = models.FloatField()


class Order(models.Model):
    server = models.ForeignKey("auth.User")
    item = models.ManyToManyField(MenuItem)
    drink = models.CharField(max_length=20)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    table_number = models.IntegerField()
