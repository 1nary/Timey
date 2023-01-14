from django.db import models



class Lecture(models.Model):
  week = (
    ('1','月曜'),
    ('2','火曜'),
    ('3','水曜'),
    ('4','木曜'),
    ('5','金曜'),
    ('6','土曜'),
  )
  period = (
    ('1','１限'),
    ('2','２限'),
    ('3','３限'),
    ('4','４限'),
    ('5','５限'),
    ('6','６限'),
    ('7','７限'),
  )
  name = models.CharField(max_length=30,blank=False)
  teacher = models.CharField(max_length=30,blank=True)
  room = models.CharField(max_length=20,blank=True)
  week = models.CharField(
    choices=week,
    default=1,
    max_length=1
  )
  period = models.CharField(
    choices=period,
    default=1,
    max_length=1
  )
  def __str__(self):
      return self.name + ',　' + self.teacher + ',　' + self.room
