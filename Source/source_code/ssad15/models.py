from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class advertisement(models.Model):
    upload = models.FileField(upload_to='uploads/')
    time_len = models.IntegerField(default=30)


# will store the georaphical location of each zone
# affected by initilize_zone.py
class zone(models.Model):
    bottom_left_coordinate_x=models.DecimalField(max_digits=20,decimal_places=17,default=0)
    bottom_left_coordinate_y=models.DecimalField(max_digits=20,decimal_places=17,default=0)


# will store the information about cost of advertisemnt and max number of bundles per zone
# and also the starting time when the change have to be taken into consideration
# at the start it contatins the default values of cost of advertisement and max number of bundles
class zone_info(models.Model) :
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    week = models.IntegerField(default=0)
    cost = models.IntegerField(default=-1)
    no_of_bundles = models.DecimalField(max_digits=10,decimal_places=5,default=0)


class slots(models.Model) :
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    week = models.IntegerField(default=0)
    slot_no = models.IntegerField(default=0)
    no_of_bundles_used = models.DecimalField(max_digits=10,decimal_places=5,default=0)
class scheduler(models.Model) :
    slots_id = models.ForeignKey(slots, on_delete=models.CASCADE)
    advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE)
    bundles_tobegiven = models.DecimalField(max_digits=10,decimal_places=5,default=0)
    is_starting = models.BooleanField(default=True)

# stores the information about advertisement that have to be displayed in the current week
class slot(models.Model):
    zone_id = models.ForeignKey(zone, on_delete=models.CASCADE)
    slot_no = models.IntegerField(default=0)
    advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE)
    is_starting = models.BooleanField(default=True)
    bundles_tobegiven = models.DecimalField(max_digits=5,decimal_places=2,default=0)

# stores the information about number dervices that have been allocated in the given slot_no
# for the given zone
class running(models.Model) :
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    slot_no = models.IntegerField(default=0)
    alloted = models.IntegerField(default=0)

# store the information about the number of devices that have been allocated to
#  a particular advertisement in the given slot and given zone
class running_ads(models.Model) :
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    ad = models.ForeignKey(advertisement, on_delete=models.CASCADE)
    slot_no = models.IntegerField(default=0)
    given = models.IntegerField(default=0)

class running_slots(models.Model) :
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    slot = models.IntegerField(default=1)
    start_time = models.DateTimeField('Starting week of the advertisement',default=timezone.now())

class devices(models.Model):
    username=models.CharField(max_length=10,unique=True)

# class zone(models.Model):
#     total_bundles=models.IntegerField(default=10)
#     bundles_used=models.IntegerField(default=0)
#     cost=models.DecimalField(default=100,max_digits=10,decimal_places=2)
#     bottom_left_coordinate_x=models.DecimalField(max_digits=18,decimal_places=15,default=0)
#     bottom_left_coordinate_y=models.DecimalField(max_digits=18,decimal_places=15,default=0)
#
# class advertisement(models.Model):
#     upload = models.FileField(upload_to='uploads/')
#
# class slot(models.Model):
#     zone_id = models.ForeignKey(zone, on_delete=models.CASCADE)
#     slot_no = models.IntegerField(default=0)
#     advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE)
#     bundles_used = models.DecimalField(max_digits=5,decimal_places=2,default=0)
#
#
#
# #to store  device ids of configured devices
# #to be decided if username of device will be alphanumeric or numeric string
# class devices(models.Model):
#     username=models.CharField(max_length=10,unique=True)
# class running(models.Model):
#     slot_no = models.IntegerField(default=0)
#     zone_id = models.ForeignKey(zone, on_delete=models.CASCADE)
