from django.db import models
from users.models import User
# Create your models here.


class Beer(models.Model):
    ref = models.IntegerField(null=True)
    name = models.CharField(max_length=200, null=True)
    brewery = models.CharField(max_length=200,null=True)
    style = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200,null=True)
    ABV = models.FloatField(null=True)
    IBU = models.IntegerField(null=True)
    EST_CAL = models.IntegerField(null=True)
    avg_scr = models.FloatField(null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return 'beer_id : {} - {}'.format(self.ref, self.name)


class Rating(models.Model):
    person = models.ForeignKey(User, on_delete='CASCADE')
    rank = models.IntegerField(choices=list(zip(range(1, 6), range(1, 6))))
