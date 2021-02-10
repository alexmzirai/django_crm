from django.db import models

# understanding how models work is a vital django pivotal point

# Jesus, help me to grow self esteem and unleash my true potential

class Lead(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    phoned = models.BooleanField(default=False)
    


