from django.db import models

# Create your models here.
# WEEKDAYS = [
#     (1, ("Monday")),
#     (2, ("Tuesday")),
#     (3, ("Wednesday")),
#     (4, ("Thursday")),
#     (5, ("Friday")),
#     (6, ("Saturday")),
#     (7, ("Sunday")),
# ]


class Menu(models.Model):
    simple_hamburger = models.IntegerField()
    middle_hamburger = models.IntegerField()
    big_hamburger = models.IntegerField()
    water = models.IntegerField()
    hot_chocolate = models.IntegerField()


class Mac(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="menus")
    # weekday = models.IntegerField(choices=WEEKDAYS)
    # from_hour = models.TimeField()
    # to_hour = models.TimeField()
    # menu = models.ManyToManyField(
    #
    # )

    # class Meta:
    #     ordering = ("weekday", "from_hour")
    #     unique_together = ("weekday", "from_hour", "to_hour")
    #
    # def __unicode__(self):
    #     return u'%s: %s - %s' % (self.get_weekday_display(),
    #                              self.from_hour, self.to_hour)

# class Restaurants(models.Model):
#     title = models.CharField(max_length=30)
#     location = models.CharField(max_length=50)

