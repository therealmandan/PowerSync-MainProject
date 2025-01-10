from django.db import models
# Create your models here.

choices = (
    ('1','type1'),
    ('2','type2')
)

class User(models.Model):
    c_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    email = models.EmailField()
    meter_type = models.CharField(max_length=10,choices=choices)
    
    def __str__(self):
        return self.name
    

class MonthlyMeterReadings(models.Model):
    meter = models.ForeignKey(User,on_delete=models.CASCADE)
    month = models.IntegerField()
    usage = models.FloatField() 
    class Meta:
        unique_together = ('meter', 'month') 


class WeeklyMeterReadings(models.Model):
    meter = models.ForeignKey(User,on_delete=models.CASCADE)
    week = models.IntegerField()
    usage = models.FloatField() 
    class Meta:
        unique_together = ('meter', 'week') 

class DailyMeterReadings(models.Model):
    meter = models.ForeignKey(User,on_delete=models.CASCADE)
    hour = models.IntegerField()
    usage = models.FloatField() 
    class Meta:
        unique_together = ('meter', 'hour') 


